from django.forms import ModelForm


class ResourceForm(ModelForm):
    class Meta:
        include = '__all__'


class CardForm(ModelForm):
    class Meta:
        include = '__all__'
