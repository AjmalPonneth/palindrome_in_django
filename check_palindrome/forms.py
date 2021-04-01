from django import forms


class PalindromeForm(forms.Form):
    palindrome = forms.CharField(label='Palindrome', max_length=100)
