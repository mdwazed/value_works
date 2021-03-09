

def month_validator(value):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep',
            'Oct', 'Nov', 'Dec',]
    if value not in months:
        raise ValidationError(
            _('%(value)s is not a velid month'),
            params={'value': value},
        )