from django.contrib.admin import site
from newsletter.models import Subscriber

site.register(Subscriber)
