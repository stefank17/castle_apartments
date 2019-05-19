from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from apartments.forms.apartments_form import ApartmentSellForm
from apartments.models import ApartmentImage, Apartment
from users.models import ViewingHistory

def index(request):
    if 'search_filter' in request.GET or 'type' in request.GET or 'rooms' in request.GET or 'zip' in request.GET or 'address_order' in request.GET:
        # get the values of the query variables
        search_filter = request.GET['search_filter']
        rooms = request.GET['rooms']
        type = request.GET['type']
        zip = request.GET['zip']
        address_order = request.GET['address_order']
        price_order = request.GET['price_order']
        date_order = request.GET['date_order']

        # make ordering by default order -price, highest fyrst
        if address_order != 'Not_selected':
            ordering = address_order
        elif price_order != 'Not_selected':
            ordering = price_order
        elif date_order != 'Not_selected':
            ordering = date_order
        else:
            ordering = '-price'

        apartments = [ {
            'id': x.id,
            'address': x.address,
            'price': x.price,
            'description': x.description,
            'type': x.type,
            'rooms': x.rooms,
            'zip': x.zip_code,
            'time_added': x.time_added,
            'size': x.size,
            'firstimage': Apartment.objects.get(id=x.id).apartmentimage_set.first().image
        } for x in Apartment.objects.filter(address__icontains=search_filter).filter(type__contains=type).filter(rooms__contains=rooms).filter(zip_code__contains=zip).order_by(ordering) ]
        return JsonResponse({'data': apartments})
    expression = '-price'
    context = {'apartments': Apartment.objects.all().order_by(expression)}
    return render(request, 'apartments/index.html', context)

# @login_required
def get_apartment_by_id(request, id):
    return render(request, 'apartments/apartment_details.html', {
        'apartment': get_object_or_404(Apartment, pk=id)
    })

# later used when login func. is working
@login_required
def sell_apartment(request):
    if request.method == 'POST':
        # form created, from apartents_form, to be used in html
        form = ApartmentSellForm(data=request.POST)
        if form.is_valid():
            apartment = form.save(commit=False)
            apartment.owner_id = request.user.id
            apartment.save()
            apartment_image = ApartmentImage(id=None, image=request.POST['image'], apartment_id=apartment.id)
            apartment_image.save()
            return redirect('index')
    else:
        form = ApartmentSellForm()
    return render(request, 'apartments/sell_apartment.html', {
        'form': form
    })

# @login_required
def get_apartment_by_id(request, apartment_id):
    if request.user.is_authenticated:
        history = ViewingHistory(id=None, time=None, apartment_id=apartment_id, user_id=request.user.id)
        history.save()
    return render(request, 'apartments/apartment_details.html', {
        'apartment': get_object_or_404(Apartment, pk=apartment_id)
    })

# Loading the purchase form
def purchase_apartment(request, id):
    return render(request, 'apartments/purchase.html', {
        'apartment': get_object_or_404(Apartment, pk=id)
    })

# Deleting apartment
def delete_apartment(request, id):
    apartment = get_object_or_404(Apartment, pk=id)
    apartment.delete()
    return redirect('index')
