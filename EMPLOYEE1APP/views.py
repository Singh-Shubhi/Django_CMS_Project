from django.shortcuts import render,redirect,get_object_or_404
from ADMIN1APP.models import Employee1,Product1,Appointment,Deal,Doctor
from ADMIN1APP.forms import ProductForm,DoctorForm,AppointmentForm,TodayScheduleForm,DealForm
from django.contrib import messages




# Create your views here.

#home page view here .....................................................................................................................
def home_page(request):
    return render(request,'base/index.html')


#login view here .........................................................................................................................
def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            employee = Employee1.objects.get(email=email, password=password)
        except Employee1.DoesNotExist:
            employee = None

        if employee is not None:
            if employee.status == 'Active':
                request.session['logged_in'] = True
                
                return redirect('dashboard-page')
            else:
                error_message = "Your account has not been activated for a long time, so your account has been deactivated."
                return render(request, 'EMPLOYEE1APP/login.html', {'error_message': error_message})
        else:
            error_message = 'Invalid email or password'
            return render(request, 'EMPLOYEE1APP/login.html', {'error_message': error_message})

    if 'logout' in request.GET:
        request.session.clear()
        return redirect('login-page')  
    
    
    return render(request, 'EMPLOYEE1APP/login.html')





# dashboard view here.......................................................................................................................
def dashboard_page(request):
    if not request.session.get('logged_in'):
        return redirect('login-page') 
    else:  
        employee = Employee1.objects.all()
        products = Product1.objects.all()
        doctor = Doctor.objects.all()
        appointment = Appointment.objects.all()
        deal = Deal.objects.all()
        total_employee = employee.count()
        total_product = products.count()
        total_doctor = doctor.count()
        total_appointment = appointment.count()
        total_deal = deal.count()
        top_orders = Deal.objects.order_by('-quantity_ordered')[:10]

    dict = {
        'employee':employee,
        'products':products,
        'doctor':doctor,
        'deal':deal,
        'total_employee':total_employee,
        'total_product':total_product,
        'total_doctor':total_doctor,
        'total_appointment':total_appointment,
        'total_deal':total_deal,
        'top_orders' : top_orders,
    }

    return render(request, 'EMPLOYEE1APP/dashboard.html',dict)


# add product page view here ................................................................................................................
def add_products(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        
        if form.is_valid():
            price = form.cleaned_data['product_price']
            if price <= 0:
                form.add_error('product_price', 'Price must be greater than zero.')
            else:
                form.save()
                return redirect('product-success')
    
    return render(request, 'EMPLOYEE1APP/add_products.html', {'form': form})

 
# add product success page view here.........................................................................................................
def product_added_success(request):
    return render(request, 'EMPLOYEE1APP/product_added_success.html')


# view product page view here................................................................................................................
def view_products(request):
    products = Product1.objects.all()
    return render(request, 'EMPLOYEE1APP/views_all_products.html', {'products': products})

# delete product view here...................................................................................................................
def delete_product(request, pk):
    product = get_object_or_404(Product1, id=pk)

    if request.method == 'POST':
        product.delete()
        return redirect('views-products')  

    return render(request, 'EMPLOYEE1APP/delete_product.html', {'product': product})

# edit product view here......................................................................................................................
def edit_products(request, pk):
    product = get_object_or_404(Product1, id=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('edit-success')  
    else:
        form = ProductForm(instance=product)

    return render(request, 'EMPLOYEE1APP/edit_products.html', {'form': form, 'product': product})


# edit success view here.................................................................................................................................
def edit_success(request):
    return render(request, 'EMPLOYEE1APP/edit_success.html')


# add doctor page view here...................................................................................................................
def add_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES)
        contact = request.POST.get('contact_number')
        # print('CNT',contact)
        if len(contact) != 10:
            messages.error(request,"Phone Number Should be exactly 10 in Length.")
        else:    
            if form.is_valid():
                form.save()
                return redirect('doctor-success')
    else:
        form = DoctorForm()
    return render(request, 'EMPLOYEE1APP/add_doctor.html', {'form': form})

# add doctor success page view here.......................................................................................................
def doctor_added_success(request):
    return render(request, 'EMPLOYEE1APP/doctor_added_success.html')

# add schedule appointment page view here.................................................................................................
def schedule_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment-done')  # Redirect to a success page
    else:
        form = AppointmentForm()

    return render(request, 'EMPLOYEE1APP/appointment.html', {'form': form})


# add appointment done page view here.....................................................................................................
def appointment_done(request):
    return render(request, 'EMPLOYEE1APP/appointment_done.html')

# add today schedule page view here........................................................................................................
def today_schedule(request):
    if request.method == 'POST':
        form = TodayScheduleForm(request.POST)
        if form.is_valid():
            selected_date = form.cleaned_data['date_selector']
            appointments = Appointment.objects.filter(date_of_schedule=selected_date)
            return render(request, 'EMPLOYEE1APP/today_schedule_details.html', {'form': form,'appointments': appointments})
    else:
        form = TodayScheduleForm()

    return render(request, 'EMPLOYEE1APP/today_schedule.html', {'form': form})

# add today schedule details page view here.................................................................................................
def today_schedule_details_page(request):
    return render(request, 'EMPLOYEE1APP/today_schedule_details.html')


# add deals details page view here.........................................................................................................
def deals_details(request):
    if request.method == 'POST':
        form = DealForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('deal-done')  
    else:
        form = DealForm()

    return render(request, 'EMPLOYEE1APP/deals_details.html', {'form': form})

# add deal done  page view here..........................................................................................................
def deal_done(request):
    return render(request, 'EMPLOYEE1APP/deal_done.html')


def forgot_password_page(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            employee = Employee1.objects.get(email=email, status='Active')
            success_message = 'Password reset instructions sent to your email'
            return render(request, 'EMPLOYEE1APP/forgot_password.html', {'success_message': success_message})
        except Employee1.DoesNotExist:
            error_message = 'Invalid email'
            return render(request, 'EMPLOYEE1APPS/forgot_password.html', {'error_message': error_message})
    return render(request, 'EMPLOYEE1APP/forgot_password.html')
