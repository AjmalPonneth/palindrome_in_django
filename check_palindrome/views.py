from django.shortcuts import render
from .forms import PalindromeForm
# Create your views here.


def check_palindrome_or_not(request):
    # form = PalindromeForm(request.POST)
    # check = request.POST.get('palindrome')
    # IsPalindrome = check.find(check[::-1]) == 0
    # context = {
    #     'form': form,
    #     'palindrome': IsPalindrome
    # }
    return render(request, 'index.html')
