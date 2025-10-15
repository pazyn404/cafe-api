import os

from django.db import models


class Printer(models.Model):
    point_id = models.IntegerField(db_index=True)
    name = models.CharField(max_length=255)
    api_key = models.CharField(unique=True, max_length=255)
    check_type = models.CharField(
        max_length=16,
        choices=[
            ("kitchen", "Kitchen"),
            ("client", "Client")
        ]
    )


class Check(models.Model):
    class Meta:
        indexes = [
            models.Index(models.F("order__id"), name="check_order_id")
        ]

    printer = models.ForeignKey(Printer, on_delete=models.CASCADE)
    order = models.JSONField()
    type = models.CharField(
        max_length=16,
        choices=[
            ("kitchen", "kitchen"),
            ("client", "client")
        ]
    )
    status = models.CharField(
        max_length=16,
        default="new",
        choices=[
            ("new", "new"),
            ("rendered", "rendered"),
            ("printed", "printed")
        ]
    )
    pdf_file = models.FileField(upload_to=os.environ["CHECK_DIR_PATH"], blank=True)
