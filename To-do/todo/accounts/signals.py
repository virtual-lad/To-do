# ### signals.py file
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import send_mail

from django.contrib.auth.signals import user_logged_in



@receiver(post_save, sender=User)
def notify_author(sender, instance, created, ** kwargs) :
    if created:
        send_mail(
            "Sign up successful",
            "Welcome to the todo app.",
            "junaid123tariq123@gmail.com",
            [f"{instance.email}"],
            fail_silently=False,
        )

@receiver(user_logged_in)
def post_login(sender, user, request, **kwargs):
    subject = 'Login Alert'
    message = f"""
    Hey { user.username }!
    
    You just logged in to our todo app.
    Thank you for using our application. 
    
    Regards,
    Team todo app!
    """

    send_mail(
        subject,
        message,
        "junaid123tariq123@gmail.com",
        [user.email],
        fail_silently=False,
    )