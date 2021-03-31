from django.urls import path
from .views import check_palindrome_or_not
urlpatterns = [
    path('', check_palindrome_or_not)
]
