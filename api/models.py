from django.db import models
from ckeditor.fields import RichTextField
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from PIL import Image

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
        if self.s_pic:
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
        if self.client_pic:
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
        if self.staff_pic:
            self.staff_pic = optimize_image(self.staff_pic, 350)

        super().save(*args, **kwargs)


# Project
class Project(models.Model):
    p_name = models.CharField(max_length=400)
    p_type = models.CharField(max_length=200, null=True)
    is_active = models.BooleanField(default=True)
    p_rank = models.IntegerField(default=0)
    p_pic = models.ImageField(upload_to="media/projectimage", null=True)
    p_desc = RichTextField()
    p_point1 = models.CharField(max_length=200)  
    p_point2 = models.CharField(max_length=200)  
    p_point3 = models.CharField(max_length=200, null=True, blank=True) 

    def __str__(self):
        return self.p_name

    def save(self, *args, **kwargs):
        if self.p_pic:
            self.p_pic = optimize_image(self.p_pic, 350)

        super().save(*args, **kwargs)
