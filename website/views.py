from django.views.generic import TemplateView
from django.shortcuts import render

class IndexView(TemplateView):
    template_name = "index.html"

class AboutView(TemplateView):
    template_name = "about.html"

class Index_LoginedViwe(TemplateView):
    template_name = "Index_logined.html"

class ContactViwe(TemplateView):
    template_name = "contact.html"

class EliteFourView(TemplateView):
    template_name = "Elite_four.html"

class UsageView(TemplateView):
    template_name = "usage-policy.html"

from django.views.generic import ListView, DetailView
from .models import Post
from .forms import PostForm
from django.shortcuts import render, get_object_or_404 # get_object_or_404を追加
from django.shortcuts import redirect
from .models import MainCategory, Tag

class Index(ListView):
    # 一覧するモデルを指定 >>> "object_list" で取得
    model = Post
    template_name = 'website/post_list.html'
    context_object_name = 'object_list'
    paginate_by = 5  # ページあたりのアイテム数

    def get_queryset(self):
        return Post.objects.all().order_by('-created_at')

class Detail(DetailView):
    model = Post  # モデル名を正確に指定してください

    # def get(self, request, *args, **kwargs):
    #     # URLパラメーターからpkを取得します。
    #     pk = self.kwargs.get('pk')
        
    #     # pkが10の場合、ルートURLにリダイレクトします。
    #     if pk > 0:
    #         return redirect('/')
        
    #     # それ以外の場合は通常のDetailViewのget()を呼び出します。
    #     return super().get(request, *args, **kwargs)


from django.views.generic.edit import CreateView

# CreateViewは新規登録画面を簡単に作るためのView
class Create(CreateView):
    model = Post
    form_class = PostForm

from django.views.generic.edit import UpdateView

class Update(UpdateView):
    model = Post
    form_class = PostForm

from django.views.generic.edit import DeleteView

class Delete(DeleteView):
    model = Post
    # 削除したあとに移動する先（トップページ）
    success_url = "/logined"

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm



def create_post(request):
    params = {
        "title": "画像のアップロード",
        "upload_form": PostForm(),
        "id": None,
        "related_tags": None,
    }

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)

            # タイトルに紐づいた投稿から関連するタグを取得
            related_tags = post.tags.all()
            
            # 取得したタグ情報をパラメータに追加
            params["related_tags"] = related_tags
            
            post.save()  # 投稿を保存
            params["id"] = post.id

    return render(request, 'post_form.html', params)

def preview(request, image_id=0):
 
    upload_image = get_object_or_404(Post, id=image_id)
 
    params = {
        'title': '画像の表示',
        'id': upload_image.id,
        'url': upload_image.image.url
    }
 
    return render(request, 'website/post_form.html', params)


# def posts_list_gets(request):
#     # すべての投稿を取得する
#     posts = Post.objects.all().order_by('created_at')
    
#     context = {
#         'posts': posts,
#     }
    
#     return render(request, 'website/logined_comp_list.html', context)



from django.shortcuts import render
from django.db.models import Q
from .models import Post

def search_posts(request):
    keyword = request.GET.get('key', '')  # キーワードを取得
    genre = request.GET.get('genre', '')  # ジャンルを取得

    # キーワードとジャンルに基づいて投稿をフィルタリング
    posts = Post.objects.all()

    if keyword:
        posts = posts.filter(Q(title__icontains=keyword) | Q(body__icontains=keyword))

    if genre:
        posts = posts.filter(category__name=genre)

    return render(request, 'website/searched_logined.html', {'filtered_posts': posts})


# from django.views import View
# class LoginedCompView(View):
#     def get(self, request):
#         # ロジックを追加する（必要に応じてデータを取得し、テンプレートをレンダリングするなど）
#         # ここでは単純なレンダリングを行いますが、必要に応じてビューロジックを追加してください。
#         return render(request, 'website/logined_comp.html')  # レンダリングするテンプレートを指定します
    


# マイページ用
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.contrib.auth.models import User

