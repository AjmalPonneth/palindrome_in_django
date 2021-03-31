from django.shortcuts import render
from .forms import PalindromeForm
# Create your views here.


def check_palindrome_or_not(request):
    form = PalindromeForm()
    palindrome = request.POST.get('palindrome')
    IsPalindrome = palindrome.find(palindrome[::-1]) == 0
    print(IsPalindrome)
    context = {
        'form': form,
        'palindrome': IsPalindrome}
    return render(request, 'index.html', context)
