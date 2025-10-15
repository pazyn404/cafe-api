from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from .serializers import OrderSerializer
from .models import Printer, Check
from .tasks import render_check


@extend_schema(
    request=OrderSerializer,
    responses={
        200: OrderSerializer
    },
    auth=None
)
@api_view(["POST"])
def create_order(request):
    def create_checks(printers, check_type):
        for printer in printers:
            check = Check(printer=printer, type=check_type, order=order_serializer.data)
            check.save()

            render_check.delay(check.pk)

    order_serializer = OrderSerializer(data=request.data)
    order_serializer.is_valid(raise_exception=True)

    if Check.objects.filter(order__id=order_serializer.data["id"]).exists():
        raise ValidationError(f"Order ({order_serializer.data['id']}) already exists")

    client_check_printers = Printer.objects.filter(point_id=order_serializer.data["point_id"], check_type="client")
    kitchen_check_printers = Printer.objects.filter(point_id=order_serializer.data["point_id"], check_type="kitchen")

    printer_errors = []
    if not client_check_printers.exists():
        printer_errors.append("There are no client printers for this point")
    if not kitchen_check_printers.exists():
        printer_errors.append("There are no kitchen printers for this point")
    if printer_errors:
        raise ValidationError(printer_errors)

    create_checks(client_check_printers, "client")
    create_checks(kitchen_check_printers, "kitchen")

    return Response(order_serializer.data)
