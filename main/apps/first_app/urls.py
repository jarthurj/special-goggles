from django.urls import re_path, path
from . import views           # This line is new!
urlpatterns = [
  path("", views.index, name="index"),     # This line has changed!
  path("new/", views.new),
  path("create/", views.create),
  path("<int:blog>/", views.blog_by_number),
  path("<int:blog>/edit", views.edit_blog),
  path("<int:blog>/delete", views.delete),
]

# / - display "placeholder to later display all the list of blogs" via HttpResponse. Have this be handled by a method named 'index'.
# /new - display "placeholder to display a new form to create a new blog" via HttpResponse. Have this be handled by a method named 'new'.
# /create - Have this be handled by a method named 'create'.  For now, have this url redirect to /.
# /{{number}} - display 'placeholder to display blog {{number}}'.  For example /15 should display a message 'placeholder to display blog 15'.  Have this be handled by a method named 'show'.
# /{{number}}/edit - display 'placeholder to edit blog {{number}}'.  Have this be handled by a method named 'edit'.
# /{{number}}/delete - Have this be handled by a method named 'destroy'. For now, have this url redirect to /.