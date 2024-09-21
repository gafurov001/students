from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from apps.tasks import send_to_email
from apps.utils.tokens import account_activation_token
from root.settings import EMAIL_HOST_USER


def generate_one_time_verification(request, user):
    current_site = get_current_site(request)
    email = user.email
    subject = "Verify Email"
    message = render_to_string('apps/register/verify_email_message.html', {
        'scheme': request.scheme,
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
    })
    # send_mail(subject, message, EMAIL_HOST_USER, [email], html_message=message)
    send_to_email.delay(subject, message, email)
