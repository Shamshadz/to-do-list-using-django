from django.shortcuts import render
from to_do_list.forms import saveForm
from to_do_list.models import Create

# Create your views here.
def index(request):
    text = ("this is test for context")

    form = saveForm(request.POST or None)
    if form.is_valid():
        form.save()

    display = Create.objects.all()
    return render(request,'to_do_list/home.html',{'test':text,'display':display})

def add(request):
    return render(request,)

def update(request):
    return render(request,)

def remove(request,pk):
    
    item = Create.objects.get(id= pk)

    if request.method == 'POST':
        item.delete()

    return render(request,'to_do_list/home.html')