from django.db.models import Model ,EmailField , DateTimeField

class Subscriber(Model):
    email = EmailField(unique=True)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
