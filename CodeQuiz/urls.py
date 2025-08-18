
from django.urls import path
from .views import home_page_view, register_view, login_view, logout_view, leaderboard_view, html_quiz_view, css_quiz_view, javascript_quiz_view, python_quiz_view


urlpatterns = [
    path("", home_page_view, name='home'),
    path("register/", register_view, name='register'),
    path("login/", login_view, name='login'),
    path("logout/", logout_view, name='logout'),
    path("leaderboard/", leaderboard_view, name='leaderboard'),
    path("html-quiz/", html_quiz_view, name='html_quiz'),
    path("css-quiz/", css_quiz_view, name='css_quiz'),
    path("javascript-quiz/", javascript_quiz_view, name='javascript_quiz'),
    path("python-quiz/", python_quiz_view, name='python_quiz'),
]
