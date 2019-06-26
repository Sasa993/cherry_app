from django.core.mail import send_mail, BadHeaderError, EmailMultiAlternatives
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm


def email_main(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)

        if form.is_valid():
            cleaned_form = form.cleaned_data
            subject = f"Contact Us Question: {cleaned_form['subject']}"
            message = f"{cleaned_form['name']} has sent a message regarding Workflow Software.\nHis email is {cleaned_form['from_email']} and the messsage is:\n\n{cleaned_form['message']}"
            html_content = f"<strong>{cleaned_form['name']}</strong> has sent a message regarding our Workflow Software.<br>His email is <strong>{cleaned_form['from_email']}</strong> and the messsage is:<br><br><strong>{cleaned_form['message']}</strong>"
            from_email = f"{cleaned_form['from_email']}"
            try:
                msg = EmailMultiAlternatives(subject, message, from_email, ['cherryfinanceapp@gmail.com'])
                msg.attach_alternative(html_content, "text/html")
                msg.send()
            except BadHeaderError:
                return HttpResponse("Email hasn't been sent")
            return redirect('success/')
    return render(request, "email.html", {'form': form})


def email_success(request):
    return render(request, "email_success.html")
