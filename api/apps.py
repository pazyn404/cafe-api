import json

from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "api"

    # def ready(self):
    #     from django_celery_beat.models import PeriodicTask, IntervalSchedule
    #     from django.db.utils import OperationalError, ProgrammingError
    #
    #     try:
    #         schedule, _ = IntervalSchedule.objects.get_or_create(
    #             every=10,
    #             period=IntervalSchedule.SECONDS,
    #         )
    #
    #         PeriodicTask.objects.get_or_create(
    #             interval=schedule,
    #             task="api.tasks.send_email_task",
    #             name="api.tasks.send_email_task",
    #             args=json.dumps([1])
    #         )
    #     except (OperationalError, ProgrammingError):
    #         pass
