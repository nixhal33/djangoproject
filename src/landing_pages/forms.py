from  django import forms

class LandingPageForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    email2 = forms.EmailField(label='Confirm email?')
    password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **krwgs):
        super().__init__(*args,**krwgs)
        for field in self.fields:
            default_css_class= 'form-control' # this will be get from bootstrap
            new_attr={
                "class": default_css_class,
                "id": f"{field}",
                "placeholder": f"Your {field}"
            }
            if field == 'email2':
                new_attr['placeholder']=f"Please confirm your email!!"
            self.fields[field].widget.attrs.update(new_attr)

    def clean(self):
        data = self.cleaned_data
        email = data.get("email")
        email2 = data.get("email2")
        if email2 !=email:
            raise forms.ValidationError("Your email must match!")
        return data

    def clean_email(self):
        data = self.cleaned_data
        email = data.get("email")
        if email.endswith('gmail.com'):
            # self.add_error('email', 'You can\'t use gmail')
            raise forms.ValidationError("You cannot login using the gmail seriously!!!")
        return email
