from django import forms

class IssueForm(forms.Form):
    commit_id = forms.CharField(max_length=40,min_length=40)
    url = forms.URLField(label='Url of the issue')