from django.contrib import admin
from .models import Restaurante

# Register your models here.
class RestauranteAdmin(admin.ModelAdmin):
    search_fields = ["nome"]
    list_display = (
        "id",
        "nome",
        "tipo",
        "horario",
        "num_funcionarios",
        "capacidade",
        "created_at",
        "modified_at",
    )


admin.site.register(Restaurante, RestauranteAdmin)
