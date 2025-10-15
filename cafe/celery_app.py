import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cafe.settings")

celery_app = Celery(__name__)
celery_app.config_from_object("django.conf:settings", namespace="CELERY")
