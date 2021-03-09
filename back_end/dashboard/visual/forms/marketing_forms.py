from django.forms import Form, ModelForm
from visual.models import Marketing


class MarketingForm(ModelForm):

    class Meta:
        model = Marketing
        fields = '__all__' 
