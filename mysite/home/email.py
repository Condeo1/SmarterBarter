from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from home.models import *
from secret_settings import *

@csrf_protect
def contact(request):
    form = ContactMessage(request.POST or None)
    if form.is_valid():
        form_message = form.cleaned_data.get("emailMessage")
        subject = 'Site Contact form'
        from_email = secret_settings.EMAIL_HOST_USER
        to_email = secret_settings.EMAIL_HOST_USER
        contact_message = "%s: %s via %s"(
            "SmarterBarter",
            form_message,
            form_email)
        send_mail(subject,
                 contact_message,
                 from_email,
                 to_email,
                 fail_silently = False)
    context = {
        "form": form,
    }    
    return render(request, "contact.html", context)