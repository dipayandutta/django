from django import forms
from .models import Sinppet
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Submit


class NameWidget(forms.MultiWidget):

    def __init__(self,attrs=None):
        super().__init__([
            forms.TextInput(),
            forms.TextInput()
        ],attrs)

    def decompress(self,value):
        if value:
            return value.split('')
        return ['','']

class NameField(forms.MultiValueField):

    widget = NameWidget
    def __init__(self,*args,**kwargs):

        fields = (
            forms.CharField(),
            forms.CharField(),
        )

        super().__init__(fields,*args,**kwargs)

    def compress(self,data_list):
        return f'{data_list[0]} {data_list[1]}'

class ContactForm(forms.Form):
    #name    = forms.CharField()
    # Multivalue field Example
    name    = NameField()
    email   = forms.CharField(label='E-mail')
    category= forms.ChoiceField(choices=[('question','Question'),('other','Other')])
    subject = forms.CharField(required=False)
    body    = forms.CharField(widget=forms.Textarea)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper = FormHelper
        self.helper.form_method = 'post'

        #Adding Submit Button
        self.helper.layout = Layout(
            'name',
            'email',
            'category',
            'subject',
            'body',
            Submit('submit','Submit',css_class='btn-success')
            
        )


class SnipperForm(forms.ModelForm):

    class Meta:
        model  = Sinppet
        fields = ('name','body')