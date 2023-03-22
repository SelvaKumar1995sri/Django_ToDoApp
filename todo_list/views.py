from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import List
from .forms import ListForm
from django.db.models import Q


def home(request):
    if request.method == "POST":
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('The item has been added to list successfully!'))
            all_items = List.objects.all
            return render(request, 'home.html', {'all_items': all_items})    
    else:
        all_items = List.objects.all()
        return render(request, 'home.html', {'all_items': all_items})

def about(request):
    return render(request, 'about.html', {})

def delete(request, item_id):
    item = List.objects.get(pk=item_id)
    item.delete()
    messages.success(request, ('The item has been deleted successfully!'))
    return redirect('home')



def edit(request, item_id):
    if request.method == "POST":
        item = List.objects.get(pk=item_id)
        form = ListForm(request.POST or None, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, ('The item has been edited successful!'))
            return redirect('home')   
    else:
        item = List.objects.get(pk=item_id)
        return render(request, 'edit.html', {'item': item})


from django.views.generic import TemplateView, ListView

class SearchResultsView(ListView):
    model = List
    template_name = 'search.html'
    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = List.objects.filter(
            Q(item__icontains=query)
        )
        return object_list