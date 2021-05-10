from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Skill,Contact,Blog,PostImage,ContactForm,Photos

# Create your views here.



def home(request):

	skill=Skill.objects.all()
	blog_about=Blog.objects.filter(tag='about')[0]
	photos=PostImage.objects.filter(post=blog_about)
	contact=Contact.objects.all()[0]
	blog=Blog.objects.all()[:3]

	return render(request,'imtinan/home.html',{'skills':skill,'about':about,'contact':contact,'blog':blog,'blog_about':blog_about,'photos':photos})




def blog(request):


	blog=Blog.objects.all()
	tag=[]
	for title in blog:
		tag.append(title.tag)
    
	contact=Contact.objects.all()[0]
	tag=set(tag)
	
	
	li=[]
	for tag in tag:

		li.append(Blog.objects.filter(tag=tag)[:3])
		


	

 
    

        


	return render(request,'imtinan/blog.html',{'blogs':li,'contact':contact})





def blog_read(request, blog_id):


    
	blog= get_object_or_404(Blog, pk=blog_id)
	photos=PostImage.objects.filter(post=blog)


	



	return render(request,'imtinan/blog_read.html',{'blog':blog,'photos':photos})





def blog_detailed(request, blog_tag):


	blog=Blog.objects.filter(tag=blog_tag)


	return render(request,'imtinan/blog_detailed.html',{'blogs':blog,'tag':blog_tag})





def contact_form(request):
	contact=Contact.objects.all()[0]

	if request.method=='POST':
		email=request.POST['email']
		text=request.POST['text']

		contactform=ContactForm(email=email,text=text)
		contactform.save()
		return render(request,'imtinan/contact_form.html',{'contact':contact})

	

	return render(request,'imtinan/contact_form.html',{'contact':contact})


def about(request):

	blog=Blog.objects.filter(tag='about').last()

	photos=PostImage.objects.filter(post=blog)

	

	return render(request,'imtinan/about.html',{'blog':blog,'photos':photos})


def project(request):

	project=Blog.objects.filter(tag='project')
	

	return render(request,'imtinan/project.html',{'projects':project,"tag":"Projects"})



def  photos(request):

	photos=Photos.objects.all()


	return render(request,'imtinan/photos.html',{'photos':photos})
 

	










