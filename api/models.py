from django.db import models
from ckeditor.fields import RichTextField
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from PIL import Image
from django.utils import timezone
from datetime import datetime

# Helper function to resize and optimize images
def optimize_image(image_field, new_height):
    # Open the uploaded image using Pillow
    image = Image.open(image_field)

    # Calculate the new width while maintaining the aspect ratio
    width, height = image.size
    new_width = int((new_height / height) * width)

    # Resize the image to the calculated dimensions
    new_size = (new_width, new_height)
    image = image.resize(new_size)

    # Convert the image to WebP format
    image = image.convert("RGB")
    output_buffer = BytesIO()
    image.save(output_buffer, format="WEBP", quality=80, method=6)

    # Prepare a BytesIO object to store the optimized image
    output_buffer.seek(0)

    # Update the uploaded image field with the optimized image
    optimized_image = InMemoryUploadedFile(
        output_buffer,
        "ImageField",  # Field name
        f"{image_field.name.split('.')[0]}.webp",  # File name
        "image/webp",  # Content type
        output_buffer.tell(),  # Size
        None,  # Content type extra arguments
        None,  # Charset
    )

    return optimized_image


# Services
class Services(models.Model):
    s_name = models.CharField(max_length=400)
    s_pic = models.ImageField(upload_to="media/serviceimage", null=True)
    s_rank = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    s_desc = RichTextField()

    def __str__(self):
        return self.s_name

    def save(self, *args, **kwargs):
        if self.s_pic and not self.pk:
            self.s_pic = optimize_image(self.s_pic, 350)

        super().save(*args, **kwargs)


# Testimonials
class Testimonials(models.Model):
    client_name = models.CharField(max_length=400)
    client_pos = models.CharField(max_length=200, null=True, blank=True)
    client_pic = models.ImageField(upload_to="media/testimonialsimage", null=True)
    client_desc = RichTextField()

    def __str__(self):
        return self.client_name

    def save(self, *args, **kwargs):
        if self.client_pic and not self.pk:
            self.client_pic = optimize_image(self.client_pic, 200)

        super().save(*args, **kwargs)


# Team
class Team(models.Model):
    staff_name = models.CharField(max_length=400)
    staff_pos = models.CharField(max_length=200, null=True)
    staff_rank = models.IntegerField(default=0)
    is_md = models.BooleanField(default=False)
    staff_pic = models.ImageField(upload_to="media/teamimage", null=True)
    staff_desc = RichTextField()
    gmail = models.EmailField(null=True, blank=True)
    linkedin = models.URLField(max_length=200, null=True, blank=True)
    twitter = models.URLField(max_length=200, null=True, blank=True)
    facebook = models.URLField(max_length=200, null=True, blank=True)
    instagram = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.staff_name

    def save(self, *args, **kwargs):
        if self.staff_pic and not self.pk:
            self.staff_pic = optimize_image(self.staff_pic, 350)

        super().save(*args, **kwargs)


# Project
class Project(models.Model):
    p_name = models.CharField(max_length=400)
    p_type = models.CharField(max_length=200, null=True)
    is_active = models.BooleanField(default=True)
    p_rank = models.IntegerField(default=0)
    p_pic = models.ImageField(upload_to="media/projectimage")
    tags = models.CharField(max_length=50,  help_text="Comma-separated tags", null=True)
    timestamp = models.DateTimeField(default=timezone.now)
    p_desc = RichTextField()
    p_point1 = models.CharField(max_length=200)  
    p_point2 = models.CharField(max_length=200)  
    p_point3 = models.CharField(max_length=200, null=True, blank=True) 

    def __str__(self):
        return self.p_name

    def save(self, *args, **kwargs):
        if self.p_pic and not self.pk:
            self.p_pic = optimize_image(self.p_pic, 500)

        super().save(*args, **kwargs)

# Course
class Course(models.Model):
    c_name = models.CharField(max_length=400)
    c_rank = models.IntegerField(default=0)
    c_tags = models.CharField(max_length=120,  help_text="Comma-separated tags", null=True)
    c_pic = models.ImageField(upload_to="media/courseimage")
    c_desc = RichTextField(null=True)
    c_overview = RichTextField(null=True)
   
    

    def __str__(self):
        return self.c_name

    def save(self, *args, **kwargs):
        if self.c_pic and not self.pk:
            self.c_pic = optimize_image(self.c_pic, 350)

        super().save(*args, **kwargs)

# Blog
class Blog(models.Model):
    b_name = models.CharField(max_length=400)
    b_type = models.CharField(max_length=200, null=True)
    b_rank = models.IntegerField(default=0)
    b_pic = models.ImageField(upload_to="media/blogimage", null=True)
    b_desc = RichTextField()
    short_desc = models.CharField(max_length=160, null=True)
    tags = models.CharField(max_length=50,  help_text="Comma-separated tags", null=True)
    timestamp = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return self.b_name

    def formatted_date(self):
        return self.timestamp.strftime("%B %d, %Y")

    def save(self, *args, **kwargs):
        if self.b_pic and not self.pk:
            self.b_pic = optimize_image(self.b_pic, 500)

        super().save(*args, **kwargs)

    def get_tags(self):
        if self.tags:
            return self.tags.split(",")
        else:
            return []



# Email contact from users

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    query_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
