from django.core.management.base import BaseCommand

from api.models import Printer


class Command(BaseCommand):
    help = "Create default printers"

    def handle(self, *args, **kwargs):
        if Printer.objects.exists():
            self.stdout.write(self.style.WARNING("Skipping printers creation"))
            return

        Printer.objects.bulk_create([
            Printer(name='printer1.1', api_key="key1.1", check_type="client", point_id=1),
            Printer(name='printer1.2', api_key="key1.2", check_type="kitchen", point_id=1),
            Printer(name='printer2.1', api_key="key2.1", check_type="client", point_id=2)
        ])
        self.stdout.write(self.style.SUCCESS("Default printers successfully created"))
