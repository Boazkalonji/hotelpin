import random
import hashlib

NBR_TOUR = 6


def code_rand():

    code = ""

    for _ in range(NBR_TOUR):
        nbr_alea = random.randint(0,9)
        nbr_alea = str(nbr_alea)
        code += nbr_alea 
        
    return code



code_genere = code_rand()





def hashage():
    en_code = code_genere.encode()
    code_chiiffre = hashlib.sha1(en_code)
    code_chiiffre = code_chiiffre.hexdigest()

    return code_chiiffre






if __name__ == "__main__":
    pass
    