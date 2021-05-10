from django.contrib import admin
from .models import Skill,Contact,Blog,PostImage,ContactForm,Photos
# Register your models here.

admin.site.register(Skill)
admin.site.register(Contact)
admin.site.register(ContactForm)

admin.site.register(Photos)




class PostImageAdmin(admin.StackedInline):

	model=PostImage

@admin.register(Blog)
class PostAdmin(admin.ModelAdmin):

	inlines=[PostImageAdmin]


	class Meta:

		model=Blog

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):

	pass

