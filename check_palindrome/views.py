from django.shortcuts import render

# Create your views here.


def check_palindrome_or_not(request):
    return render(request, 'index.html')
