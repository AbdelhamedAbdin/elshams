from django.shortcuts import render, redirect
from django.views import View
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template import Context
from django.template.loader import get_template
from .forms import ContactForm
from django.contrib import messages


class ContactUs(View):
    forms = ContactForm

    def get(self, request):
        return render(request, 'contact-us/contact.html', {'forms': self.forms(None)})

    def post(self, request):
        forms = self.forms(request.POST)

        if forms.is_valid():

            template = get_template('contact-us/contact-format.html')
            context = Context({
                'name': forms.cleaned_data['name'],
                'phone': forms.cleaned_data['phone'],
                'message': forms.cleaned_data['message'],
                'email': forms.cleaned_data['email']
            })

            content = template.render(context.dicts[1])

            msg = EmailMultiAlternatives(
                subject=forms.cleaned_data['subject'],
                from_email=forms.cleaned_data['email'],
                to=[settings.DEFAULT_FROM_EMAIL]
                 )
            msg.attach_alternative(content, "text/html")
            msg.send()
            messages.success(request, "لقد تم ارسال الرسالة بنجاح.يرجى متابعة بريدكم الالكترونى باستمرار لمتابعة الرد.",
                             extra_tags="send_contact")
            return redirect('contact:contact-us')
        else:
            return render(request, 'contact-us/contact.html', {'forms': forms})
