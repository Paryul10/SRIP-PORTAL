from django import forms

class IssueForm(forms.Form):
    commit_id = forms.CharField(max_length=40,min_length=40)
    url = forms.URLField(label='Url of the issue')

class ReportForm(forms.Form):
    report = forms.URLField(label='Link to the Wiki Page')

class HandleForm(forms.Form):
    handle = forms.CharField(max_length=40,label='Git Handle')
    handle_confirm = forms.CharField(max_length=40,label='Confirm Git Handle')

    # def __init__(self, *args, **kwargs):
    #     super(HandleForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
    #     self.fields['handle'].widget.attrs['style'] = 'width:100px; height:40px;'
    #     self.fields['handle_confirm'].widget.attrs['style']  = 'width:800px; height:80px;'

    def clean(self):
        cleaned_data = super().clean()    #inbuilt clean.

        handle_form = cleaned_data.get('handle')
        handle_form_confirm = cleaned_data.get('handle_confirm')
        
        if handle_form != handle_form_confirm:
            print('Not Equal')
            raise forms.ValidationError('Fields Do NOT match')

        # return handle_form