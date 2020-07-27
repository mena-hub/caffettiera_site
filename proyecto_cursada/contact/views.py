from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

def contact(request):
    contact_form = ContactForm()
    # ----------------------------
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # -----------------------------------------               
            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto",
                "De {} <{}> \n Escribió: \n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["mssz.nnia@gmail.com"],
                reply_to=[email],
            ) # -------------------------------------
        try:
            email.send()
            return redirect("respuesta/"+'?ok')
            # return redirect(reverse("contact")+'?ok')
        except:
            return redirect("respuesta/"+'?fail')
    return render(request, "contact/contact.html",
                    {
                        'formulario':contact_form
                        })

def respuesta(request):
    return render(request, "contact/respuesta.html")