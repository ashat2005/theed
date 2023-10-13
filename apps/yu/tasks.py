from youtube_dl import YoutubeDL
from django.core.mail import EmailMessage
from django.conf import settings
from celery import shared_task
from .models import Mail

@shared_task()
def send_feedback_email_task(video_url, email):
    try:
        video_info = YoutubeDL().extract_info(url=video_url, download=False)

        filename = f"{video_info['title']}.mp3"
        options = {
            'format': 'bestaudio/best',  
            'keepvideo': False,  
            'outtmpl': f'media/{filename}',  
        }

        with YoutubeDL(options) as ydl:
            ydl.download([video_url])

        mail = EmailMessage(
            "Ваш файл готов.",
            "Это уведомление отправлено, потому что вы указали свой адрес электронной почты на нашем веб-сайте.",
            settings.EMAIL_HOST_USER,  
            [email] 
        )

        mail.attach_file(f'media/{filename}')
        mail.send()

        try:
            conversion_request = Mail.objects.get(video_url=video_url, email=email)
            conversion_request.converted_mp3_url = f'media/{filename}'
            conversion_request.is_completed = True
            conversion_request.save()
        except Mail.DoesNotExist:
            pass

    except Exception as e:
        print(f"Error in send_feedback_email_task: {e}")
