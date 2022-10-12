from listings.models import *
from django.shortcuts import render, redirect
from listings.forms import ContactUsForm, BandForm, ListingForm
from django.core.mail import send_mail


def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands})


def band_detail(request, band_id):
    band = Band.objects.get(id=band_id)
    return render(request, 'listings/band_detail.html', {'band': band})


def listing_list(request, band_id):
    band = Band.objects.get(id=band_id)
    return render(request, 'listings/listing_list.html', {'band': band})


def listing_detail(request, band_id, listing_id):
    listing = Listing.objects.get(id=listing_id)
    return render(request, 'listings/listing_detail.html', {'listing': listing})


def contact(request):
    # si c'est une requete POST on crée un formulaire avec les données renseigné
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f'Message de {form.cleaned_data["name"] or "anonyme"}',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.com']
            )
            return redirect('/email-send-success/')
    # si c'est une requete GET on crée un formulaire vide
    else:
        form = ContactUsForm()
    return render(request, 'listings/contact.html', {'form': form})


def email_send(request):
    return render(request, 'listings/email_send.html')


def about(request):
    return render(request, 'listings/about')


def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm()
    return render(request, 'listings/band_create.html', {'form': form})


def band_update(request, band_id):
    band = Band.objects.get(id=band_id)
    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            form.save()
            return redirect('band-detail', band_id)
    else:
        form = BandForm(instance=band)
    return render(request, 'listings/band_update.html', {'form': form})


def band_delete(request, band_id):
    band = Band.objects.get(id=band_id)
    if request.method == 'POST':
        band.delete()
        return redirect('band-list')
    return render(request, 'listings/band_delete.html', {'band': band})

def listing_create(request, band_id):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save()
            return redirect('listing-detail', band_id, listing.id)
    else:
        form = ListingForm()
    return render(request, 'listings/listing_create.html', {'form': form})

def listing_update(request, band_id, listing_id):
    listing = Listing.objects.get(id=listing_id)
    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            return redirect('listing-detail', band_id, listing_id)
    else:
        form = ListingForm(instance=listing)
    return render(request, 'listings/listing_update.html', {'form': form})

def listing_delete(request, band_id, listing_id):
    listing = Listing.objects.get(id=listing_id)
    if request.method == 'POST':
        listing.delete()
        return redirect('listing-list', band_id)
    return render(request, 'listings/listing_delete.html', {'listing': listing})
