from django.contrib import admin

from .models import *

# Register your models here. 1
class SettingAdmin(admin.ModelAdmin):
    list_display = ['id','logo','logo_2', 'color']
admin.site.register(Setting,SettingAdmin)


# Register your models here. 2

class Web_SliderAdmin(admin.ModelAdmin):
    list_display = ['id','web_image','mobile_image', 'title']
admin.site.register(Web_Slider,Web_SliderAdmin)


# Register your models here. 3
class OverviewAdmin(admin.ModelAdmin):
    list_display = ['id','web_image','mobile_image', 'title','details']
admin.site.register(Overview,OverviewAdmin)



# Register your models here. 4
class About_UsAdmin(admin.ModelAdmin):
    list_display = ['id','web_image','mobile_image', 'title','details']
admin.site.register(About_Us, About_UsAdmin)


# Register your models here. 5
class Unique_Selling_PropositionAdmin(admin.ModelAdmin):
    list_display = ['id','icone','title',]
admin.site.register(Unique_Selling_Proposition,Unique_Selling_PropositionAdmin)


# Register your models here. 6
class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ['id','typology','rera_carpet_area','price']
admin.site.register(Configuration, ConfigurationAdmin)


# Register your models here. 7
class AmenitiesAdmin(admin.ModelAdmin):
    list_display = ['id','icone','title',]
admin.site.register(Amenities, AmenitiesAdmin)


# Register your models here. 8
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['id','web_image','mobile_image', 'section', 'title']
admin.site.register(Gallery, GalleryAdmin)



class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['id','name','mobile', 'subject', 'update_at','status','note','message','email','ip',]
    list_editable = ['status','note']
    readonly_fields =['ip']
    list_filter = ['status']


admin.site.register(ContactMessage,ContactMessageAdmin)


# Register your models here. 8
class BookingopenAdmin(admin.ModelAdmin):
    list_display = ['id','project_name','at', 'by', 'landp_arcel','possession','spot_booking_offers','early_buy_discounts','flexipay_for_first','luxurious','priceing']
admin.site.register(Bookingopen, BookingopenAdmin)


# Register your models here. 8
class WelcometoAdmin(admin.ModelAdmin):
    list_display = ['id','title','details', 'readmore',]
admin.site.register(Welcometo, WelcometoAdmin)
