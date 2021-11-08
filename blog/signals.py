from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from .models import Post

@receiver(post_delete, sender=Post) 
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(save=False)
    instance.audio.delete(save=False)

@receiver(pre_save, sender=Post) 
def updating_image_delete(sender, instance, **kwargs): 
    if instance.pk:
        try:
            old_image = Post.objects.get(pk=instance.pk).image
        except Post.DoesNotExist:
            return False
 
        else:
            new_image = instance.image
            if new_image:
                if old_image and old_image.url != new_image.url:
                    old_image.delete(save=False)
            else:
                old_image.delete(save=False)
    if not instance.pk:
        return False

@receiver(pre_save, sender=Post)
def updating_audio_delete(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_audio = Post.objects.get(pk=instance.pk).audio
        except Post.DoesNotExist:
            return False
        else:
            new_audio = instance.image
            if new_audio:
                if old_audio and old_audio.url != new_audio.url:
                    old_audio.delete(save=False)
            else:
                old_audio.delete(save=False)
    if not instance.pk:
        return False
