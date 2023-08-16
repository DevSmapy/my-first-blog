from django.conf import settings
from django.db.models import Model,ForeignKey,CharField,TextField,DateTimeField,CASCADE
from django.utils.timezone import now

class Post(Model):
    author = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    title = CharField(max_length=200)
    text = TextField()
    create_date = DateTimeField(default=now)
    published_date = DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = now()
        self.save()

    def __str__(self):
        return self.title