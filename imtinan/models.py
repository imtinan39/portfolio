from django.db import models

# Create your models here.


class Skill(models.Model):

	title=models.CharField(max_length=50)
	skill=models.CharField(max_length=50)




	def __str__(self):
   		return self.skill



class Contact(models.Model):


	phone=models.CharField(max_length=12)
	email=models.EmailField(max_length=100)
	github=models.URLField(max_length=500)
	linkedin=models.URLField(max_length=500)
	insta=models.URLField(max_length=500)
	fb=models.URLField(max_length=500)


	def __str__(self):
   		return self.email

class Blog(models.Model):

	title=models.CharField(max_length=100)
	description=models.TextField(max_length=1000)
	image=models.ImageField(upload_to='portfolio/blog/images')
	tag=models.CharField(max_length=50)
	url=models.URLField(max_length=500,blank=True)




	def __str__(self):
   		return self.title


class PostImage(models.Model):
	post=models.ForeignKey(Blog,default=None, on_delete=models.CASCADE)
	image=models.ImageField(upload_to='portfolio/blog/images')
	caption=models.CharField(max_length=100)

	def __str__(self):
   		return self.post.title



class ContactForm(models.Model):

	email=models.EmailField(max_length=100)
	text=models.TextField(max_length=100)




	def __str__(self):
   		return self.email

class Photos(models.Model):


	image=models.ImageField(upload_to='portfolio/blog/images')

	caption=models.CharField(max_length=100)

	def __str__(self):

		return self.caption









	
