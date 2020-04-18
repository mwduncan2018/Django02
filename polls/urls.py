from django.urls import path

from . import views


app_name = 'polls'
urlpatterns = [
    path(r'<int:question_id>/', views.detail, name='detail'),
    path(r'more/detail/<int:question_id>/<str:extra_word>/', views.more_detail, name='more_detail'),
    path(r'<int:question_id>/results/', views.results, name='results'),
    path(r'<int:question_id>/vote/', views.vote, name='vote'),
    path(r'question/list/', views.question_list, name='question_list'),
    path(r'shortcut/question/list/', views.question_list_shortcut, name='question_list_shortcut'),
    path(r'deliberate/404/', views.deliberate_404, name='deliberate_404'),
    path(r'raise/404/if/<int:question_id>/does/not/exist/', views.raise_404_if_question_does_not_exist, name='raise_404_if_question_DNE'),
    path(r'link/library/', views.link_library, name='link_library'),
    path(r'minimal/form/<int:question_id>/', views.minimal_form, name='minimal_form'),
    path(r'v2/<int:question_id>/', views.v2, name='v2'),
    
    path(r'show/all/choices', views.show_all_choices, name='show_all_choices'),
    
    path(r'', views.index, name='index'),
]