from django import forms

class wikiForm(forms.Form):
	wiki = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Search'}))

class titleForm(forms.Form):
	title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Title'}))

class bodyForm(forms.Form):
	body = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Type your paragraph.'}))