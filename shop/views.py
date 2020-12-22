from django.shortcuts import render
from django.http import HttpResponse
from .models import Product_des,Contact,Order
from math import ceil

# Create your views here.
def index(request):
    #products=Product_des.objects.all()
    #n=len(products)
    #nslides=ceil(n/4)
    #print("products:- ",products)
    #params={'products':products,'range':(1,nslides),'nslides':nslides}
    #allprods=[[products,range(1,nslides),nslides],[products,range(1,nslides),nslides]]
    allprods=[]
    catprods=Product_des.objects.values('category','product_id')
    catitems={item['category'] for item in catprods}
    #print(catitems)
    for c in catitems:
        products=Product_des.objects.filter(category=c)
        n = len(products)
        nslides=ceil(n/4)
        allprods.append([products,range(1,nslides),nslides])
    params={'allprods':allprods}
    return render(request,'shop/index.html',params)

def searchmatch(search_text,item):
    if search_text.lower() in item.product_name.lower() or \
        search_text.lower() in item.category.lower() or \
            search_text.lower() in item.product_desc.lower():
        return True
    else:
        return False
def search(request):
    search_text=request.GET.get('search','')
    allprods = []
    catprods = Product_des.objects.values('category', 'product_id')
    catitems = {item['category'] for item in catprods}
    # print(catitems)
    for c in catitems:
        products = Product_des.objects.filter(category=c)
        sprods=[item for item in products if searchmatch(search_text,item)]
        n = len(sprods)
        nslides = ceil(n / 4)
        if n !=0:
            allprods.append([sprods, range(1, nslides), nslides])
    params = {'allprods': allprods,"msg":""}
    if (len(allprods) == 0):
        params = {"msg": "Please enter proper search name"}

    return render(request, 'shop/search.html', params)


def aboutus(request):
    return render(request,'shop/about.html')

def contactus(request):
    if request.method == 'POST':
        name=request.POST.get('name','')
        email=request.POST.get('emailid','')
        phone=request.POST.get('phoneno','')
        msg=request.POST.get('msg','')
        contact=Contact(name=name,email=email,phone=phone,msg=msg)
        contact.save()
        print(name,email,phone,msg)
    return render(request,'shop/contactus.html')

def productview(request,pid):
    prview = Product_des.objects.filter(product_id=pid)
    print(prview)
    return render(request,'shop/prodview.html',{'prview':prview[0]})

def checkout(request):
    flag=False
    if request.method == 'POST':
        itemjson=request.POST.get('itemjson','')
        fname=request.POST.get('firstName','')
        lname=request.POST.get('lastName','')
        email=request.POST.get('emailid','')
        address=request.POST.get('address','') + request.POST.get('address2','')
        phone=request.POST.get('phone','')
        country=request.POST.get('country','')
        state=request.POST.get('state','')
        zipcode=request.POST.get('zip','')
        total=request.POST.get('totalprice','')

        order=Order(itemjson=itemjson,fname=fname,lname=lname,email=email,address=address,
                    phone=phone,country=country,state=state,zipcode=zipcode,totall=total)
        order.save()
        flag=True
        return render(request,'shop/checkout.html',{'flag':flag})
    return render(request,'shop/checkout.html')

