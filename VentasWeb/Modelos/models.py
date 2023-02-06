from django.db import models
from django.conf import settings
from django.forms import model_to_dict

from crum import get_current_user

from VentasWeb.choices import sexo


##############################################################################

class Category(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_create_category")
    user_update = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                    related_name='user_update_category', null=True, blank=True)
    date_create = models.DateField(auto_now_add=True, null=True, blank=True)
    date_update = models.DateField(auto_now=True, null=True, blank=True)

    name = models.CharField(max_length=100, verbose_name="Nombre", unique=True)

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["id"]

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.usuario = user
            else:
                self.user_update = user
        super(Category, self).save()

class Product(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_create_product")
    user_update = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                    related_name='user_update_product', null=True, blank=True)
    date_create = models.DateField(auto_now_add=True, null=True, blank=True)
    date_update = models.DateField(auto_now=True, null=True, blank=True)

    name = models.CharField(max_length=100, verbose_name="Nombre", unique=True)
    code = models.CharField(max_length=20,verbose_name="Codigo", unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product/%Y/%m/%d", null=True, blank=True)
    precio_venta_publico = models.DecimalField(default=0.00, max_digits=9,decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["id"]

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.usuario = user
            else:
                self.user_update = user
        super(Product, self).save()

class Client(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_create_client")
    user_update = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                    related_name='user_update_client', null=True, blank=True)
    date_create = models.DateField(auto_now_add=True, null=True, blank=True)
    date_update = models.DateField(auto_now=True, null=True, blank=True)

    name = models.CharField(max_length=50, verbose_name="Nombre")
    surname = models.CharField(max_length=50, verbose_name="Apellido")
    dni = models.PositiveIntegerField(unique=True, verbose_name="Dni")
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name="Direccion")
    gender = models.CharField(max_length=10, choices=sexo, verbose_name="Sexo")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ["id"]

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.usuario = user
            else:
                self.user_update = user
        super(Client, self).save()

class Sale(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_create_sale")
    user_update = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                    related_name='user_update_sale', null=True, blank=True)
    date_create = models.DateField(auto_now_add=True, null=True, blank=True)
    date_update = models.DateField(auto_now=True, null=True, blank=True)

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)


    def __str__(self):
        return self.client.name

    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"
        ordering = ["id"]

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.usuario = user
            else:
                self.user_update = user
        super(Sale, self).save()

class DetSale(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_create_detsale")
    user_update = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                    related_name='user_update_detsale', null=True, blank=True)
    date_create = models.DateField(auto_now_add=True, null=True, blank=True)
    date_update = models.DateField(auto_now=True, null=True, blank=True)

    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cant = models.IntegerField(default=0)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.prod.name

    class Meta:
        verbose_name = "Detalle Venta"
        verbose_name_plural = "Detalle Ventas"
        ordering = ["id"]

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.usuario = user
            else:
                self.user_update = user
        super(DetSale, self).save()
