from django import forms




class GetPath(forms.Form):
	origin = forms.CharField(label = "origin")
	to = forms.CharField(label = "to")	