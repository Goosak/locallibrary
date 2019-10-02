from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

#admin.site.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
	fields = ['first_name','last_name',('date_of_birth', 'date_of_death')]

admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
admin.site.register(Language)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display=('title', 'author')

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
	list_filter = ('status', 'due_back')
	fieldsets=(
		(None, {
			'fields':('book', 'imprint', 'id')
		}),
		('Availability',{
			'fields':('status', 'due_back')
		})
	)