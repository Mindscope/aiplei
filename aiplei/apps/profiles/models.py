from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


USER_STATUS_CHOICES = ((0, _(u'Registered')),
                       (1, _(u'Limited Access')),
                       (2, _(u'Beta Tester')),
                       (3, _(u'Unlimited Access')),
                       )


class Profile(models.Model):
    user = models.OneToOneField(User)
    access = models.IntegerField(_(u'user access'), default=0)


@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
    if kwargs['created']:
        user = kwargs['instance']
        p = Profile(user=user)
        p.save()


@receiver(pre_delete, sender=User)
def delete_profile(sender, **kwargs):
    user = kwargs['instance']
    try:
        p = Profile.objects.get(user=user)
        p.delete()
    except:
        pass
