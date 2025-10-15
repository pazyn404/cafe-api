from django.core.management.base import BaseCommand
from django_celery_beat.models import IntervalSchedule, PeriodicTask


class Command(BaseCommand):
    help = "Create crontab to print rendered checks"

    def handle(self, *args, **kwargs):
        schedule, _ = IntervalSchedule.objects.get_or_create(
            every=1,
            period=IntervalSchedule.MINUTES,
        )
        _, create = PeriodicTask.objects.get_or_create(
            interval=schedule,
            name="api.tasks.print_rendered_checks",
            task="api.tasks.print_rendered_checks",
        )

        if create:
            self.stdout.write(self.style.SUCCESS("Crontab successfully created"))
        else:
            self.stdout.write(self.style.WARNING("Skipping crontab creation"))
