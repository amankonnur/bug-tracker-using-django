from django.core.mail import send_mail
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_email_view(email):
    subject = "You have been assigned a defect complete ASAP"
    message = "The given high priority defect need to complete"
    from_email = '4al20ai002@gmail.com'
    recipient_list = [email]

    # render html email from template
    html_message = render_to_string('task_email_template.html')

    #create plain text version by striping the html tags
    palin_message = strip_tags(html_message)

    try:
        send_mail(
            subject = subject,
            message=message,
            from_email=from_email,
            recipient_list=recipient_list,
            html_message=html_message,
            fail_silently=False
        )
        return HttpResponse("Email sent successfully!")
    except Exception as e:
        return HttpResponse(f"Error Sending Emial : {str(e)}")
        