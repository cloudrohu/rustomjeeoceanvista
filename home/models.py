from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(max_length=150,)
    keywords = models.CharField(max_length=255,)
    description = models.CharField(max_length=255,)
    configuration_bg = models.ImageField(upload_to='logo/')
    logo = models.ImageField(upload_to='logo/',)
    logo_2 = models.ImageField(upload_to='logo/')
    icon = models.ImageField(upload_to='images/',)
    color = models.CharField(max_length=150)
    cuntact_no = models.CharField(max_length=150,)
    location = models.CharField(max_length=1150,)
    site_address= models.CharField(max_length=1150,blank=True,null=True)
    googletagmanager= models.CharField(max_length=1150,blank=True,null=True)
    
    def __str__(self):
        return self.title    
        
    class Meta:
        verbose_name_plural='1. Header'

class Web_Slider(models.Model):
    web_image = models.ImageField(upload_to='sliderimage/')
    mobile_image = models.ImageField(upload_to='sliderimage/')
    title = models.CharField(max_length=150)
    
    def __str__(self):
        return self.title    
        
    class Meta:
        verbose_name_plural='2. Web Slider'

class Overview(models.Model):
    web_image = models.ImageField(upload_to='overviewimage/')
    mobile_image = models.ImageField(upload_to='overview/')
    title = models.CharField(max_length=150)
    details= models.TextField(blank=False,max_length=5500)
    
    def __str__(self):
        return self.title    
        
    class Meta:
        verbose_name_plural='3. Overview'

class About_Us(models.Model):
    web_image = models.ImageField(upload_to='aboutimage/')
    mobile_image = models.ImageField(upload_to='aboutimage/')
    title = models.CharField(max_length=150)
    details= models.TextField(blank=False,max_length=5500)
    
    def __str__(self):
        return self.title    
        
    class Meta:
        verbose_name_plural='4. About_Us'

class Unique_Selling_Proposition(models.Model):
    icone = models.ImageField(upload_to='uspimage/')
    title = models.CharField(max_length=150)
    icone2 = models.ImageField(upload_to='uspimage/',blank=True,null=True)
    title2 = models.CharField(max_length=150,blank=True,null=True)
    
    def __str__(self):
        return self.title    
        
    class Meta:
        verbose_name_plural='5. Unique Selling Proposition'

class Configuration(models.Model):
    typology = models.CharField(max_length=150)
    rera_carpet_area = models.CharField(max_length=150)
    price = models.CharField(max_length=150)
    
    def __str__(self):
        return self.typology    
        
    class Meta:
        verbose_name_plural='6. Configuration'

class Amenities(models.Model):
    icone = models.ImageField(upload_to='amenitiesimage/')
    title = models.CharField(max_length=150)
    icone2 = models.ImageField(upload_to='uspimage/',blank=True,null=True)
    title2 = models.CharField(max_length=150,blank=True,null=True)
    
    def __str__(self):
        return self.title    
        
    class Meta:
        verbose_name_plural='7. Amenities'

class Gallery(models.Model):

    SECTION = (
        ('Views','Views'),
        ('Amenities','Amenities'),       
        ('Interiors','Interiors'),       
        ('Exterior','Exterior'),       
        ('Plans','Plans'),  
    )

    section = models.CharField(choices=SECTION,max_length=100)
    web_image = models.ImageField(upload_to='galleryimage/')
    mobile_image = models.ImageField(upload_to='galleryimage/')
    title = models.CharField(max_length=150)
    
    def __str__(self):
        return self.title    
        
    class Meta:
        verbose_name_plural='8. Gallery'


        



