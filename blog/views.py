from django.shortcuts import get_object_or_404,render, redirect
from .models import Post
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import CreatePostForm
from  django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import Http404



def post_list(request):
	# user= User.objects.all()
	try:
		posts= Post.objects.all().order_by('-date_created')[3:]
		latest_post= Post.objects.all().order_by('-date_created')[:3]
	except Post.DoesNotExist:
		raise Http404(" No content to show")



	context={
		'posts' : posts,
		'latest_post':latest_post,
		# 'user':user,

	}

	return render(request, 'blog/post_list.html', context)

def post_detail(request, post_id):
	
	post= get_object_or_404(Post, pk=post_id)

	return render(request, 'blog/post_detail.html', {'post':post})


def signup(request):
	if request.method == 'POST':
		form = UserCreationFrom(request.POST)

		if form.is_valid():
			form.save()
			username= form.cleaned_data.get('username')
			raw_password= form.cleaned_data.get('password1')
			user= authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('post_list')
	else:
		form= UserCreationForm()
	return render(request, 'signup.html', {'form':form})

@login_required
def add_post(request):
	if request.method == "POST":
		form = CreatePostForm(request.POST, request.FILES)
		if form.is_valid():
			post= form.save(commit=False)
			#post.image = request.FILES.get('image')
			post.author = request.user
			post.date_created = timezone.now()
			post.save()
			return redirect('post_detail', post_id=post.pk)
	else:
		form = CreatePostForm()
	return render(request, 'blog/post_edit.html', {'form':form})

@login_required
def edit_post(request,post_id):
	post= get_object_or_404(Post, pk=post_id)

	if request.method == 'POST':
		form= CreatePostForm(request.POST, instance=post)
		if form.is_valid():
			post= form.save(commit=False)
			#post.image = request.FILES.get('image')
			post.author = request.user
			post.date_created = timezone.now()
			post.save()
			return redirect('post_detail', post_id=post_id)
	else:
		form = CreatePostForm()
	return render(request, 'blog/post_edit.html', {'form':form})



