# from fonctions import dupliquer_image, valeurs_pixels


#----- CHOIX DES FICHIERS DE TRAVAIL -----#
image_source = 'vinci.bmp'
image_finale = 'vinci_modifiee.bmp'

# image_source = 'joconde.bmp'
# image_finale = 'joconde_modifiee.bmp'



#----- CONVERSION ASCII --> DECIMALE -----#
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



#----- OUVERTURE FICHIER -----#
def ouvrir_fichier(image_source, octets_to_read=0):
    '''
    Ouvre un fichier, et retourne son contenu en type byte
    Penser à le convertir en bytearray pour modifier son contenu via bytearray()
    args :
        str image_source : Nom du fichier source et son extension
        int octets_to_read : Nombre total d'octets à lire. Si = 0 (par défaut), tout est lu
    return : 
        byte data : données contenu dans le fichier image_source
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



#----- CONTENU HEADER IMAGE -----#
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
    print("Taille du fichier: ", val_dec(infos[2:6]), "octets")
    print("Champ réservé :", val_dec(infos[6:10]))
    print("Offset de l'image :", val_dec(infos[10:14]))
    print("Largeur de l'image :", val_dec(infos[18:22]), "px")
    print("Hauteur de l'image :", val_dec(infos[22:26]), "px")

    print("Codage de la couleur:", val_dec(infos[28:30]), "couleur(s)")



#----- CONVERSION IMAGE EN ROUGE -----#
def vers_rouge(image_source = image_source, image_finale = image_finale):
    '''
    Convertit une image colorée en une image contant uniquement sa composante rouge.
    Le résultat est stockée dans image_finale 
    args :
        str image_source : nom et extension de l'image initiale 
        str image_finale : nom et extension de l'image finale. cette valeur sera le nom du fichier image
    return : 
        void
    '''
    datas = ouvrir_fichier(image_source)
    
    offset = val_dec(datas[10:14])
    datas = bytearray(datas) 

    for i in range(offset, len(datas), 3):
        datas[i] = 0
        datas[i+1] = 0
    
    fichier_final = open(image_finale, 'wb')
    fichier_final.write(datas)
    fichier_final.close()

vers_rouge()



#----- INVERSION D'IMAGE -----#
def inversion_image(image_source = image_source, image_finale = 'inversion.bmp'):
    '''
    Inverse les couleurs d'une image 
    Le résultat est stockée dans image_finale 
    args :
        str image_source : nom et extension de l'image initiale 
        str image_finale : nom et extension de l'image finale. cette valeur sera le nom du fichier image
    return : 
        void
    '''
    datas = ouvrir_fichier(image_source)
    
    offset = val_dec(datas[10:14])
    datas = bytearray(datas) 

    for i in range(offset, len(datas)):
        datas[i] = 255 - datas[i] 

    fichier_final = open(image_finale, 'wb')
    fichier_final.write(datas)
    fichier_final.close()

inversion_image()