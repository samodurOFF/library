from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils import timezone
from rest_framework.authtoken.models import Token


from .models import Book



@receiver(post_save, sender=Book)
def book_saved(sender, instance, created, **kwargs):
    if created:
        print(f'New book created: {instance.title}')
    else:
        print(f'Book updated: {instance.title}')


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

@receiver(pre_save, sender=Book)
def update_timestamp(sender, instance, **kwargs):
    instance.updated_at = timezone.now()

@receiver(post_save, sender=Book)
def notify_admin_on_new_order(sender, instance, created, **kwargs):
    if created:
        send_mail(
            'New Book Created',
            f'Book {instance.id} has been created.',
            'admin@gmail.com',
            ['admin@gmail.com'],
        )