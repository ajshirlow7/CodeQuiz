from django.urls import path
from .views_clean import home_page_view, register_view, login_view, logout_view, quiz_html_view, quiz_css_view, quiz_javascript_view, quiz_python_view

urlpatterns = [
    path("", home_page_view, name='home'),
    path("register/", register_view, name='register'),
    path("login/", login_view, name='login'),
    path("logout/", logout_view, name='logout'),
    path("quiz/html/", quiz_html_view, name='quiz_html'),
    path("quiz/css/", quiz_css_view, name='quiz_css'),
    path("quiz/javascript/", quiz_javascript_view, name='quiz_javascript'),
    path("quiz/python/", quiz_python_view, name='quiz_python'),
]
