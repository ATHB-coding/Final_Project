from django.http import HttpResponse
from django.shortcuts import render

from .forms import ContactForm


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "content": "Bem-vindo a página de contato",
        "form": contact_form
    }

    if contact_form.is_valid():
        print(contact_form.cleaned_data)
        return

    return render(request, "contact/view.html", context)
