from django import forms
from .models import *


class ProfileForm(forms.Form):
    position_title = forms.CharField(required=True, label="Position Title",widget=forms.TextInput(attrs={"class":"form-control",'placeholder':'Google Software Engineer'}))
    country = forms.CharField(required=True, label="Country",widget=forms.TextInput(attrs={"class":"form-control",'placeholder':'Bangladesh'}))
    call = forms.IntegerField(required=True,label="Phone Number",widget=forms.NumberInput(attrs={"class":"form-control",'placeholder':"01700000000"}))
    address = forms.Textarea(attrs={"class":"form-control",'placeholder':'Naher Mantion, House No -00, Road-5, Lane-02, Block-G, Dhanmondi, Dhaka, Bangladesh'})
    description = forms.Textarea(attrs={"class":"form-control",'placeholder':'Hi, This is Jhon......'})
    

    class Meta:
        model = Profile
        fields =['position_title','call','country','address','description']






