import qrcode
import hashlib

def genereQrcode(text):
    path_image = 'imgqrcode/image.png'
    rq_genere = qrcode.make(text)
    rq_genere.save(path_image)

    return 


