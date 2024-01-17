from django.contrib import admin
from .models import Employee1,Product1,Doctor,Deal,Appointment
from django.utils.html import format_html

class DisplayEmployee1(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','date_of_joining','status']
    list_filter = ['status']
    search_fields = ['first_name','last_name']
    list_per_page = 5

class DisplayProduct1(admin.ModelAdmin):
    list_display = ['id','product_name','company_name','product_image','product_price','entered_by','display_image']
    list_filter = ['entered_by']
    search_fields = ['product_name','company_name']
    list_per_page = 5

    def display_image(self,obj):
        return format_html ('<img src={} height="100" width="100" />',obj.product_image.url)
    
class DisplayDeal(admin.ModelAdmin):
    list_display = ['id','product_name1','quantity_ordered','entered_by']
    list_filter = ['entered_by']
    list_per_page = 5

class DisplayAppointment(admin.ModelAdmin):
    list_display = ['id','date_of_schedule','entered_by']
    list_filter = ['entered_by','date_of_schedule']
    list_per_page = 5

class DisplayDoctor(admin.ModelAdmin):
    list_display = ['id','name','specialisation','location','entered_by']
    list_filter = ['entered_by']
    search_fields = ['name','location','specialisation']
    list_per_page = 5

# Register your models here.
admin.site.register(Employee1,DisplayEmployee1)
admin.site.register(Product1,DisplayProduct1)
admin.site.register(Doctor,DisplayDoctor)
admin.site.register(Appointment,DisplayAppointment)
admin.site.register(Deal,DisplayDeal)


