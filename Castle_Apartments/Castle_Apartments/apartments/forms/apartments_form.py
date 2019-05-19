from django.forms import ModelForm, widgets
from django import forms
from apartments.models import Apartment

#TODO: FIX HERE
# some widgets could be changed to select, number...
class ApartmentSellForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        apartmentTypes = (('fjolbyli', 'Fjölbýli'), ('einbyli', 'Einbýli'))
        zipCode = (('zip', 101), ('zip', 102), ('zip', 103), ('zip', 104), ('zip', 105), ('zip', 107), ('zip', 108), ('zip', 109), ('zip', 110), ('zip', 111), ('zip', 112), ('zip', 113), ('zip', 116), ('zip', 121), ('zip', 123), ('zip', 124), ('zip', 125), ('zip', 127), ('zip', 128), ('zip', 129), ('zip', 130),
                   ('zip', 132), ('zip', 150), ('zip', 170), ('zip', 172), ('zip', 190), ('zip', 200), ('zip', 201), ('zip', 202), ('zip', 203), ('zip', 210), ('zip', 212), ('zip', 220), ('zip', 221), ('zip', 222), ('zip', 225), ('zip', 230), ('zip', 232), ('zip', 233), ('zip', 235), ('zip', 240), ('zip', 245),
                   ('zip', 250), ('zip', 260), ('zip', 270), ('zip', 271), ('zip', 276), ('zip', 300), ('zip', 301), ('zip', 302), ('zip', 310), ('zip', 311), ('zip', 320), ('zip', 340), ('zip', 345), ('zip', 350), ('zip', 355), ('zip', 356), ('zip', 360), ('zip', 370), ('zip', 371), ('zip', 380), ('zip', 400),
                   ('zip', 401), ('zip', 410), ('zip', 415), ('zip', 420), ('zip', 425), ('zip', 430), ('zip', 450), ('zip', 451), ('zip', 460), ('zip', 465), ('zip', 470), ('zip', 471), ('zip', 500), ('zip', 510), ('zip', 512), ('zip', 520), ('zip', 524), ('zip', 530), ('zip', 531), ('zip', 540), ('zip', 545),
                   ('zip', 550), ('zip', 560), ('zip', 565), ('zip', 565), ('zip', 570), ('zip', 580), ('zip', 600), ('zip', 601), ('zip', 602), ('zip', 603), ('zip', 610), ('zip', 611), ('zip', 620), ('zip', 621), ('zip', 625), ('zip', 630), ('zip', 640), ('zip', 641), ('zip', 645), ('zip', 650), ('zip', 660),
                   ('zip', 670), ('zip', 671), ('zip', 675), ('zip', 680), ('zip', 681), ('zip', 685), ('zip', 690), ('zip', 700), ('zip', 701), ('zip', 710), ('zip', 715), ('zip', 720), ('zip', 730), ('zip', 735), ('zip', 740), ('zip', 750), ('zip', 755), ('zip', 760), ('zip', 765), ('zip', 780), ('zip', 781),
                   ('zip', 785), ('zip', 800), ('zip', 801), ('zip', 802), ('zip', 810), ('zip', 815), ('zip', 816), ('zip', 820), ('zip', 825), ('zip', 840), ('zip', 845), ('zip', 850), ('zip', 851), ('zip', 860), ('zip', 861), ('zip', 870), ('zip', 871), ('zip', 880), ('zip', 900), ('zip', 902))
        model = Apartment
        exclude = [ 'id', 'owner' ]
        widgets = {
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'zip_code': widgets.Select(attrs={'class': 'form-control'}, choices=zipCode),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'size': widgets.NumberInput(attrs={'class': 'form-control'}),
            'rooms': widgets.NumberInput(attrs={'class': 'form-control'}),
            'type': widgets.Select(attrs={'class': 'form-control'}, choices=apartmentTypes)
        }
