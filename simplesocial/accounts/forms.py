# for getting user infromation
from django.contrib.auth import get_user_model
# for creating user form
from django.contrib.auth.forms import UserCreationForm

# A form for crearing a form
class UserCreateForm(UserCreationForm):
    
    # connecting to model
    class Meta:
        fields = ('username','email','password1','password2')
        model = get_user_model()
         
        # editing the labels of the fields of the form
        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            self.fields['username'].label = 'Display Name'
            self.fields['email'].label  = 'Email Address'



