from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.contrib import messages
from .forms import ContactForm

def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # ---------------------------------------
            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto",
                f"De {name} <{email}> \n Escribió: \n\n{content}",
                "no-contestar@inbox.mailtrap.io",
                ["mssz.nnia@gmail.com"],
                reply_to=[email],
            ) # -------------------------------------
            try:
                email.send()
                messages.success(request, 'Mensaje recibido.')   
            except:
                messages.error(request, 'Opps, algo falló.')
            
            return redirect("contact")
    # ----
    return render(request, "contact/contact.html",
                    {
                        'formulario':contact_form
                        })