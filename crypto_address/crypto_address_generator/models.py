from django.db import models

from django.db import models


class Address(models.Model):
    id = models.AutoField(primary_key=True)
    currency = models.CharField(
        max_length=3,
        verbose_name='Acronym',
        help_text="The three-letter acronym for the cryptocurrency."
    )
    address = models.CharField(
        max_length=100,
        verbose_name='Address',
        help_text="The valid address for the specified cryptocurrency."
    )

    def __str__(self):
        return f"{self.currency} Address: {self.address}"
