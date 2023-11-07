
from django.contrib import messages,auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        un = request.POST['username']
        pw = request.POST['password1']
        cpw = request.POST['password2']


        if pw==cpw:
            if User.objects.filter(username=un):
                messages.info(request,"username taken")
                return redirect('register:register')
            else:
                user = User.objects.create_user(username=un, password=pw)
                user.save();
                print("user created")
                return redirect('login:login')

        else:
            print("password not matching ")
            return redirect('register')
        return redirect('register:register')

    else:
        return render(request, 'register.html')

















# def register(request):
#     if request.method == 'POST':
#         form = CustomRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('login')  # Change 'home' to your desired redirect URL
#     else:
#         form = CustomRegistrationForm()
#     return render(request, 'register.html', {'form': form})

#
#
#     if request.method=='POST':
#         username=request.POST.get('username')
#         password1 = request.POST.get('password1')
#         password2 = request.POST.get('password2')
#         if password1!=password2:
#             return render(request,'register.html')
#         my_user=User.objects.create_user(username,password1)
#         my_user.save()
#         return redirect('login')
#     return render(request, 'register.html')