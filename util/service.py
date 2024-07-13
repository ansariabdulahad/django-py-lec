from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

def SendMail(fullname, email, subject, message, recipients) :
    try :
        data = {
            'name' : fullname,
            'email' : email,
            'message' : message
        }
        html = render_to_string('email_template.html', data)
        send_mail(
            subject=subject,
            message=None,
            html_message=html,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=recipients
        )
        return {
            'success' : True
        }
    except Exception as exe :
        return {
            'success' : False,
            'error' : exe
        }