from django.core.mail import send_mail
from django.conf import settings

def SendMail(subject, message, recipients) :
    try :
        send_mail(
            subject=subject,
            message=message,
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