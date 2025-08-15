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

    return JsonResponse({
        'success': False,
        'message': 'Invalid request method.'
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
