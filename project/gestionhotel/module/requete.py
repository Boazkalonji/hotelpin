from django.db import connection
from gestionhotel.models import *

def requete(date_debut,chambre):

    with connection.cursor() as cursor:
        req = f"""
                SELECT Reservations.*,Chambres.* 
                FROM gestionhotel_reservations AS reservations
                INNER JOIN 
                gestionhotel_chambres AS chambres
                ON reservations.chambre_id = chambres.id  
                WHERE (reservations.date_debut = %s AND chambres.id = %s) 
          
            """
        cursor.execute(req,[date_debut,chambre])
        resultat = cursor.fetchall()
    return resultat





if __name__ == "__main__":
    req = requete('2024-01-01',2)