from django.contrib import admin

from .models import Produto, Cliente

#Classe para exibir vários atributos na seção de produtos
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')


#Classe para exibir vários atributos na seção de produtos
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)
