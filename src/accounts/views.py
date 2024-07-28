from django.contrib import messages
from django.contrib.auth import (
    authenticate,
    login,
    logout,
)
from django.shortcuts import render, redirect

from .forms import (
    UserLoginForm, UserRegistrationForm,
    AccountDetailsForm, UserAddressForm,
)


# TODO: Create the register view.
# Upon successful registration, the user should be redirected home and a success message should be displayed.
# This success message should show the user their new account number, which they will need to login.
def register_view(request):
    

    # TODO: The template expects three forms: user_form, account_form, address_form.
    context = {
        "title": "Create a Bank Account",
        "user_form": None,
        "account_form": None,
        "address_form": None,
    }

    return render(request, "accounts/register_form.html", context)


# TODO: Create the login view.
# Upon successful login, the user should be redirected home and a success message should be displayed.
def login_view(request):

    # TODO: The template expects a form for the user login.
    context = {
        "form": None,
        "title": "Log In",
    }

    return render(request, "accounts/form.html", context)


# TODO: Create the logout view.
# Upon successful logout, the user should be redirected to the home page.
