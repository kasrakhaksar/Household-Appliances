from django.db.models import Model , CharField ,SlugField , ForeignKey , CASCADE , TextField , ImageField ,SET_NULL , DateTimeField , ManyToManyField , Index
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse


class Category(Model):
    name = CharField(max_length=100, unique=True)
    slug = SlugField(max_length=120, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("blogs:category_detail", args=[self.slug])


class Tag(Model):
    name = CharField(max_length=30, unique=True)
    slug = SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Blog(Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = CharField(max_length=250)
    slug = SlugField(max_length=250, unique=True)
    author = ForeignKey(User, on_delete=CASCADE, related_name='blog_posts')
    content = TextField()
    excerpt = TextField(max_length=300, blank=True)
    image = ImageField(upload_to='blogs/', blank=True, null=True)
    category = ForeignKey(Category, on_delete=SET_NULL, null=True, related_name='posts')
    tags = ManyToManyField(Tag, related_name='posts', blank=True)
    status = CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    published = DateTimeField(blank=True, null=True)

    seo_title = CharField(max_length=70, blank=True)
    seo_description = CharField(max_length=160, blank=True)

    class Meta:
        ordering = ['-published']
        indexes = [
            Index(fields=['-published']),
        ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blogs:post_detail", args=[self.slug])
