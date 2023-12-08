from django.db import models
from cloudinary.models import CloudinaryField


# ユーザー認証
from django.contrib.auth.models import User

# ユーザーアカウントのモデルクラス
class Account(models.Model):

    # ユーザー認証のインスタンス(1vs1関係)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # 追加フィールド
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    account_image = models.ImageField(upload_to='img/', null=True, default='default_image.png')

    # Cloudinary画像フィールドを追加
    account_image = CloudinaryField('account_image', null=True)

    def __str__(self):
        return self.user.username





from django.urls import reverse_lazy
from django.utils import timezone

class MainCategory(models.Model):    #Artistのメインカテゴリ
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True)
    
    def __str__(self):
        return self.name
    
    



class Tag(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True)
    
    def __str__(self):
        return self.name


class Post(models.Model):
    created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        blank=False,
        null=False)
    
    updated = models.DateTimeField(
        auto_now=True,
        editable=False,
        blank=False,
        null=False)
    

    # 画像の保存先としてMEDIA_ROOTで指定したディレクトリの下のimgディレクトリを指定
    image = models.ImageField(upload_to='img/', null=True, default='default_image.png')

    # Cloudinary画像フィールドを追加
    image = CloudinaryField('image', null=True)
        
    title = models.CharField(
        max_length=255,
        blank=False,
        null=False)

        
    body = models.TextField(
        blank=True,
        null=False)
    
    links = models.CharField(
        max_length=255,
        blank=True,
        null=True)

    category = models.ForeignKey(
        MainCategory,
        on_delete=models.CASCADE)
        
    tags = models.ManyToManyField(
        Tag,
        blank=True)
    

    created_at = models.DateTimeField(default=timezone.now)  # 登録日時を保存するフィールド

    

    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse_lazy("detail", args=[self.id])
    

