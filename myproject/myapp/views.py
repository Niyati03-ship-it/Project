from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from transformers import pipeline
from django.contrib.auth.models import User
pipeline("summarization")


summarizer = None
original_count = 0
summary_count = 0

def user_signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            return render(request, 'signup.html', {'error': 'Passwords do not match'})

        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Username already exists'})

        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('home')

    return render(request, 'signup.html')


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')

@login_required
def home(request):
    global summarizer

    summary = ""
    original_count = 0   
    summary_count = 0    

    if summarizer is None:
        summarizer = pipeline(
            "summarization",
            model="sshleifer/distilbart-cnn-12-6"
        )

    if request.method == "POST":
        text = request.POST.get('text', '')

        if text.strip():
            original_count = len(text.split())

            result = summarizer(
                text,
                max_length=len(text.split()) - 20,
                min_length=len(text.split()) // 2,
                do_sample=False
)

            summary = result[0]['summary_text']
            summary_count = len(summary.split())

    return render(request, 'home.html', {
        'summary': summary,
        'original_count': original_count,
        'summary_count': summary_count
    })

def user_logout(request):
    logout(request)
    return redirect('login')


