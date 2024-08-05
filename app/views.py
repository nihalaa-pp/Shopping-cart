from django.shortcuts import render, redirect
from django.db.models import Count
from django.views import View
from .models import Product, Cart
from .forms import  CustomerRegistrationForm,CustomerProfileForm
from  django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from .models import ProductVariant, Cart
from django.http import JsonResponse
from django.db.models import Q




# Create your views here.
def home(request):
     return render(request,"app/home.html")

def about(request):
     return render(request,"app/about.html")

def contact(request):
     return render(request,"app/contact.html")


class CategoryView(View):
     def get(self,request,val):
          product = Product.objects.filter(category=val)
          title  = Product.objects.filter(category=val).values('title')
          return render(request,"app/category.html",locals())
     
class ProductDetail(View):
     def get(self,request,pk):
          product = Product.objects. get(pk=pk)
          return render(request,"app/productdetail.html",locals())     
     
class CategoryTitle(View):
     def get(self,request,val):
          product = Product.objects.filter(title=val)
          title = Product.objects.filter(category=product[0].category).values('title')
          return render(request,'app/category.html',locals())

class CustomerRegistrationView(View):
     def get(self, request):
          form = CustomerRegistrationForm()
          return render(request, 'app/customerregistration.html', locals())
     
     def post(self, request): 
          form = CustomerRegistrationForm(request.POST)
          if form.is_valid():
               form.save()
               messages.success(request, 'Congratulations! User registered successfully')
               return redirect('home')  # Redirect to the home page or any other page
          else:
               messages.warning(request, 'Invalid input data')
          return render(request, 'app/customerregistration.html', locals())
     
class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        context = {
            'form': form
        }
        return render(request, 'app/profile.html', context)

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('profile')
        else:
            messages.error(request, 'Error updating profile')
        context = {
            'form': form
        }
        return render(request, 'app/profile.html', context)
    


# views.py

from django.shortcuts import redirect
from django.urls import reverse

def add_to_cart(request):
    user=request.user
    product_id=request.GET.get('prod_id')
    product = product.objects.get(id=product_id)
    Cart(user=user,product=product).save()
    return redirect('/cart')
 
def show_cart(request):
     user = request.user
     cart = Cart.objects.filter(user=user)
     amount = 0
     for p in cart:
          value = p.quantity * p.product.discounted_price
          amount = amount + value
     totalamount = amount+40     
     return render(request, 'app/addtocart.html',locals()) 

def plus_cart(request):
     if request.method =='GET':
          prod_id=request.GET['prod_id'] 
          print(prod_id)
          c= Cart.objects.get(Q(Product=prod_id)&Q(user=request.user))
          c.quantity+=1
          c.save()
          user = request.user
          cart = Cart.objects.filter(user=user)
          amount = 0
          for p in cart:
               value= p.quantity * p.product.discounted_price
               amount = amount+value
          totalamount = amount+ 40     
          data={
               'quantity':c.quantity,
               'amount':amount,
               'totalamount':totalamount


          }
          return JsonResponse(data)

          
          