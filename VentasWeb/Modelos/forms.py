from django.forms import *
from .models import Category

############################################################################

class CategoryForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs["class"] = "form-control"
            form.field.widget.attrs["autocomplete"] = "off"

    class Meta:
        model = Category
        fields = "__all__"
        widgets = {
            "name" : TextInput(
                attrs = {
                    "placeholder":"Nombre de categoria"
                }
            ),
        }
        exclude = ["usuario","user_update",]
    
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data["error"] = form.errors
        except Exception as e:
            data["error"] = str(e)
        return data
    


class CategoryEditForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs["class"] = "form-control"
            form.field.widget.attrs["autocomplete"] = "off"

    class Meta:
        model = Category
        fields = "__all__"
        widgets = {
            "name" : TextInput(
                attrs = {
                    "placeholder":"Nombre de categoria"
                }
            ),
        }
        exclude = ["usuario","user_update",]
    
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data["error"] = form.errors
        except Exception as e:
            data["error"] = str(e)
        return data
    