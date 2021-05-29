# from fonctions import dupliquer_image, valeurs_pixels

image_source = 'vinci.bmp'
image_finale = 'vinci_modifiee.bmp'

# image_source = 'joconde.bmp'
# image_finale = 'joconde_modifiee.bmp'


def val_dec(n_octets):
    '''
    Convertit un code ASCII en valeur décimale. 
    Ajouter b devant l'argument str n_octets
    arg : 
        b'str' n_octets : Code ASCII à convertir 
    return : 
        int result : code ASCII converti en valeur décimale
    '''
    result = 0
    for i in range(len(n_octets)):
        if i == 0:
            result += n_octets[i]
        else:
            result += n_octets[i] * 256**i

    return result


def ouvrir_fichier(image_source, octets_to_read=0):
    '''
    Si methode = rb (par défaut) ouverture en lecture binaire de image_source
    Si methode = wb ouverture en écriture binaire de image_source
    arg :
        str image_source : Nom du fichier et son extension
        int octets_to_read : Nombre total d'octets à lire. Si = 0, tout est lu
        str methode : ouverture en lecture : rb ; en écriture : wb
    return : 
        byte data : données du fichier image_source
    '''
    source = open(image_source, 'rb')
    
    # Lecture
    # Si il n'y a pas de valeurs spécifiques à lire 
    if octets_to_read == 0:
        data = source.read()
    else:
        data = source.read(octets_to_read)

    source.close()
    return data


def info_image(image=image_source): 
    '''
    Affiche les infos suivantes sur l'image donnée en argument : 
    signature, taille, champ reservé, offset, largeur et hauteur
    arg : 
        str image : nom et extension du fichier image source
    return : 
        void
    ''' 
    infos = ouvrir_fichier(image, octets_to_read=30)
    print('------', image, '------')
   
    print("Signature : ", infos[0:2])
    print("Taille du fichier: ", val_dec(infos[2:6]), "octets (", infos[2:6], ")")
    print("Champ réservé :", val_dec(infos[6:10]), " (", infos[6:10], ")")
    print("Offset de l'image :", val_dec(infos[10:14]), " (", infos[10:14], ")")
    print("Largeur de l'image :", val_dec(infos[18:22]), "px (", infos[18:22], ")")
    print("Hauteur de l'image :", val_dec(infos[22:26]), "px (", infos[22:26], ")")

    print("Codage de la couleur:", val_dec(infos[28:30]), "couleur(s) (", infos[28:30], ")")

info_image(image_source) 

# valeurs_pixels(image_source = image_source, valeur_a_afficher=[0, 0])

def vers_rouge(image_source = image_source, image_finale = image_finale):
    '''
    Convertit une image colorée en une image contant unique la composant rouge 
    args :
        str image_source : nom et extension de l'image initiale 
        str image_finale : nom et extension de l'image initiale. cette valeur sera le nom du fichier image
    return : 
        void
    '''
    datas = ouvrir_fichier(image_source)
    
    offset = val_dec(datas[10:14])
    datas = bytearray(datas) #conversion de type pour travailler avec un type de données modifiable

    for i in range(offset, len(datas), 3):
        datas[i] = 0
        datas[i+1] = 0
    
    print(i+(3*offset))
    destination=open(image_finale, 'wb')
    destination.write(datas)
    destination.close()


vers_rouge(image_source)
info_image(image_finale)

