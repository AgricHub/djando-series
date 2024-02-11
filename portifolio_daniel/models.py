from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

class CaseStudy(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='case_studies/')

class Testimonial(models.Model):
    author = models.CharField(max_length=100)
    content = models.TextField()
    
class ContactMessage(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

