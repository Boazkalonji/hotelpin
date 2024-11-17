from django.shortcuts import render
from django.shortcuts import redirect
from  django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
import hashlib
from django.core.mail import send_mail,EmailMultiAlternatives
from django.template.loader import render_to_string
from gestionhotel.models import *
from django.contrib.auth.models import User
from django.db import connection
from datetime import timedelta,date,datetime
from utilisateurs.module import requete, comprise_entre, genere_random,convert_date
import random



































NBR_TOUR = 6

@login_required(login_url = 'utilisateurs:login_users')
def delete_user(request,id):
    user = User.objects.get(pk = id)
    user.delete
    return redirect('utilisateurs:login_users')





def login_users(request):

    if request.method == 'POST':
        nom = request.POST['nom']
        mdp = request.POST['mdp']

        user = authenticate(request, username = nom, password = mdp)

        if user is not None:
            login(request, user)
            return redirect('gestionhotel:index')
        else:
           return render(request,'utilisateurs/erreur.html',{'user':user}) 
        
    return render(request,'utilisateurs/login.html') 


@login_required(login_url = 'utilisateurs:login_users')
def update_user_value(request,id):
    user = User.objects.get(id=id)
    return render(request,'utilisateurs/update_user.html',{'user':user})


@login_required(login_url = 'utilisateurs:login_users')
def update_user(request,id):
    if request.method == 'POST':

        nom = request.POST['nom']
        mdp = request.POST['mdp']
        postnom = request.POST['postnom']
        prenom = request.POST['prenom']
        email = request.POST['email']
        confirme_mdp = request.POST['confirme_mdp']

        

        if mdp == confirme_mdp:
            
            user = User.objects.get(id=id)

            if user is not None:
                user.username = nom
                user_mdp = make_password(mdp)
                user.password = user_mdp
                user.first_name = postnom
                user.last_name = prenom
                user.email = email
                user.save()
                return redirect('utilisateurs:login_users')

            
            return render(request,'utilisateurs/erreur.html')
        else:
            return HttpResponse('le mdp ne pas bien')    
    else:

        return render(request,'utilisateurs/update_user.html')


def sing_up(request):

    if request.method == 'POST':

        nom = request.POST['nom']
        mdp = request.POST['mdp']
        postnom = request.POST['postnom']
        prenom = request.POST['prenom']
        email = request.POST['email']


        if nom =='' or mdp =='' or postnom == '' or prenom == '' or email == '':
            return render(request,'utilisateurs/erreur.html')
        else:
            user = User.objects.create_user(username=nom, password=mdp)
            user.first_name = postnom
            user.last_name = prenom
            user.email = email

            user.save()

            subject = 'EMAIL DE CREATION COMPTE A PINHOTEL'
            message = 'Vous venez de creer un compte à pinhotel'
  

            html_content = render_to_string("utilisateurs/email.html",context={"message" : message})


            msg = EmailMultiAlternatives(
                subject,
                message,
                "pinhotelp@gmail.com",
                [email],
                headers={"List-Unsubscribe": "<mailto:www.pinhotel.com>"},
            )

            msg.attach_alternative(html_content, "text/html")
            msg.send()

            return redirect('utilisateurs:login_users')
    else:
        return render(request,'utilisateurs/sing_up.html')




@login_required(login_url = 'utilisateurs:login_users')
def logout_users(request):
    logout(request)
    return redirect('utilisateurs:login_users')




@login_required(login_url = 'utilisateurs:login_users')
def viewreservation(request,id):

    context = {

        'reservation':Reservations.objects.filter(user_id = id)
    }
    return render(request,'utilisateurs/viewreservation.html', context)







































































@login_required(login_url = 'utilisateurs:login_users')
def reservation(request,user_id,id_chambre):

    context = {

        'chambre' : id_chambre,
        'montant': Chambres.objects.get(id = id_chambre),
        'compte' : Comptes.objects.all()
    }



    if request.method == 'POST':
        user = request.POST['user_id']
        chambre = request.POST['chambre']
        compte = request.POST['compte']
        prix = request.POST['prix']
        date_debut = request.POST['date_debut']
        date_fin = request.POST['date_fin']
        num_compte = request.POST['num_compte']


        date_fin_c = convert_date.convert(date_fin)
        date_debut_c = convert_date.convert(date_debut)
        print(date_fin_c)
        print(date_debut_c)
        print(datetime.now())
        if datetime.now() > (date_fin_c) or datetime.now() > (date_debut_c):
            
            erreur_date_inf = {'erreur_date_inf': 'la date de debut ou de fin reservation doit etre superieur à la date actuelle'}
            return render(request, 'utilisateurs/reservation.html', erreur_date_inf)
        else:
            if date_fin < date_debut :
      
                mgs = {'mgs':'veuillez revoir les dates choisie surment la date fin est inferieur a la date debut '}
                return render(request, 'utilisateurs/reservation.html',mgs)
            else:
                req = requete.requete(date_debut,chambre)
                
                print(req)
            
                if req:
                    
                    with connection.cursor() as cursor2:
                        req2 = "SELECT * FROM gestionhotel_reservations  AS reservations WHERE reservations.date_debut  = %s"
                        cursor2.execute(req2,[date_debut])
                        resultat = cursor2.fetchall()


                        for i in resultat:
                            pass
                        
                        dd = i[1]
                        df = i[2]

                        durer = df-dd


                        text = {
                            'text': f" la chambre numero {chambre} est reserver deja pour une dure {durer} allant de {dd} à {df} tu peut reserver a partir de {df + timedelta(days=1)} ou choisir une autre chambre dans nos differente categorie Merci."
                        }
    
                    return render(request, 'utilisateurs/reservation.html',text)
                else:

                    req3 = comprise_entre.comprise_entre(chambre,date_debut)

                    if req3:
                        dd = date
                        df = date
                        for i in req3:
                            pass
                            dd = i[0]
                            df = i[1]



                        #print(text)
                        cxt_msg = {
                            'cxt_msg':f'il y a deja une reservation pour la date de {dd} à {df} veillez choisir une autre date à partir de {df + timedelta(1)}'
                        }
                        
                        #print(req3)
                        return render(request, 'utilisateurs/reservation.html',cxt_msg)
                    else:
                        reservation_user = Reservations.objects.create(
                            user_id = user,
                            compte_id = compte,
                            chambre_id = chambre,
                            date_debut = date_debut,
                            date_fin = date_fin,
                            num_compte = num_compte,
                            durer = convert_date.dure(date_debut,date_fin),
                            code_reservation = genere_random.code_rand())





                        subject = f'EMAIL DE RESERVATION CHAMBRE NUMERO {chambre}'
                        message = f'Vous venez de reserver la chambre {chambre} pour une dure de {convert_date.dure(date_debut,date_fin)} jour allant de {date_debut} à {date_fin}'
            

                        html_content = render_to_string("utilisateurs/rerservation_email.html",context={"message" : message})
                        user_id = int(user_id)
                        user_id= User.objects.get(id = user_id) 
                        email_user = user_id.email

                        msg = EmailMultiAlternatives(
                            subject,
                            message,
                            "pinhotelp@gmail.com",
                            [email_user],
                            headers={"List-Unsubscribe": "<mailto:www.pinhotel.com>"},
                        )

                        msg.attach_alternative(html_content, "text/html")
                        msg.send()
                        return redirect('gestionhotel:index')
        
    
    else:
        return render(request, 'utilisateurs/reservation.html', context)

