from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

posts=[
	{
		'author': 'Mr. mamun',
		'title': 'hello world',
		'date_posted': '27 oct 2021',
		'conent': 'explaination of first fillings'
	},
	{
		'author': 'Mr. kashem',
		'title': 'hello world go',
		'date_posted' :'24 june 2022',
		'conent': 'explaination of next fillings'
	}
]

def home(request):
	context={
		'posts':posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html',{'title':'about'})