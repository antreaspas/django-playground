from django.urls import path

from blog.app import views

urlpatterns = [
    path('articles/', views.ArticlesListCreateView.as_view()),
    path('articles/<int:id>', views.ArticleRetrieveUpdateDestroyView.as_view()),
    path('articles/<int:article_id>/comments', views.CommentsListCreateView.as_view()),
    path('articles/<int:article_id>/comments/<int:key>', views.CommentRetrieveUpdateDestroyView.as_view()),
]
