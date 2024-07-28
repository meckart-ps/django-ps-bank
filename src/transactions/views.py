from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import DepositForm, WithdrawalForm


# TODO: Create the deposit view.
# Deposits should inaccessible if users are not logged in.
# Successful deposits should redirect to the home page and a success message should be displayed.
def deposit_view(request):

    # TODO: The template expects a form for the deposit.
    context = {
        "title": "Deposit",
        "form": None
    }
    return render(request, "transactions/form.html", context)


# TODO: Create the withdrawal view.
# Withdrawals should inaccessible if users are not logged in.
# Successful withdrawals should redirect to the home page and a success message should be displayed.
def withdrawal_view(request):

    # TODO: The template expects a form for the withdrawal.
    context = {
        "title": "Withdraw",
        "form": None
    }
    return render(request, "transactions/form.html", context)
