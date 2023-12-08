from django.urls import path
from .views import IndexView, AboutView, ContactViwe, EliteFourView,  MyPageView , UsageView, delete_tag
from . import views

urlpatterns = [
    
    path("", IndexView.as_view()), 
    path("about/", AboutView.as_view()),
    path("contact/", ContactViwe.as_view()),
    path("Elite_four/", EliteFourView.as_view()),
    path("usage-policy/", UsageView.as_view()),

    path("logined/", views.Index.as_view(), name="index"), 
    path('detail/<int:pk>/', views.Detail.as_view(), name="detail"),
    path("create/", views.Create.as_view(), name="create"),
    path('update/<int:pk>/', views.Update.as_view(), name="update"),
    path('delete/<int:pk>/', views.Delete.as_view(), name="delete"),
    path('preview/<int:pk>/', views.preview, name='preview'), # 追記
    path('searched_logined/', views.search_posts, name='search_posts'), # 検索用
    #path("logined_comp/", views.LoginedCompView.as_view(), name="logined_comp"),  # 新しいビューを追加する場合
    path('my_page/', MyPageView.as_view(), name='my_page'), #マイページ
    path('register/', views.AccountRegistration.as_view(), name='register'),
    path('logined/<int:pk>/', views.good, name='toggle_like'),
    path('add_tag/', views.add_tag, name='add_tag'),
    path('delete_tag/', views.delete_tag, name='delete_tag'),
]