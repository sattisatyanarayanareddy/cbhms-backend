from django import forms


class Patient_details(forms.Form):

    name = forms.CharField(max_length = 100)
    email = forms.CharField(max_length = 150)
    username = forms.CharField(max_length = 150)
    password = forms.CharField(max_length = 150)
    mobile = forms.CharField(max_length = 150)
    gender = forms.CharField(max_length=50)
    specialization = forms.CharField(max_length=120)
    age = forms.IntegerField()
    languages = forms.CharField(max_length=150)
    img = forms.ImageField()

    def clean_image(self):
        image = self.cleaned_data.get('img',False)
        if image:
            if image.size > 10 * 1024 * 1024:
                raise forms.ValidationError("image size is too large")
            return image
        else:
            raise forms.ValidationError("could not read uloaded image")

class Doctors_login(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=150)