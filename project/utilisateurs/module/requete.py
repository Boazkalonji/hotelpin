from django.db import connection
from gestionhotel.models import *

def requete(date_debut,chambre):

    with connection.cursor() as cursor:
        req = f"""
        
                SELECT * FROM gestionhotel_reservations WHERE gestionhotel_reservations.date_debut = %s AND gestionhotel_reservations.chambre_id = %s
          
            """
        cursor.execute(req,[date_debut,chambre])
        resultat = cursor.fetchall()
    return resultat





if __name__ == "__main__":
    req = requete('2024-01-01',2)