from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from .models import Subscriber

class SubscriberViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def create(self, request):
        email = request.data.get('email')
        if not email:
            return Response({'message': 'Email is required.'}, status=status.HTTP_400_BAD_REQUEST)

        subscriber, created = Subscriber.objects.get_or_create(email=email)

        if created:
            send_mail(
                subject="Welcome to Our Newsletter!",
                message="Thank you for subscribing to our newsletter!",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[subscriber.email],
                fail_silently=False,
            )
            return Response({'message': 'Subscribed successfully! A welcome email has been sent.'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'This email is already subscribed.'}, status=status.HTTP_200_OK)
