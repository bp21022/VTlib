from django import forms
from .models import Post
from django.conf import settings


from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.core.mail import send_mail
from .models import Account

# subject = "登録確認"
# message_template = """
# ご登録ありがとうございます。
# 以下URLをクリックして登録を完了してください。

# """

# def get_activate_url(user):
#     uid = urlsafe_base64_encode(force_bytes(user.pk))
#     new_token = default_token_generator.make_token(user)  # 新しいトークンの生成
#     print(f"Newly generated token for user {user.pk}: {new_token}")  # 新しいトークンをコンソールに表示
#     return settings.FRONTEND_URL + f"/activate/{uid}/{new_token}/"


class AccountForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label="パスワード")

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        labels = {'username': "ユーザーID", 'email': "メール"}

    # def save(self, commit=True):
    #     # commit=Falseだと、DBに保存されない
    #     user = super().save(commit=False)
    #     user.email = self.cleaned_data["email"]
        
        # 確認するまでログイン不可にする
        #user.is_active = False
        
        # if commit:
        #     user.save()
        #     activation_link = get_activate_url(user)
        #     print(f"New activation link with updated token: {activation_link}")  # 新しいアクティベーションリンクを表示
        #     message = message_template + activation_link
        #     user.email_user(subject, message)
        # return user

class AddAccountForm(forms.ModelForm):
    class Meta():
        # モデルクラスを指定
        model = Account
        fields = ('last_name','first_name','account_image',)
        labels = {'last_name':"苗字",'first_name':"名前",'account_image':"写真アップロード",}



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "image", "body", "category", "tags", "links"]



# from django.utils.encoding import force_str
# from django.utils.http import urlsafe_base64_decode
# from django.contrib.auth.tokens import default_token_generator

# def activate_user(uidb64, token):    
#     try:
#         uid = urlsafe_base64_decode(uidb64).decode()
#         user = User.objects.get(pk=uid)
#         print(f"User ID: {uid}, User: {user}")
#     except Exception as e:
#         print(f"Exception: {e}")
#         return False

#     if default_token_generator.check_token(user, token):
#         user.is_active = True
#         user.save()
#         print("User activated successfully.")
#         return True
#     else:
#         print("Token validation failed. User activation failed.")

#     print("Token validation failed.")
#     return False


from django import forms
from .models import Tag

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']