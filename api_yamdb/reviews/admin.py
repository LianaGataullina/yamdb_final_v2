from django.contrib import admin
from .models import Title, User
from .models import Comment, Review, Genres, Categories


admin.site.register(User)
admin.site.register(Review)
admin.site.register(Comment)
admin.site.register(Genres)
admin.site.register(Categories)
admin.site.register(Title)
