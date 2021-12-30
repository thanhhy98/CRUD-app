from django.forms import ModelForm
from .models import WebForm

class FromWebForm(ModelForm):
    class Meta:
        model = WebForm
        fields = '__all__'