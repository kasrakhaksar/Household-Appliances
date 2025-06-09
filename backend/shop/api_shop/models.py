from django.db.models import Model , Index , CharField , TextField , DecimalField , PositiveIntegerField , BooleanField , ImageField , DateTimeField




class Product(Model):
    CATEGORY_CHOICES = [
        ('kitchen', 'Kitchen Appliances'),
        ('cleaning', 'Cleaning Appliances'),
        ('entertainment', 'Entertainment Devices'),
        ('climate', 'Heating/Cooling'),
        ('other', 'Other'),
    ]

    name = CharField(max_length=100, verbose_name="Product Name")
    description = TextField(null=True, blank=True, verbose_name="Description")
    price = DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")
    discount_price = DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Discount Price")
    stock = PositiveIntegerField(default=0, verbose_name="Stock Quantity")
    brand = CharField(max_length=100, null=True, blank=True, verbose_name="Brand")
    category = CharField(max_length=50, choices=CATEGORY_CHOICES, verbose_name="Category")
    is_active = BooleanField(default=True, verbose_name="Is Active")
    image = ImageField(upload_to='product_images/', null=True, blank=True, verbose_name="Product Image")
    created_at = DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = DateTimeField(auto_now=True, verbose_name="Updated At")


    def __str__(self):
        return f"{self.name} - {self.brand or 'No Brand'}"


    class Meta:
            ordering = ['-created_at']
            indexes = [
                Index(fields=['category'])
            ]
            verbose_name = "Product"
            verbose_name_plural = "Products"