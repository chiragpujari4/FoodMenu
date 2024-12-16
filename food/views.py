from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Items
from django.template import loader
from .forms import ItemForm
from django.views.generic.edit import CreateView

def index(request):
    item_list=Items.objects.all()
    context={
        'item_list':item_list,
    }
    return render(request, 'food/index.html', context)

def items(request):
    return HttpResponse("This is an item view.")


def detail(request, item_id):
    item=Items.objects.get(id=item_id)
    context={
        'item':item,
    }
    return render(request, 'food/detail.html', context)

#def create_item(request):
    form=ItemForm(request.POST or None)
    

    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request,'food/item-form.html',{'form':form})

#class based view for create item user association

class CreateItem(CreateView):
    model=Items
    fields= ['item_name','item_desc','item_price','item_image']
    template_name='food/item-form.html'
    
    def form_valid(self,form):
        form.instance.user_name=self.request.user
        
        return super().form_valid(form)

def update(request, item_id):
    item=Items.objects.get(id=item_id)
    form=ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request,'food/item-form.html',{'form':form,'item':item})

def delete(request,item_id):
    item=Items.objects.get(id=item_id)

    if request.method=='POST':
        item.delete()
        return redirect('food:index')
    
    return render(request,'food/delete-confirm.html',{'item':item})

