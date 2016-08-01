import logging
from django.conf import settings
from django.contrib.auth.models import User
from .middlewares import ThreadLocal

logger = logging.getLogger(__name__)

IGNORE_IF_IP_STARTS_WITH = getattr(settings, 'D2B_IGNORE_IF_IP_STARTS_WITH',
                                   ['172', '127'])


class InvalidLoginBackend(object):
    def authenticate(self, username=None, password=None):
        request = ThreadLocal.get_current_request()
        if request:
            ip = request.META['REMOTE_ADDR']
            if ip.split('.')[0] in IGNORE_IF_IP_STARTS_WITH:
                return None
            msg = u'Failed password for user %s from %s' % (username, ip)
            logger.info(msg)

        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
