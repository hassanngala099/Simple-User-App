from django.shortcuts import render,HttpResponse
from Django_PG_1.models import Post,Topic,Board
from Django_PG_1.forms import SignupForm_Example
from django.contrib.auth import login, authenticate,logout,get_user_model

# Create your views here.
def hello(request):
	return HttpResponse("Hi You are about tpo view the app")


def liveops(request):
		return HttpResponse(5+4)


def posts_table(request):
	data_posts=Post.objects.all()
	return render(request,'posts.html',{"data_posts":data_posts})

def boards_table(request):
	data_boards=Board.objects.all()
	return render(request,'boards.html',{"k":data_boards})

def topics_table(request):
	data_topics=Topic.objects.all()
	context = {
	"topics_table":data_topics
	}
	return render(request,'topics_table.html',context)

def fetchdataform_table(request):
	
	return render(request,'form.html',{}) #this function renders the form.html which collects data login_form_table

def login_form_table(request):# we expect to receive variables entered in the form.html,this view converts form fields in pythin readable format
	name = request.GET['name']
	email=request.GET['email']
	phone=request.GET['phone']
	message=request.GET['message']
	return render(request,'form_data.html',{"name":name,"email":email,"phone":phone,"message":message}) 


def SignupForm_Example_f(request):
	if request.method == 'POST':
		form = SignupForm_Example(request.POST or None)
		if form.is_valid():
			user=form.save(commit=False)
			password=form.cleaned_data.get('password')
			user.set_password(password)
			user.save()
			login(request,user)
			print(request.user.is_authenticated)
			print(request.user.is_valid)
	else:

		#form =SignupForm_
		form =SignupForm_Example(request.GET)
		print("yaaay")
	return render(request,'signup.html',{'form':form})
"""
def signup(request):
    if request.method == 'POST':
        form = SignupForm_Example(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            #username =     form.cleaned_data.get('username')
            password =     form.cleaned_data.get('password')
            #email =        form.cleaned_data.get("email")
            #user = authenticate(username=username, password=raw_password)
            user.set_password(password)
            user.save()
            login(request,user)
            print(request.user.is_authenticated)
    else:
        #form = SignupForm_Example()
        print("yaaay")
    return render(request, 'signup.html', {'form': form})
"""



