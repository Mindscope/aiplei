from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


class BetaInviteRequest(models.Model):
    email = models.EmailField(_(u'email'), unique=True)

    def __unicode__(self):
        return u'%s' % self.email

    class Meta:
        verbose_name = _(u'Invitation request')
        verbose_name_plural = _(u'Invitation requests')


@receiver(post_save, sender=User)
def delete_beta_request(sender, **kwargs):
    if kwargs['created']:
        user = kwargs['instance']
        try:
            beta_request = BetaInviteRequest.objects.get(email=user.email)
            beta_request.delete()
        except BetaInviteRequest.DoesNotExist:
            pass
