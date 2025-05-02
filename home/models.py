from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
from django.forms import ModelForm, TextInput, Textarea
from django.http import request
from django.utils.safestring import mark_safe


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
        verbose_name_plural='9. Header'

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
     

class ContactMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
        ('follow up', 'follow up'),
    )
    name= models.CharField(blank=False,max_length=20)
    mobile= models.CharField(blank=False,max_length=20)
    email= models.EmailField(blank=False,max_length=50)
    subject= models.CharField(blank=False,max_length=50)
    message= models.TextField(blank=False,max_length=255)
    status=models.CharField(max_length=10,choices=STATUS,default='New')
    ip = models.CharField(blank=True, max_length=20)
    note = models.CharField(blank=True, max_length=100)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural='1. Responce'

class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject','message']
        widgets = {
            'name'   : TextInput (attrs={'class': 'input','placeholder':'Name & Surname',} ),
            'subject' : TextInput(attrs={'class': 'input','placeholder':'Subject'}),
            'email'   : TextInput(attrs={'class': 'input','placeholder':'Email Address'}),
            'message' : Textarea(attrs={'class': 'input','placeholder':'Your Message','rows':'5'}),
        }



class Bookingopen(models.Model):
    project_name = models.CharField(max_length=150,)
    at = models.CharField(max_length=255,)
    by = models.CharField(max_length=255,)
    landp_arcel = models.CharField(max_length=255,)
    possession = models.CharField(max_length=255,)
    spot_booking_offers = models.CharField(max_length=255,)
    early_buy_discounts = models.CharField(max_length=255,)
    flexipay_for_first = models.CharField(max_length=255,)
    luxurious = models.CharField(max_length=255,)
    priceing = models.CharField(max_length=255,)
    
    
    def __str__(self):
        return self.project_name    
        
    class Meta:
        verbose_name_plural='10. project_name'


class Welcometo(models.Model):
    title = models.CharField(max_length=150)
    details= models.TextField(blank=False,max_length=5500)
    readmore= models.TextField(blank=False,max_length=5500)
    
    def __str__(self):
        return self.title    
        
    class Meta:
        verbose_name_plural='11. Welcome To'


class Location(models.Model):
    title = models.CharField(max_length=150)    
    
    def __str__(self):
        return self.title    
        
    class Meta:
        verbose_name_plural='12. Location'



class Maharera(models.Model):
    qr_image = models.ImageField(upload_to='overviewimage/')
    title = models.CharField(max_length=150)
    maharera_no= models.CharField(blank=True,max_length=50)
    details= models.CharField(blank=True,max_length=500)
    
    def __str__(self):
        return self.title    
        
    class Meta:
        verbose_name_plural='13. Maharera'
