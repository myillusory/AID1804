from django import forms
from .models import *
TOPIC_CHOICE = (
    ('1', '好评'),
    ('2', '中评'),
    ('3', '差评'),
)
class RrmarkForm(forms.Form):
    subject = forms.CharField(label='Title')
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Message', widget=forms.Textarea)
    topic = forms.ChoiceField(label='Topic', choices=TOPIC_CHOICE)
    isSaved = forms.BooleanField(label='isSaved')
class LoginForm(forms.Form):
    uname = forms.CharField(label='用户名称')
    upwd = forms.CharField(label='登录密码',widget=forms.PasswordInput)
class RegisterForm(forms.Form):
    uname = forms.CharField(max_length=18, label='用户名称')
    upwd = forms.CharField(widget=forms.PasswordInput, label='用户密码')
    uage = forms.IntegerField(label='用户年龄')
    uemail = forms.EmailField(label='电子邮件')
class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['uname', 'upwd']
        labels = {
            'uname': '用户名称',
            'upwd': '用户密码'
        }
class WidgetForm(forms.Form):
    uname = forms.CharField(label='用户名称', widget=forms.TextInput(
        attrs={
            "name": "user_name",
            "placeholder": "form-control",
            "class": "form-control",
        }
    )
                            )
    upwd = forms.CharField(
        label="用户密码",
        widget=forms.PasswordInput(
            attrs={
                "name": "user_pwd",
                "placeholder": "请输入密码",
                "class": "form-control",
            }
        )
    )