class MyPageView(LoginRequiredMixin, DetailView):
    model = User  # Userモデルを使っていますが、自分のプロフィールモデルを使う場合はそれに置き換えます
    template_name = 'website/my_page.html'  # マイページを表示するテンプレート名
    context_object_name = 'user_data'  # テンプレートで使うオブジェクト名

    def get_object(self, queryset=None):
        return self.request.user
    



from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import AccountForm, AddAccountForm
from django.contrib.auth.models import User

class AccountRegistration(TemplateView):

    template_name = 'registration/register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['AccountCreate'] = False
        context['account_form'] = AccountForm()
        context['add_account_form'] = AddAccountForm()
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        account_form = AccountForm(request.POST)
        add_account_form = AddAccountForm(request.POST, request.FILES)
        
        if account_form.is_valid() and add_account_form.is_valid():
            account = account_form.save(commit=False)
            account.set_password(account.password)
            account.save()

            add_account = add_account_form.save(commit=False)
            add_account.user = account

            if 'account_image' in request.FILES:
                add_account.account_image = request.FILES['account_image']

            add_account.save()

            context = self.get_context_data()
            context['AccountCreate'] = True
            context['success_message'] = "登録が完了しました。"  # 成功メッセージを追加

            return render(request, self.template_name, context)

        else:
            print(account_form.errors)
            print(add_account_form.errors)
            context = self.get_context_data()
            context['account_form'] = account_form
            context['add_account_form'] = add_account_form
            return render(request, self.template_name, context)


# from django.views.generic import TemplateView
# from .forms import activate_user

# class ActivateView(TemplateView):
#     template_name = "registration/activate.html"
    
#     def get(self, request, uidb64, token, *args, **kwargs):
#         # 認証トークンを検証して、
#         result = activate_user(uidb64, token)
#         # コンテクストのresultにTrue/Falseの結果を渡します。
#         return super().get(request, result=result, **kwargs)



    

# views.py
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

def good(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        post.good += 1
        post.save()

        return JsonResponse({'likes': post.good})
    

#タグを追加する
from django.shortcuts import render, redirect
from .forms import TagForm
from .models import Tag

def add_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            tag = form.save()  # タグを保存
            return redirect('https://vtuber-library.onrender.com/create/')
    else:
        form = TagForm()

    tags = Tag.objects.all()  # すべてのタグを取得

    if request.method == 'POST' and 'delete_tag' in request.POST:
        tag_id = request.POST.get('delete_tag')  # 削除するタグの ID を取得
        tag_to_delete = get_object_or_404(Tag, pk=tag_id)  # 削除するタグを取得
        tag_to_delete.delete()  # タグを削除
        return redirect('https://vtuber-library.onrender.com/create/')  # 削除後にリダイレクト

    return render(request, 'website/add_tag.html', {'form': form, 'tags': tags})

def delete_tag(request):
    if request.method == 'POST':
        # 削除の処理を実装する
        pass  # ここに削除のロジックを記述

    # リダイレクトや必要なレスポンスを返す
    return redirect('https://vtuber-library.onrender.com/create/')



# モデルのインポート
from website.models import Post

# Cloudinaryの設定
import cloudinary
from cloudinary.uploader import upload

def upload_image_to_cloudinary(image_file):
    # Cloudinaryに画像をアップロード
    uploaded_image = upload(image_file, folder="your_folder")  # 必要に応じてフォルダーを指定
    # Cloudinaryから取得したURLを返す
    return uploaded_image['secure_url']

# ビュー内での画像アップロード処理
def your_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # 新しいモデルインスタンスを作成
            new_instance = Post()
            # アップロードされた画像のURLを取得
            image_url = upload_image_to_cloudinary(request.FILES['image'])
            # アップロードされた画像のURLをモデルのフィールドに保存
            new_instance.image = image_url
            new_instance.save()  # 新しいモデルインスタンスを保存
            # リダイレクトなどの追加処理...
    else:
        form = PostForm()
    return render(request, 'website/post_list.html', {'form': form})
