from django.db import models
from twilio.rest import Client
from dotenv import load_dotenv
import os

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)
    load_dotenv()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        client = Client(account_sid, auth_token)
        
        if self.score >= 70:

            message = client.messages.create(
                body=f"congratulations {self.name}, you PASSED with the score of {self.score}",
                from_=os.getenv('TWILIO_PHONE_NUMBER'),
                to="+639121769168",
            )
        else:

            message = client.messages.create(
                body=f"Sorry {self.name}, you FAILED with the score of {self.score}",
                from_="+17754380602",
                to="+639121769168",
            )

        print(message.body)
        return super().save(*args, **kwargs)