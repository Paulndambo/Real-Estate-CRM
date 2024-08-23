from typing import Iterable
from django.db import models
from apps.core.models import AbstractBaseModel
from dateutil.relativedelta import relativedelta
from datetime import datetime

INSTALLMENT_STATUSES = (
    ("Paid", "Paid"),
    ("Pending", "Pending"),
    ("Defaulted", "Defaulted"),
    ("Future", "Future"),
)
# Create your models here.
class ClientPaymentPlan(AbstractBaseModel):
    client = models.ForeignKey("users.Client", on_delete=models.CASCADE)
    unit = models.ForeignKey("properties.PropertyUnit", on_delete=models.SET_NULL, null=True)
    booking_fee = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    deposit_fee = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    period = models.IntegerField(default=1)
    installment_amount = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    total_amount = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    first_repayment_date = models.DateField(null=True)
    fully_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.client.name
    
    def save(self, *args, **kwargs):
        # Call the original save method
        super().save(*args, **kwargs)

        self.create_installments()
        

    def create_installments(self):
        payment_date = datetime.strptime(self.first_repayment_date, '%Y-%m-%d').date()
        for month in range(1, int(self.period) + 1):
            installment = ClientInstallment.objects.create(
                client=self.client,
                payment_plan=self,
                amount_expected=self.installment_amount,
                date_expected=payment_date
            )
            
            payment_date = payment_date + relativedelta(months=1)
            print(f"Next Expected Date is: {payment_date}")
    

class ClientInstallment(AbstractBaseModel):
    client = models.ForeignKey("users.Client", on_delete=models.CASCADE, related_name="clienstallments")
    payment_plan = models.ForeignKey(ClientPaymentPlan, on_delete=models.CASCADE, related_name="planinstallments")
    amount_expected = models.DecimalField(max_digits=100, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    date_expected = models.DateField(null=True)
    paid = models.BooleanField(default=False)
    status = models.CharField(max_length=255, choices=INSTALLMENT_STATUSES, default="Future")

    def __str__(self):
        return self.client.name


class ClientPayment(AbstractBaseModel):
    client = models.ForeignKey("users.Client", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=100, decimal_places=2)

    def __str__(self):
        return self.client.name