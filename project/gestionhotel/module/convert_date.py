import datetime




def dure(date_debut,date_fin):

    format_date = "%Y-%m-%d"
    
    date_debut_format = datetime.datetime.strptime(date_debut,format_date)
    date_fin_format = datetime.datetime.strptime(date_fin,format_date)

    date_debut = datetime.datetime(date_debut_format.year,date_debut_format.month, date_debut_format.day)
    date_fin = datetime.datetime(date_fin_format.year,date_fin_format.month, date_fin_format.day)
                        
    resultat = date_fin - date_debut
    dure = resultat.days

    return int(dure)



if __name__ == "__main__":
    pass