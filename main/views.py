from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import boto3

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

@login_required
def home_view(request):
    s3 = boto3.client('s3')
    buckets = s3.list_buckets()
    return render(request, 'home.html', {'buckets': buckets.get('Buckets', [])})

