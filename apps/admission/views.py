from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import AdmissionForm
from django.contrib import messages
from .utils import admission_notification


class AdmissionView(View):

    def get(self, request):
        forms = AdmissionForm(request.GET or None)
        return render(request, 'addmissions/admission.html', {'forms': forms})

    def post(self, request):
        forms = AdmissionForm(request.POST)
        submit_term = request.POST.get("admission-terms") or None

        if submit_term == "on":
            if not forms.is_valid():
                return render(request, 'addmissions/admission.html', {'forms': forms})
            else:
                forms.save()
                sender_email = forms.cleaned_data.get("email")
                messages.success(request, "لقد تم ارسال طلبكم بنجاح سيتم الرد عليكم فى اقرب وقت ممكن", extra_tags="success_join")
                admission_notification(sender_email)
                return redirect('admission:admission')
        return render(request, 'addmissions/admission.html', {'forms': forms})
