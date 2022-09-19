from doctest import master
from django.shortcuts import render,redirect
from App.forms import MyForm
from App.models import Master
# Create your views here.

data = {}
data["view_form"] = MyForm()
def index(request):
    return render(request,"index.html")

def form_page(request):
    return render(request,"forms.html",data)

def form_submit(request):
    print(request.POST)
    print(request.POST['Name'])

    data["form_data"] = {}

    for k,v in request.POST.items():
        data["form_data"].setdefault(k,v)

    Master.objects.create(
        Name = request.POST["Name"],
        Email = request.POST["Email"],
        Password = request.POST["Password"]       
    )
    return redirect(form_page)

def data_page(request):
    return render(request,"data.html",data)

def get_data(request):
    master = Master.objects.get(Email=request.POST['Email'])
    data['Email_data'] = master
    return redirect(data_page)
    
def update_page(request):
    master = Master.objects.get(Email=request.POST['Email'])
    master.Name = request.POST['Name']
    master.Password = request.POST['Password']
    master.save()
    data['Email_data'] = master
    return redirect(data_page)