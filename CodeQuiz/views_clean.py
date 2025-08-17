
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import json

def home_page_view(request):
    """
    Render the home page of the CodeQuiz application.
    """
    return render(request, 'home.html')

def register_view(request):
    """
    Handle user registration via AJAX POST request.
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')

            # Validate input
            if not username or not password:
                return JsonResponse({
                    'success': False,
                    'message': 'Username and password are required.'
                })

            # Check if user already exists
            if User.objects.filter(username=username).exists():
                return JsonResponse({
                    'success': False,
                    'message': 'Username already exists.'
                })

            # Create new user
            User.objects.create_user(username=username, password=password)
            return JsonResponse({
                'success': True,
                'message': 'Account created successfully!'
            })

        except json.JSONDecodeError:
            return JsonResponse({
                'success': False,
                'message': 'Invalid data format.'
            })

# Quiz views

from .seed_html_quiz import QUESTIONS as HTML_QUESTIONS
from .seed_css_quiz import QUESTIONS as CSS_QUESTIONS
from .seed_javascript_quiz import QUESTIONS as JS_QUESTIONS
from .seed_python_quiz import QUESTIONS as PYTHON_QUESTIONS
from django.core.paginator import Paginator


def quiz_html_view(request):
    page_number = request.GET.get('page', 1)
    paginator = Paginator(HTML_QUESTIONS, 10)
    page_obj = paginator.get_page(page_number)
    score = None
    total_questions = len(page_obj.object_list)
    if request.method == 'POST':
        # Calculate score based on submitted answers
        score = 0
        for idx, question in enumerate(page_obj.object_list, start=1):
            user_answers = request.POST.getlist(f'q{idx}')
            correct_answers = []
            if hasattr(question, 'answers'):
                correct_answers = [a[0] for a in question.answers if len(a) > 1 and a[1] is True]
            elif hasattr(question, 'choices') and hasattr(question, 'correct'):
                correct_answers = question.correct if isinstance(question.correct, list) else [question.correct]
            if set(user_answers) == set(correct_answers):
                score += 1
    return render(request, 'quiz.html', {
        'questions': page_obj.object_list,
        'quiz_type': 'HTML',
        'page_obj': page_obj,
        'score': score,
        'total_questions': total_questions
    })


def quiz_css_view(request):
    page_number = request.GET.get('page', 1)
    paginator = Paginator(CSS_QUESTIONS, 10)
    page_obj = paginator.get_page(page_number)
    score = None
    total_questions = len(page_obj.object_list)
    if request.method == 'POST':
        score = 0
        for idx, question in enumerate(page_obj.object_list, start=1):
            user_answers = request.POST.getlist(f'q{idx}')
            correct_answers = []
            if hasattr(question, 'answers'):
                correct_answers = [a[0] for a in question.answers if len(a) > 1 and a[1] is True]
            elif hasattr(question, 'choices') and hasattr(question, 'correct'):
                correct_answers = question.correct if isinstance(question.correct, list) else [question.correct]
            if set(user_answers) == set(correct_answers):
                score += 1
    return render(request, 'quiz.html', {
        'questions': page_obj.object_list,
        'quiz_type': 'CSS',
        'page_obj': page_obj,
        'score': score,
        'total_questions': total_questions
    })


def quiz_javascript_view(request):
    page_number = request.GET.get('page', 1)
    paginator = Paginator(JS_QUESTIONS, 10)
    page_obj = paginator.get_page(page_number)
    score = None
    total_questions = len(page_obj.object_list)
    if request.method == 'POST':
        score = 0
        for idx, question in enumerate(page_obj.object_list, start=1):
            user_answers = request.POST.getlist(f'q{idx}')
            correct_answers = []
            if hasattr(question, 'answers'):
                correct_answers = [a[0] for a in question.answers if len(a) > 1 and a[1] is True]
            elif hasattr(question, 'choices') and hasattr(question, 'correct'):
                correct_answers = question.correct if isinstance(question.correct, list) else [question.correct]
            if set(user_answers) == set(correct_answers):
                score += 1
    return render(request, 'quiz.html', {
        'questions': page_obj.object_list,
        'quiz_type': 'JavaScript',
        'page_obj': page_obj,
        'score': score,
        'total_questions': total_questions
    })


def quiz_python_view(request):
    page_number = request.GET.get('page', 1)
    paginator = Paginator(PYTHON_QUESTIONS, 10)
    page_obj = paginator.get_page(page_number)
    score = None
    total_questions = len(page_obj.object_list)
    if request.method == 'POST':
        score = 0
        for idx, question in enumerate(page_obj.object_list, start=1):
            user_answers = request.POST.getlist(f'q{idx}')
            correct_answers = []
            if hasattr(question, 'answers'):
                correct_answers = [a[0] for a in question.answers if len(a) > 1 and a[1] is True]
            elif hasattr(question, 'choices') and hasattr(question, 'correct'):
                correct_answers = question.correct if isinstance(question.correct, list) else [question.correct]
            if set(user_answers) == set(correct_answers):
                score += 1
    return render(request, 'quiz.html', {
        'questions': page_obj.object_list,
        'quiz_type': 'Python',
        'page_obj': page_obj,
        'score': score,
        'total_questions': total_questions
    })


def login_view(request):
    """
    Handle user login via AJAX POST request.
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')

            # Validate input
            if not username or not password:
                return JsonResponse({
                    'success': False,
                    'message': 'Username and password are required.'
                })

            # Authenticate user
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({
                    'success': True,
                    'message': f'Welcome back, {username}!'
                })
            else:
                return JsonResponse({
                    'success': False,
                    'message': 'Invalid username or password.'
                })

        except json.JSONDecodeError:
            return JsonResponse({
                'success': False,
                'message': 'Invalid data format.'
            })

    return JsonResponse({
        'success': False,
        'message': 'Invalid request method.'
    })


def logout_view(request):
    """
    Handle user logout.
    """
    logout(request)
    return redirect('home')
