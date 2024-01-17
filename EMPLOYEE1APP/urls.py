from django.urls import path
from .views import dashboard_page,login_page,forgot_password_page,add_products,product_added_success,view_products,delete_product,edit_products,edit_success,add_doctor,doctor_added_success,schedule_appointment,appointment_done,today_schedule,today_schedule_details_page,deals_details,deal_done

urlpatterns =[
    path('dashboard/',dashboard_page,name="dashboard-page"),
    # path('chart/',chart,name="chart-page"),
    path('login/',login_page,name="login-page"),
    path('reset_password/',forgot_password_page, name='reset-password'),
    path('add_products/',add_products,name="product-page"),
    path('product_success/',product_added_success,name="product-success"),
    path('views/',view_products,name="views-products"),
    path('delete/<int:pk>',delete_product,name="delete"),
    path('edit/<int:pk>',edit_products,name="edit"),
    path('edit_success/',edit_success,name="edit-success"),
    path('add_doctor/',add_doctor,name="add-doctors"),
    path('doctor_success_page/',doctor_added_success,name="doctor-success"),
    path('appointment/',schedule_appointment,name="appointment-page"),
    path('appointment_done_page/',appointment_done,name="appointment-done"),
    path('today_schedule/',today_schedule, name='today-schedule'),
    path('today_schedule_details/',today_schedule_details_page, name='today-schedule-page'),
    path('deals_details/',deals_details, name='deals-details'),
    path('deal_done/',deal_done, name='deal-done'),
    # path('view_deal/',view_deal,name="view-deal"),
    
    
]