from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from Django_PG_1.models import Post,Topic,Board
from Django_PG_1.forms import SignupForm_Example
from Django_PG_1.forms import login_FormExample,new_topic
from django.contrib.auth import login, authenticate,logout,get_user_model
from django.contrib.auth.decorators import login_required

# Create your views here.
def hello(request):
	return HttpResponse("Hi You are about tpo view the app")


def liveops(request):
		return HttpResponse(5+4)

@login_required
def posts_table(request):
	data_posts=Post.objects.all()
	return render(request,'posts.html',{"data_posts":data_posts})

	
@login_required
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
			authenticate(password=user.password,username=user.username)
			print(request.user)
			login(request,user)
			print(request.user.is_authenticated)
			print(request.user.is_staff)
			return redirect('logout')

	else:

		#form =SignupForSm_
		form =SignupForm_Example(request.GET)
		print("yaaay")
	return render(request,'signup.html',{'sign':form})

#@login_required
def logoutt(request):
	logout(request)
	return render(request,'logout.html')

def loginform(request):
	if request.method=='POST':
		form =login_FormExample(request.POST or None)
		if form.is_valid():
			password=form.cleaned_data.get('password')
			username=form.cleaned_data.get('username')
			instant_creds=authenticate(password=password,username=username)
			"""
			if instant_creds:
				login(request,instant_creds)
				return HttpResponse("loggedon")
			else:
				return HttpResponse('invalid creds')"""
			login(request,instant_creds)
			return redirect('posts_table')
		else:
			return HttpResponse('invalid form')
	else:
		form =login_FormExample()
	return render (request,'loginform.html',{'form':form})

def dashboard(request):
	return render(request,'dashboard.html')


def allboards(request):
	boards=Board.objects.all()
	return render(request,'boards_file.html',{'boards':boards})

def board(request,pk):
	board = get_object_or_404(Board,pk=pk)
	topics = Topic.objects.filter(child_board=board)
	return render(request,'topics.html',{'topics':topics,'board':board})

def create_topic(request,pk):
	if request.method =="POST":
		new_topicform=new_topic(request.POST or None)
		if new_topicform.is_valid():
			subject=new_topicform.cleaned_data.get('subject')
			#updated_time=new_topicform.cleaned_data.get('updated_time')
			board = get_object_or_404(Board,pk=board.pk )
			CurrentUser=request.user
			#we have all our variables with data
			#create a new instance of topic
			Topic = Topic.objects.create(
				subject='subject',
				#updated_time='updated_time',
				child_board='board',
				Topic_Beginner='CurrentUser'

				)
			Topic.save()#relational algebra
			returnHttpResponse("Post saved")
			#return redirect('')
	else:
		new_topicblankform=new_topic()
	return render(request,"new_topic.html",{'new_topicform':new_topicblankform})


