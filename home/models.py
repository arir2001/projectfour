from django.db import models

# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"), (2, "Archived"))
SERVICE = ((0, "One-shot Personal Reset"), (1, "3-month Life Coaching plan"), (2, "Business Consultancy"), (3, "Tailored Plan"))

class Testimonial(models.Model):
    name = models.CharField(max_length=100, unique=True, default='Anna')
    age = models.IntegerField(default =30)
    extra_detail = models.CharField(max_length=100, default='Job Title Here')

    testimonial = models.TextField(blank=True, max_length=140)

    service = models.IntegerField(choices=SERVICE, default=0)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return f"{self.name} - {self.service}" 


#new code- about = inquire
class Inquire(models.Model):
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    def __str__(self):
        return self.title
        return self.updated_on
        return self.content


class Service(models.Model):
    name = models.CharField(max_length=200, unique=True)
    def __str__(self):
        return self.name


class CollaborateRequest(models.Model):
    name = models.CharField(max_length=200)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, default=1)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"
        