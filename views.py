from django.shortcuts import render,redirect
from .models import ProductData
from .forms import ProductDeleteForm,ProductInsertForm,ProductUpdateForm
from django .http .response import HttpResponse
# Create your views here.
def home(request):
    return render(request,"home.html")
def Product_insert_view(request):
    if request.method=="POST":
        iform=ProductInsertForm(request.POST)
        if iform.is_valid():
            product_id=request.POST.get('product_id','')
            product_type=request.POST.get('product_type','')
            product_cost =request.POST.get('product_cost','')
            product_class=request.POST.get('product_class','')
            product_color = request.POST.get('product_color', '')
            brand_name=request.POST.get('brand_name','')
            organisation_mobile_no=request.POST.get('organisation_mobile_no','')
            organisation_email=request.POST.get('organisation_email','')

            data=ProductData(
                product_id=product_id,
                product_type=product_type,
                product_cost=product_cost,
                product_class=product_class,
                product_color=product_color,
                brand_name=brand_name,
                organisation_mobile=organisation_mobile_no,
                organisation_email=organisation_email,
            )
            data.save()
            iform=ProductInsertForm()
            return render(request, 'create.html', {'iformh':iform})
    else:
        iform=ProductInsertForm()
        return render(request,'create.html',{'iformh':iform})

def product_update_view(request):
    if request.method=="POST":
       uform=ProductUpdateForm(request.POST)
       if uform.is_valid():
           product_idu=request.POST.get('product_id','')
           product_costu=request.POST.get('product_cost','')
           pdata=ProductData.objects.filter(product_id=product_idu)
           if not pdata:
               return HttpResponse("products are not avilable")
           else:
               pdata.update(product_cost=product_costu)
               uform=ProductUpdateForm()
               return render(request,'update.html',{'uformh':uform})
    else:
        uform=ProductUpdateForm()
        return render(request,'update.html',{'uformh':uform})



def product_retrive_view(request):
    rdata=ProductData.objects.all()
    return render(request,'retrive.html',{'rdatah':rdata})



def product_delete_view(request):
    if request.method=="POST":
       dform=ProductDeleteForm(request.POST)
       if dform.is_valid():
           product_idd=request.POST.get('product_id','')
           pdatad=ProductData.objects.filter(product_id=product_idd)
           if not pdatad:
               return render(request,'noid.html')
           else:
               pdatad.delete()
               dform=ProductDeleteForm()
               return render(request,'delete.html',{'dformh': dform})
    else:
        dform=ProductDeleteForm()
        return render(request, 'delete.html', {'dformh': dform})



