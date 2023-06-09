from django.db import models

class Application(models.Model):
    name = models.CharField("ФИО",max_length=50)
    email = models.EmailField("Email")
    phone_number = models.CharField("Номер телефона",max_length=30)
    Comment = models.TextField(null=True)
    is_checked = models.BooleanField("Просмотрено",default=False)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
