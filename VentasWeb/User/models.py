from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from crum import get_current_request

#####################################################################################################


class Usuario(AbstractUser):
    image = models.ImageField(
        upload_to='users/%Y/%m/%d', null=True, blank=True)

    def get_image(self):
        if self.image:
            return "{}{}".format(settings.MEDIA_URL, self.image)
        return "{}{}".format(settings.STATIC_URL, "img/empty.png")

    def get_group_session(self):
        try:
            request = get_current_request()
            groups = self.groups.all()
            if groups.exists():
                if 'group' not in request.session:
                    request.session['group'] = groups[0]
        except:
            pass
