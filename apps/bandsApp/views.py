# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import *
import re
import bcrypt
from django.utils import timezone
from django.contrib import messages

# Display home page
def index (request) :  
    context = {}
    return render(request, 'bandsApp/index.html', context)

# Display all the bands by local artists. 
def artists (request) :  
    context = {}
    return render(request, 'bandsApp/artistsBands.html', context)

# Display all the bands by exclusive brands. 
def exclusives (request) :  
    context = {}
    return render(request, 'bandsApp/exclusiveBands.html', context)

# Display all the bands by charities. 
def cause (request) :  
    context = {}
    return render(request, 'bandsApp/charityBands.html', context)

# Display the search results 
def search (request) :  
    context = {}
    return render(request, 'bandsApp/searchResults.html', context)

# Display shopping cart 
def showCart (request, orderId) :  
    context = {'orderId':orderId}
    return render(request, 'bandsApp/shoppingCart.html', context)

# Edit shopping cart 
def editCart (request, orderId) :  
    context = {'orderId':orderId}
    return redirect(reverse('bands:cart'))



