from django import forms
from .models import Product1,Doctor,Employee1,Appointment,Deal
from django import forms
from datetime import date



# product form here...........................................................................................................................
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product1
        fields = ['product_name', 'company_name', 'product_image', 'product_price', 'entered_by']
        
# doctor form here........................................................................................................................... 
class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'specialisation', 'contact_number', 'location', 'entered_by']
    


# appointment form here.....................................................................................................................
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor', 'date_of_schedule', 'time_of_schedule', 'entered_by']

        widgets = {
            'date_of_schedule': forms.DateInput(attrs={'type': 'date'}),
            'time_of_schedule': forms.TimeInput(attrs={'type': 'time'}),
        }

    def clean_date_of_schedule(self):
        selected_date = self.cleaned_data['date_of_schedule']
        current_date = date.today()

        if selected_date < current_date:
            raise forms.ValidationError("Selected date must be today or future's date.")
        return selected_date

# todayschedule form here....................................................................................................................  
class TodayScheduleForm(forms.Form):
    date_selector = forms.DateField(
        label='Select Date',
        initial=date.today,
        widget=forms.DateInput(attrs={'type': 'date'})
    )


# deal form here.............................................................................................................................
class DealForm(forms.ModelForm):
    class Meta:
        model = Deal
        fields = ['doctor', 'product_name1', 'quantity_ordered', 'entered_by']

    def clean_quantity_ordered(self):
        quantity = self.cleaned_data['quantity_ordered']
        if quantity <= 0:
            raise forms.ValidationError("Quantity should not be negative and zero.")
        return quantity