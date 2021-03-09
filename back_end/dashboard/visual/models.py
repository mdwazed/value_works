from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from visual.custom_validators.validators import month_validator




class Marketing(models.Model):
    month = models.CharField(max_length=3, validators=[month_validator])
    social_media_follower = models.IntegerField(null=True)
    website_visitors = models.IntegerField(null=True)
    lead_ratio = models.DecimalField(max_digits=5, decimal_places=2, null=True) # in percentile

    def __str__(self):
        return f'marketing--{self.month}--{self.social_media_follower}'

class Customers(models.Model):
    month = models.CharField(max_length=3, validators=[month_validator])
    net_promoter_score = models.IntegerField(null=True)
    net_new_customer = models.IntegerField(null=True)
    num_of_customer = models.IntegerField(null=True)

    def __str__(self):
        return f'customer--{self.month}--{self.net_promoter_score}'

class ProductDevelopment(models.Model):
    month = models.CharField(max_length=3, validators=[month_validator])
    dev_freq = models.IntegerField(null=True)
    test_accuracy = models.DecimalField(max_digits=5, decimal_places=2, null=True) # in percentile
    test_coverage = models.DecimalField(max_digits=5, decimal_places=2, null=True) # in percentile

    def __str__(self):
        return f'product development--{self.month}--{self.dev_freq}'


class ProductOperation(models.Model):
    month = models.CharField(max_length=3, validators=[month_validator])
    sp_avg_reaction_time = models.IntegerField(null=True) # in seconds
    sp_avg_resolution_time = models.IntegerField(null=True) # in seconds
    customer_escalation = models.IntegerField(null=True)
    availability = models.DecimalField(max_digits=5, decimal_places=2, null=True) # in percentile
    open_support_ticket = models.IntegerField(null=True)

    def __str__(self):
        return f'product operation--{self.month}--{self.availability}'


class Hr(models.Model):
    month = models.CharField(max_length=3, validators=[month_validator])
    num_of_employee = models.IntegerField(null=True)
    num_of_open_position = models.IntegerField(null=True)
    time_to_hire = models.IntegerField(null=True) # in days
    attrition = models.DecimalField(max_digits=5, decimal_places=2, null=True) # in percentile

    def __str__(self):
        return f'hr--{self.month}--{self.num_of_employee}'


class ProfitLoss(models.Model):
    month = models.CharField(max_length=3, validators=[month_validator])
    software_revenue = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    other_revenue = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    professional_service_revenue = models.DecimalField(max_digits=9, decimal_places=2, null=True)