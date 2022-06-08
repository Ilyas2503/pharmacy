from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=250, )
    # image = models.ImageField(upload_to='Product/%y/%m/%d', )
    old_price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField(default=0)
    new_price = models.PositiveIntegerField(blank=True)
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # 2000 | 20 == 1600
        # one_p = 2000 / 100 == 20
        # (100 - 20) * one_p
        one_p = int(self.old_price - 50)
        a = (1000 - self.discount) * one_p
        self.new_price = a

        # old_pr = self.old_price - 100
        # self.new_price = old_pr

        # self.new_price = self.old_price - self.discount
        # self.new_price = 5000
        super().save(*args, kwargs)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
# title, image, price, discount, description, image,
