import random
import hashlib

NBR_TOUR = 6


def code_rand(nombre_tour):

    code = ""

    for _ in range(nombre_tour):
        nbr_alea = random.randint(0,9)
        nbr_alea = str(nbr_alea)
        code += nbr_alea 
        
    return code







if __name__ == "__main__":
    rander = code_rand(NBR_TOUR)
    print(rander)
    