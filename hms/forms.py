from django import forms

class SearchForm(forms.Form):
    disease_name = forms.CharField(max_length=50)
    location_name = forms.CharField(max_length=50)

class ReviewForm(forms.Form):
    hname=forms.CharField(max_length=50)
    choice = forms.ChoiceField(choices=('Excellent','Satisfactory','Good','Not upto mark'))
    Comments = forms.TextInput()