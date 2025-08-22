from django import forms

# Create your models here.

class FormMixin:
    def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         self.apply_style_widget()
         self.remove_help_text()

    common_classes ="border-2 focus:outline-none px-3 py-2 rounded no-spinner"

    def apply_style_widget(self):

        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.TextInput):
                field.widget.attrs.update({
                    'class': f'{self.common_classes} w-full',
                })
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    'class': f'{self.common_classes} w-full',
                    'rows':2
                })
            elif isinstance(field.widget, forms.SelectDateWidget):
                field.widget.attrs.update({
                    'class': self.common_classes
                })
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs.update({
                    'class':f'{self.common_classes} w-full'
                })
            else:
                field.widget.attrs.update({
                    'class':f'{self.common_classes} w-full'
                })

    def remove_help_text(self):
         for _, field in self.fields.items():
            field.label = ""


class RegisterForm(FormMixin, forms.Form):
    first_name= forms.CharField(widget=forms.TextInput(attrs={"placeholder":"First Name"}),required=True)
    last_name= forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Last Name"}),required=True)
    phone= forms.IntegerField(widget=forms.NumberInput(attrs={
        "placeholder":"Phone Number",
        }),
        required=True
        )
    email= forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"Email Address"}),required=True)
    
    

class LoginForm(FormMixin, forms.Form):
    user_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"placeholder":"User Name"}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={"placeholder":"************"}))


     
    


