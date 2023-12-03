from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth import login, logout, authenticate, forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.template.loader import render_to_string
import uuid  # for generating unique tokens
from django.urls import reverse
# Create your views here.


# Home Paths
def base_index(request):
    return render(request, 'base_index.html')
def page_links(request):
    return render(request, 'page_links.html')
# Other Paths
def blank(request):
    return render(request, 'blank.html')
def checkout(request):
    return render(request, 'checkout.html')

def all_stores(request):
    return render(request, 'all_stores.html')
def all_products(request):
    return render(request, 'all_products.html')
# #######################    Customer login Setup    ###################################################################
# user registration
def signup(request):
    return render(request, 'signup.html')
def signup_customer(request):
    try:
        if request.method == 'POST':
            username = request.POST.get("username")
            password = request.POST.get("password")
            email = request.POST.get("email")
            phone = request.POST.get("phone_no")
            address = request.POST.get("customer_address")

            s = customer.objects.create(username=username, password=password, email=email, phone=phone, address=address)
            s.save()

            # You can also set additional user attributes here if needed
            message = "Successfully Created Account. Login now !"
            return render(request, "login.html", {'message': message})
        else:
            error_message = "Username or Password already exist. Please try again...!"
            return render(request, "signup.html", {'error_message': error_message})

    except:
        error_message = "Please enter the details!"
        return render(request, 'signup.html', {'error_message': error_message})
# user Login
def login_user(request):
    return render(request, 'login.html')
def my_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            profile = customer.objects.get(username=username, password=password)
            if profile and profile.password != "":
                customer_id = profile.customer_id
                return redirect('index', customer_id=customer_id)

            else:
                # Return an 'invalid login' error message.
                error_message = "Invalid username or password. Please try again."
                return render(request, 'login.html', {'error_message': error_message})


        except:
            error_message = "Please enter the details!"
            return render(request, 'login.html', {'error_message': error_message})


    else:
        error_message = "Please enter the details!"
        return render(request, 'login.html', {'error_message': error_message})
def index(request, customer_id):
    customer_id = int(customer_id)
    profile = customer.objects.filter(customer_id=customer_id)
    product = product_s.objects.all()
    return render(request, 'index.html', {'profile': profile, 'product': product,'customer_id':customer_id})
def back_home(request, customer_id):
    return redirect('index', customer_id=customer_id)
def back_home1(request, customer_id,product_id):
    return redirect('index', customer_id=customer_id)
# logout Setup
def logout_view(request):
    # logout(request)
    return render(request, 'base_index.html')
########################################################################################################################


# ######################## Supplier login Setup ########################################################################
# Supplier registration
def supplier_portal(request):
    return render(request, 'supplier_portal.html')
def signup_supplier(request):
    try:
        if request.method == 'POST':
            username = request.POST.get("username")
            password = request.POST.get("password")
            email = request.POST.get("email")
            phone = request.POST.get("phone_no")
            gstin = request.POST.get("gstin")
            shop_name = request.POST.get("shop_name")
            address = request.POST.get("shop_address")
            aadhar = request.POST.get("aadhar_no")
            s = supplier.objects.create(username=username, password=password, email=email, phone=phone, gstin=gstin, shop_name=shop_name, address=address, aadhar=aadhar)
            s.save()

            message = "Successfully Created Account. Login now !"
            return render(request, "supplier_login.html", {'message': message})
        else:
            error_message = "Username or Password already exist. Please try again...!"
            return render(request, "supplier_portal.html", {'error_message': error_message})

    except:
        error_message = "Please enter the details!"
        return render(request, 'supplier_portal.html', {'error_message': error_message})
# supplier login
def supplier_login(request):
    return render(request, 'supplier_login.html')
def supplier_view(request):
            if request.method == 'POST':
                username = request.POST["username"]
                password = request.POST["password"]
                try:
                    s = supplier.objects.get(username=username, password=password)

                    if s and s.password != "":

                        return render(request, 'supplier_panel.html', {'s': s})
                    else:
                        error_message = "Invalid username or password. Please try again."
                        return render(request, 'supplier_login.html', {'error_message': error_message})

                except supplier.DoesNotExist:
                    error_message = "Invalid username or password. Please try again."
                    return render(request, 'supplier_login.html', {'error_message': error_message})
            else:
                # Return an 'invalid login' error message.
                error_message = "Invalid username or password. Please try again."
                return render(request, 'supplier_login.html', {'error_message': error_message})
########################################################################################################################


# ########################     Admin login Setup     ###################################################################
# Admin registration
def admin_portal(request):
    return render(request, 'admin_portal.html')
def signup_admin(request):
    try:
        if request.method == 'POST':
            username = request.POST.get("username")
            password = request.POST.get("password")
            email = request.POST.get("password")

            s = thestore_admin.objects.create(username=username, password=password, email=email)
            s.save()
            message = "Successfully Created Account. Login now !"
            return render(request, "admin_login.html", {'message': message})
        else:
            error_message = "Username or Password already exist. Please try again...!"
            return render(request, "admin_portal.html", {'error_message': error_message})
    except:
        error_message = "Please enter the details!"
        return render(request, 'admin_portal.html', {'error_message': error_message})
# Admin login
def admin_login(request):
    return render(request, 'admin_login.html')
def admin_view(request):
    try:
        if request.method == 'POST':
            username = request.POST["username"]
            password = request.POST["password"]
            try:
                d = thestore_admin.objects.get(username=username)
                if d.password == password and d.password != "":
                    return render(request, 'admin_panel.html')
                else:
                    error_message = "Invalid username or password. Please try again."
                    return render(request, 'admin_login.html', {'error_message': error_message})
            except:
                error_message = "Invalid username or password. Please try again."
                return render(request, 'admin_login.html', {'error_message': error_message})

        else:
            # Return an 'invalid login' error message.
            error_message = "Invalid username or password. Please try again."
            return render(request, 'admin_login.html', {'error_message': error_message})
    except:
        error_message = "Please enter the details!"
        return render(request, 'admin_login.html', {'error_message': error_message})
