from django.db import connection
from gestionhotel.models import *


def comprise_entre(chambre,date_d):

    with connection.cursor() as cursor:          

        req3 = f"""           
                SELECT * FROM gestionhotel_reservations WHERE gestionhotel_reservations.chambre_id = %s AND 
                %s BETWEEN gestionhotel_reservations.date_debut AND gestionhotel_reservations.date_fin
            """
        cursor.execute(req3,[chambre,date_d])
        resultat3 = cursor.fetchall() 
    return  resultat3




if __name__ == "__main__":
    pass