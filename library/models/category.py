from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='Category Name')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'categories'
        permissions = [
            ("can_get_statistic", "Can get genres statistic"),
        ]