########################################################################################################################


# ################################# contact method for feedback ########################################################
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)


        if form.is_valid():
            # Process the form data
            form.save()
            # Send email
            subject = 'Thank you for contacting us'
            message = 'We received your message and will get back to you soon.'
            from_email = 'rahuldevkalady@gmail.com'
            recipient_list = [form.cleaned_data['email']]

            send_mail(subject, message, from_email, recipient_list)

            response = "Thank You...!"

            # Redirect or show a success message
            return render(request,  'contact.html', {'response': response})
        else:
            return HttpResponse("Error")
    else:
        form = ContactForm()
        return render(request, 'contact.html', {'form': form})
# feedback message view
def messages_view(request):
    # Retrieve data from the Message model
    m = Message.objects.all()
    # Pass the data to the template
    return render(request, 'messages.html', {'messages': m})
########################################################################################################################


# ################### Supplier Panel######### ##########################################################################
# Create Product
def create_product(request, supplier_id):

    if request.method == 'POST':

        form = CreateProduct(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            response = "Successfully Added...!"
            s = supplier.objects.get(pk=supplier_id)
            return render(request, 'create_product.html', {'response': response,'s':s})
        else:
            print(form.errors)
            return HttpResponse("Error")
    else:
        s = supplier.objects.get(pk=supplier_id)
        form = CreateProduct()
        return render(request, 'create_product.html', {'form': form, 's':s})
# View Products
def products_by_supplier(request, supplier_id):
    s = supplier.objects.get(pk=supplier_id)
    p = product_s.objects.filter(supplier_id=s)



    context = {
        'supplier': s,
        'products': p,

    }

    return render(request, 'product_by_supplier.html', context)
# Delete product
def delete_product(request, product_id):
    p = product_s.objects.filter(product_id=product_id)
    p.delete()
    return HttpResponse("Deleted")
########################################################################################################################
# Customer panel
def profile(request, customer_id):
    p = customer.objects.get(customer_id=customer_id)
    print(p)
    return render(request, 'profile.html', {'p': p})
def profile1(request, customer_id,product_id):
    return redirect('profile',customer_id=customer_id)
def Account_Dashboard(request, customer_id):
    p = customer.objects.get(customer_id=customer_id)
    print(p)
    return render(request, 'Account_Dashboard.html', {'p': p})
def edit_customer_details(request, customer_id):
    profile = get_object_or_404(customer, customer_id=customer_id)
    if request.method == "POST":
        form = edit_customer_form(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            p = customer.objects.get(customer_id=customer_id)
            return render(request, 'Account_Dashboard.html', {'p': p})
            # return render(request, 'edit_customer_details.html', {'form': form, 'profile': profile})
        else:
            form = edit_customer_form(instance=profile)
            return render(request, 'edit_customer_details.html', {'form': form, 'profile': profile})
    else:
        form = edit_customer_form(instance=profile)
        return render(request, 'edit_customer_details.html', {'form': form, 'profile': profile})
def view_product(request, customer_id, product_id):

    customer_id =int(customer_id)
    p2 = product_s.objects.all()
    product = get_object_or_404(product_s, product_id=product_id)
    print(product)
    return render(request, 'product.html',{'product': product, 'customer_id': customer_id, 'p2': p2})
def view_cart(request, customer_id):
    profile = customer.objects.get(customer_id=customer_id)
    try:
        # Try to get an existing cart associated with the customer
        c = cart.objects.get(customer_id=profile)
        print(c)

    except cart.DoesNotExist:
        # If the cart does not exist, create a new one
        c = cart.objects.create(customer_id=profile)
        c.save()
    # Perform any additional logic or data retrieval needed before rendering the cart page
    items = cart_item.objects.filter(cart=c)

    t=0
    total_price=0
    for i in items:
        if i.cart.customer_id == profile:
            total_price = total_price+i.product_id.price
            t=t+total_price
        else:
            pass
    print(profile)
    print(items)
    return render(request, 'cart.html', {'profile': profile, 'cart': c, 'items': items,'total_price':t})
def view_cart1(request,customer_id,product_id):
    return redirect('view_cart',customer_id=customer_id)
def add_to_cart(request,customer_id,product_id):
    profile = customer.objects.get(customer_id=customer_id)
    cart_object = cart.objects.get(customer_id=profile)
    product = product_s.objects.get(product_id=product_id)
    c = cart_item.objects.create(cart=cart_object,product_id=product)
    c.save()
    return redirect('view_cart',customer_id=customer_id)
def remove_from_cart(request,customer_id,product_id):
    profile = customer.objects.get(customer_id=customer_id)
    cart_object = cart.objects.get(customer_id=profile)
    product = product_s.objects.get(product_id=product_id)
    c = cart_item.objects.filter(cart=cart_object, product_id=product)
    c.delete()
    return redirect('view_cart', customer_id=customer_id)
def product_category(request,customer_id):
    a = product_s.objects.all()[0:6:2]
    c = product_s.objects.all()
    for i in c:
        print(i.category_id)
    b = category.objects.all()
    return render(request, 'product_category.html',{'a':a,'b':b,'c':c})
def product_category_by_id(request):
    c=category.objects.filter(category_id=1)
    print(c)
    for i in c:
        print(i.category_id)
    return render(request, 'product_category_by_id.html',{'c':c})
