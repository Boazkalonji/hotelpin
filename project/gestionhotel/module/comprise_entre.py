from django.db import connection
from gestionhotel.models import *


def comprise_entre(date_debut,date_fin):

    with connection.cursor() as cursor:          

        req3 = f"""           
                SELECT reservations.date_debut, reservations.date_fin,Chambres.*
                FROM gestionhotel_reservations AS reservations
                INNER JOIN 
                gestionhotel_chambres AS chambres
                ON reservations.chambre_id = chambres.id 
                WHERE
                ( %s OR %s BETWEEN reservations.date_debut AND reservations.date_fin)
          
            """
        cursor.execute(req3,[date_debut,date_fin])
        resultat3 = cursor.fetchall() 
    return  resultat3




if __name__ == "__main__":
    req = comprise_entre('2024-01-01','2024-01-5')