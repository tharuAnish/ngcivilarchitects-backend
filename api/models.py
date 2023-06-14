from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.base import Model
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from PIL import Image
# Create your models here.


class Services(models.Model):
    s_name=models.CharField(max_length=400)
    s_desc=RichTextField()
    s_pic = models.ImageField(upload_to='media/serviceimage', null=True)
    is_active=models.BooleanField(default=True)
    s_rank=models.IntegerField(default=0)
    def __str__(self):
        return self.s_name
    

class Testimonials(models.Model):
    client_name=models.CharField(max_length=400)
    client_desc=RichTextField()
    client_pic = models.ImageField(upload_to='media/serviceimage', null=True)
    is_active=models.BooleanField(default=True)
    client_rank=models.IntegerField(default=0)
    def __str__(self):
        return self.client_name
    
    # To resize image

    def save(self, *args, **kwargs):
        if self.client_pic:
            self.client_pic = self.Testimonials(self.client_pic)

        super().save(*args, **kwargs)

    @staticmethod
    def Testimonials(image_field):
        # Open the uploaded image using Pillow
        image = Image.open(image_field)

        # Calculate the new width while maintaining the aspect ratio
        new_height = 200
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
            'ImageField',  # Field name
            f"{image_field.name.split('.')[0]}.webp",  # File name
            'image/webp',  # Content type
            output_buffer.tell(),  # Size
            None,  # Content type extra arguments
            None,  # Charset
        )
        return optimized_image
