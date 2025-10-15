import os
import json

import requests
from celery import shared_task
from django.core.files.base import ContentFile

from cafe import settings
from .models import Check


@shared_task(ignore_result=True)
def render_check(check_id):
    check = Check.objects.get(pk=check_id)

    data = json.dumps(check.order)
    template = open(os.environ["CHECK_TEMPLATE_PATH"], "rb")
    response = requests.post(
        os.environ["WEBRENDERER_URL"],
        data={"data": data},
        files={"template": template}
    )

    if response.status_code != 200:
        raise Exception(response.text)

    filename = f"{check.order['id']}_{check.type}"
    check.pdf_file.save(f"{filename}.pdf", ContentFile(response.content))
    check.status = "rendered"
    check.save()


@shared_task(ignore_result=True)
def print_rendered_checks():
    def print_checks(checks):
        for check in checks:
            check.status = "printed"
            check.save()

    rendered_client_checks = Check.objects.filter(status="rendered", type="client")
    rendered_kitchen_checks = Check.objects.filter(status="rendered", type="kitchen")

    print_checks(rendered_client_checks)
    print_checks(rendered_kitchen_checks)
