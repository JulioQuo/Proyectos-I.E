from django.contrib import admin
from .models import Genero,Imprenta,Libro
# Register your models here.

class LibroAdmin(admin.ModelAdmin):
    list_display = ['nombre','autor','genero','año','sinopsis','precio','num_pag','imprenta']
    search_fields = ['nombre','año']
    list_filter = ['genero']
    list_per_page= 20

admin.site.register(Genero)
admin.site.register(Imprenta)
admin.site.register(Libro, LibroAdmin)

