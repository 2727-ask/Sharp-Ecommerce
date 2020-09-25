from django.shortcuts import render
from .models import Product
from .models import Ads
from .models import Orders
from .models import OrderUpdate
from .models import Product_Rating
from PayTm import Checksum

from django.views.decorators.csrf import csrf_exempt

MERCHANT_KEY = 'nTVsy_ZkHny&WrG@'


from django.http import HttpResponse

def trial(request):
    products = Product.objects.all()
    return render(request,'shop/trial.html',{'product':products[:]})

def home(request):
    products = Product.objects.all()
    return render(request,'shop/home.html',{'products':products})

def qv(request,myid):
    product=Product.objects.filter(product_id=myid)

    return render(request,'shop/qv.html',{'product':product[:]})


def rate(request,myid):
    product=Product.objects.filter(product_id=myid)
    if request.method == "POST":
        fname = request.POST.get('fname', '')
        lname = request.POST.get('lname', '')
        mail = request.POST.get('mail', '')
        star = request.POST.get('star', '')
        comment = request.POST.get('comments', '')
        p_name= product[0]

        review = Product_Rating(prod_name=p_name,cust_fname=fname,cust_lname=lname,cust_email=mail,review=comment,star=star)
        review.save()
    getName = Product_Rating.objects.filter(prod_name=product[0])
    return render(request, 'shop/rate.html',{'getName':getName[:]})

def checkout(request):
    if request.method =="POST":
        fname = request.POST.get('fname','')
        lname = request.POST.get('lname','')
        address = request.POST.get('address','')
        city = request.POST.get('city','')
        state = request.POST.get('state','')
        zip_code = request.POST.get('zip_code','')
        phone1 = request.POST.get('phone1','')
        phone2 = request.POST.get('phone2','')
        items = request.POST.get('items','')
        amount = request.POST.get('amount','')
        mail=request.POST.get('mail','')

        order = Orders(fname=fname,lname=lname,
                       address=address,city=city,state=state,zip_code=zip_code,
                       phone1=phone1,phone2=phone2,cart_products=items,mail=mail,amount=amount)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()

        id=order.order_id
        alert=True
        # amount transfer through Paytm(user)
        param_dict={
            'MID': 'zEFdnn09256832651916',
            'ORDER_ID': str(order.order_id),
            'TXN_AMOUNT': str(amount),
            'CUST_ID': str(mail),
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL':'http://127.0.0.1:8000/handlerequest/',
        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return render(request,'shop/paytm.html',{'param_dict':param_dict})





        #return render(request,'shop/checkout.html',{'alert':alert,'id':id})

    return render(request,'shop/checkout.html')


@csrf_exempt
def handlerequest(request):
    return HttpResponse("hello World")














