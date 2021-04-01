from django import forms


class PalindromeForm(forms.Form):
    palindrome = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Palindrome'}))
