from django.shortcuts import render,redirect
from . models import *
from django.contrib.auth.models import User
from django.db import connection
from datetime import timedelta,date
from .models import Chambres, Reservations
from gestionhotel.module import requete, comprise_entre, genere_random,convert_date
import random
from django.core.mail import send_mail,EmailMultiAlternatives
from django.template.loader import render_to_string




def index(request):
    context = {

        'chambre1' : Chambres.objects.filter(id_categorie=1),
        'chambre2' : Chambres.objects.filter(id_categorie = 2)
    }
    return render(request, 'gestionhotel/index.html',context )




def contact(request):


    if request.method =='POST':

        sujet = request.POST['sujet']
        name = request.POST['name']
        postnom = request.POST['postnom']
        email = request.POST['email']
        message = request.POST['ee']
        


        user_send_msg = Message.objects.create(
            sujet = sujet,
            nom = name,
            postnom = postnom,
            email = email,
            message = message
        )
    

        context={
            "sujet" : sujet,
            "message":message,
            "info": f'Mr/Md {name} {postnom}'
        }
        
        html_content = render_to_string("gestionhotel/email.html",context)

        subject = sujet
        msg = EmailMultiAlternatives(
            subject,
            message,
            email,
            ["pinhotelp@gmail.com"],
            headers={"List-Unsubscribe": "<mailto:www.pinhotel.com>"},
        )

        msg.attach_alternative(html_content, "text/html")
        msg.send()

        return redirect('gestionhotel:index')
    else:
        return render(request, 'gestionhotel/contact.html')





def about(request):
    return render(request, 'gestionhotel/about.html')





def services(request):
    return render(request, 'gestionhotel/services.html')


def galerie(request):
    return render(request, 'gestionhotel/galerie.html')



def album_deux(request):
    return render(request, 'gestionhotel/album2.html')

def album_one(request):
    return render(request, 'gestionhotel/album1.html')





















