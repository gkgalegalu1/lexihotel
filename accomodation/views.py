from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from accomodation.models import Booking
from django.contrib import messages
from django.contrib.auth.models import User, auth


from datetime import date

def about(request):
    return render(request, 'accomodation/about.html')

def register(request):
    return render(request, 'accomodation/register.html')

def register_employee(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email']
        
        if  password == password2:
            if User.objects.filter(username=username).exists():
                
                messages.info(request, 'Username taken')
                return redirect('register')
            
            elif User.objects.filter(email=email).exists():
                messages.add_message(request, messages.INFO, "email taken. Please use another email")
                return redirect('register')
            else:   
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, password=password, email=email)
                user.save();
                return render(request, 'accomodation/login.html')
                 
        else:
            messages.add_message(request, messages.INFO, "password does not much")
            return redirect('register')
    
    else:
        return render(request, 'register.html')   
    

def login(request):
    return render(request, 'accomodation/login.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            #messages.info(request, f'Now you are loggedin as {user} ' )
            messages.info(request, f'Now you are loggedin as {user} ' )
 
            return render(request, 'accomodation/employee_page.html')
        else:
            messages.error(request, 'Invalid credentials')
            return render(request, 'accomodation/login.html')
    else:
        return render(request, 'accomodation/login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')


def check_reservation(request):
    booking = Booking.objects.all().values()
    return render(request, 'accomodation/showcustomers.html', {'booking':booking})

def rooms(request):
    #for room in rooms:
    return render(request, 'accomodation/rooms.html', {'large':74.99, 'medium':49.99, 'small':39.99})
    
    
def home(request):
    return render(request, 'accomodation/home.html', {'cost':cost})

cost=float(49.99)
def makereservation(request):
    
    return render(request, 'accomodation/reservationpage.html', {'cost':cost})

def calc_price(request, num_days, price_of_a_room, num_of_rooms):
    price = num_days * price_of_a_room * num_of_rooms
    

def submit_reservation(request):
    if request.method=='POST':
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        email=request.POST['first_name']
        phone=request.POST['phone']
        arrival=request.POST['arrival_date']
        number_of_staying_days=int(request.POST['num_of_days'])
        rooms=int(request.POST['rooms'])
        adults=request.POST['adult']
        kids=request.POST['kids']
        total_cost =  cost * rooms * number_of_staying_days 
        
        
        booking = Booking(first_name=firstname, last_name=lastname, email=email,phone=phone, arrival_date=arrival, num_of_days=number_of_staying_days, number_of_rooms=rooms, number_of_adults=adults,number_of_kids=kids )
        booking.save()
        
        customer = {'firstname':firstname,
                    'lastname':lastname, 
                   'email':email,
                   'arrival':arrival,
                   'number_of_staying_days':number_of_staying_days,
                   'rooms':rooms,
                   'adults':adults,
                   'kids':kids,
                   'cost':cost,
                   'total_cost':total_cost
                   
                  
                  }
        return render(request, 'accomodation/makereservation.html', {'customer':customer})
def record_payment(request):
    if request.method=='POST':
        booking = Booking.objects.all().values()
        booking['paid']=request.POST['total_cost']
        return render(request, 'pay_for_stay.html')

def pictures(request):
    return render(request, 'accomodation/pictures.html')       
        
