from django.shortcuts import render, HttpResponseRedirect
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView
from .models import *
from .forms import *

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
#####################################################

class Inicio(TemplateView):
    template_name="inicio.html"

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        request.user.get_group_session()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Pagina principal'
        context['categorias_list'] = reverse_lazy('category_list')

        return context


class CategoryList(ListView):
    model = Category
    template_name = "category_list.html"

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = Category.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Listado"
        context["filtro"] = Category.objects.all()
        context["url"] = reverse_lazy('category_add')

        return context


class CategoryCreate(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'Form/form_category_create.html'
    success_url = reverse_lazy("category_list")

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = "No ha ingreado a ninguna opcion"
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Crear Categoria"
        context["action"] = "add"
        context["url"] = reverse_lazy('category_list')

        return context

