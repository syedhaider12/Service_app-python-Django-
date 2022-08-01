from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth
from twilio.rest import Client
from .models import TwoToken
from helper import randon_str

from .models import bussiness
from .models import contact

TWILIO_ACCOUNT_SID = "AC6d4aa402e75e756db6ed37b3ac918d71"
TWILIO_AUTH_TOKEN = "2e78ddff89cae193d14f03dddde19bbc"
c = Client(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN)



def home(request):
    if request.method == 'POST':
        search = request.POST['search']
        ser = search.upper()
        print(ser)
        result = bussiness.objects.filter(category=ser).all()
        return render(request,'home.html', {'res': result , 'search': ser})
    else:
        res = bussiness.objects.filter(category='RESTURANT')[:4]
        home = bussiness.objects.filter(category='HOMESERVICE')[:4]
        plum = bussiness.objects.filter(category='PLUMBER')[:4]
        return render(request , 'home.html',{'re':res,'hom':home , 'plum': plum})

    




    
   
    

        
        
   

def rest(request):
     res = bussiness.objects.filter(category='RESTURANT').all()
     return render(request,'resturant.html', {'res': res})

def hom(request):
    
    home = bussiness.objects.filter(category='HOMESERVICE').all()
    return render(request,'homeservice.html', {'hom': home})

def plumb(request):
    plum = bussiness.objects.filter(category='PLUMBER').all()
    return render(request,'plumber.html',{'plum': plum})


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        mobile = request.POST['mobile']
        user = auth.authenticate(username=email, password=password)
        print("yes")
        if user is not None:
            print("no")
            
            
            opt = randon_str()
            print(opt)
            u = User.objects.get(username=email)
            d =TwoToken(user_id=u.id)
            c.messages.create(from_='+18589433602', body= opt , to = '+' + mobile)
            TwoToken(user_id=u.id, code=opt, phone='+' + mobile).save()
            
            
            print("save")

            messages.info(request, f'otp code sent of your mobile number ',mobile)
           
            return render(request,'otp.html')
        else:
            messages.info(request,'incorrect user name or password')
            return redirect('/SignIn')
    return render(request , 'signin.html')

def log(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        #country = request.POST['code']
        #mobile = request.POST['mobile']
        password1 = request.POST['password']
        password2 = request.POST['confirm_password']
        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Exist')
                print('emailtaken')
                return redirect('/SignUp')
            else:
                user = User.objects.create_user(username=email, email=email, first_name=fname, last_name=lname, password=password1)
                user.save()
               # u = User.objects.get(username=email)
                
                #TwoToken(user_id=u.id, phone ='+' + country + mobile).save()
                
                messages.info(request,'User Create Succesfully')
                return redirect('/SignIn')
        else:
            messages.info(request,'Password Not Matching')
            print('passwordnotmatcking')
            return redirect('/SignUp')
        
    else:
        return render(request , 'signup.html')

def ot(request):
    if request.method == 'POST':
        cod = request.POST['verify']
        c=TwoToken.objects.get(code)
        if cod == c:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid code')
            return redirect('/Otp')
    else:
        
        return render(request , 'otp.html')

def cont(request):
    if request.method == 'POST':
        email = request.POST['mail']
        Name = request.POST['nam']
        query = request.POST['text']
        d = contact(Name=Name,email=email,query=query)
        d.save();
        return redirect('/Contactus')
    else:
        return render(request,'contact.html')
def logt (request):
    auth.logout(request)
    return redirect('/')

def quick (request , myid):
  
    va = bussiness.objects.filter(id=myid)
    return render(request, 'quick.html',{'product':va[0]})

def reg(request):
    return render(request , 'register.html')

    

   

