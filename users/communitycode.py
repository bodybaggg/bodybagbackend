
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import User
from django.db.models.signals import post_save


@receiver(pre_save, sender=User)
def generate_unique_code(sender, instance, **kwargs):
    if not instance.unique_code:
        # Generate a unique code 
        instance.unique_code = f"h{User.objects.latest('id').id}"


@receiver(post_save, sender=User)
def post_save_generate_unique_code(sender, instance, created, **kwargs):
    if created:
        # Access the unique_code attribute and return it in the post-response
        generated_unique_code = instance.unique_code
        
        # print(f"Generated Unique Code: {generated_unique_code}")
