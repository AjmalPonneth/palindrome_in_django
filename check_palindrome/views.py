from django.shortcuts import render
from .forms import PalindromeForm
# Create your views here.


def check_palindrome_or_not(request):
    form = PalindromeForm(request.POST)
    check = request.POST.get('palindrome')
    string = str(check)
    IsPalindrome = string.find(string[::-1]) == 0
    return render(request, 'index.html', {'form': form, 'palindrome': IsPalindrome})
