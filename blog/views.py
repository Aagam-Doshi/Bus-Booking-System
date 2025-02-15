from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# from .utils import generate_otp, verify_otp
# from django.core.mail import send_mail
# from django.conf import settings



def home(request):
    return render(request,'blog/home.html')   

def about(request):
    return render(request,'blog/about.html')

def browse(request):
    
    print("Hello Aagam!!")
    
    return render(request,'blog/base.html')
    

def browse_with_details(request):

    destination=request.GET.get('dest')
    source=request.GET.get('src')

    
    print (source,destination)

    buses=Bus.objects.filter(startDest=source,endDest=destination)
    # print (buses)
    
    listOfSchedule=[]
    for bus in buses:
        print (bus.busId)

        schedules= Schedule.objects.filter(busId=bus)
        for schedule in schedules:
            schedule_dict = {
            "from":source,
            "to":destination,
            "busId":bus.busId,
            "id": schedule.id,
            "depTime": schedule.depTime.strftime("%Y-%m-%d %H:%M:%S"),
            "arrTime": schedule.arrTime.strftime("%Y-%m-%d %H:%M:%S"),
            "seatsRemaining": schedule.seatsRemaining
            }
            listOfSchedule.append(schedule_dict)

    print(listOfSchedule)
            
        
        
    
    
    # print(schedules,schedules_list)
    # context={
    #     'deptime':str(deptime),
    #     'arrtime':str(arrtime),
    # }


    return render(request,'blog/base.html',{"schedules":listOfSchedule})


@login_required(login_url='/login')
def booking(request,id):
    

    print (id)
    detail=Schedule.objects.get(id=id)
    seat_remain=detail.seatsRemaining

    context={'id':id,
        'seat_remain':seat_remain ,


        }
    

    if(request.method=='POST'):
        passname=request.POST.get('passname')
        #wallet check and reduce should be here
        booking_obj=Booking.objects.create(pasNam=passname,customer=request.user,schedule=detail)
        if booking_obj is not None:
            return redirect("/")#later redirect to upcoming journeys



    return render(request,'blog/booking.html',context)

def login(request):
    if(request.method=='POST'):
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=MyUser.objects.get(username=username,password=password)
        print(user)

        if user is not None:
            auth.login(request,user)
            return redirect("/")

    
    return render(request,'blog/login.html')


def logout_view(request):
    logout(request)
    return render(request,'blog/home.html')



def register(request):
    print(request.method)
    if(request.method=='POST'):
        
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=MyUser.objects.create(username=username,password=password)
        # user=MyUser()
        # user.username=username
        # user.password=password
        # user.save()

        print(user)


        if user is not None:
            auth.login(request,user)
            return redirect("/")
    
    return render(request,'blog/register.html')
    

    

