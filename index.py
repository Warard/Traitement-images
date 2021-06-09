# from fonctions import dupliquer_image, valeurs_pixels



#----- CHOIX DES FICHIERS DE TRAVAIL -----#
image_source = 'assets/source/vinci.bmp'
image_finale = 'assets/source/vinci_modifiee.bmp'

# image_source = 'assets/source/joconde.bmp'
# image_finale = 'assets/source/joconde_modifiee.bmp'



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
def vers_rouge(image_source = image_source, image_finale = 'assets/result/rouge.bmp'):
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

# vers_rouge()



#----- INVERSION D'IMAGE -----#
def inversion_image(image_source = image_source, image_finale = 'assets/result/inversion.bmp'):
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

# inversion_image()



#----- NOIR ET BLANC -----#
def noir_et_blanc(image_source = image_source, image_finale = 'assets/result/NeB.bmp'):
    '''
    Transforme une image colorée en une image en noir et blanc 
    Le résultat est stockée dans image_finale 
    args :
        str image_source : nom et extension de l'image initiale 
        str image_finale : nom et extension de l'image finale. cette valeur sera le nom du fichier image
    return : 
        void
    '''
    datas = ouvrir_fichier(image_source)
    datas = bytearray(datas)

    offset = val_dec(datas[10:14])
    
    for i in range(offset, len(datas)):
        r = val_dec(datas[i+2:i+3])
        v = val_dec(datas[i+1:i+2])
        b = val_dec(datas[i:i+1])

        m = (r+v+b) // 3

        datas[i] = m 

    fichier_final = open(image_finale, 'wb')
    fichier_final.write(datas)
    fichier_final.close()

# noir_et_blanc() 



#----- MONOCHROME -----#
def monochrome(seuil, niveau1, niveau2, image_source = 'assets/result/NeB.bmp', image_finale = 'assets/result/monochrome.bmp'):
    '''
    Transforme une image en noir et blanc 3 couleurs, en une image monochrome 
    Le résultat est stockée dans image_finale 
    args :
        str image_source : nom et extension de l'image initiale (doit-être en noir et blanc)
        str image_finale : nom et extension de l'image finale. cette valeur sera le nom du fichier image
    return : 
        void
    '''
    datas = ouvrir_fichier(image_source)
    datas = bytearray(datas)

    offset = val_dec(datas[10:14])
    
    for i in range(offset, len(datas)):
        r = val_dec(datas[i+2:i+3])
        v = val_dec(datas[i+1:i+2])
        b = val_dec(datas[i:i+1])

        if r < seuil:
            r = niveau1
        else:
            r = niveau2
        datas[i] = r

        if v < seuil:
            v = niveau1
        else:
            v = niveau2
        datas[i] = v

        if b < seuil:
            b = niveau1
        else:
            b = niveau2
        datas[i] = b


    fichier_final = open(image_finale, 'wb')
    fichier_final.write(datas)
    fichier_final.close()

# monochrome(seuil = 90, niveau1 = 50, niveau2 = 180)



#----- ROTATION 180 -----#
def rotation_180(image_source = image_source, image_finale = 'assets/result/180.bmp'):
    '''
    Fais une rotation de 180 degrés de l'image source, et stocke le résultat dans image finale
    args :
        str image_source : nom et extension de l'image initiale 
        str image_finale : nom et extension de l'image finale. cette valeur sera le nom du fichier image
    return : 
        void
    '''
    datas = ouvrir_fichier(image_source)

    hauteur = val_dec(datas[22:26])
    largeur = val_dec(datas[18:22])
    offset = val_dec(datas[10:14])
    
    # Données de l'image finale ; ici, ajout du header provenant de l'image source 
    datas_dest = bytearray(datas[0:offset])
    
    # On réouvre le fichier source de manière à utiliser .seek pour lire ses lignes
    src = open(image_source, 'rb')

    # Initialisation de la variable qui contiendra les copies des lignes
    ligne = []


    for i in range(1, hauteur+1):
        # Parcours les lignes unes à une en partant de la fin et les stocke (partir de la fin permet de faire la rotation)
        src.seek(offset + ((hauteur - i)*largeur)*3)
        ligne = src.read(largeur*3)

        # Ecris les lignes unes à unes
        for k in range(len(ligne)):
            datas_dest.append(ligne[k])

        

    fichier_final = open(image_finale, 'wb')
    fichier_final.write(datas_dest)
    fichier_final.close()

# rotation_180() 



#----- ROTATION MIROIR -----#
def miroir(image_source = image_source, image_finale = 'assets/result/miroir.bmp'):
    '''
    Fais un effet miroir sur l'image source et stocke le résultat dans l'image finale
    args :
        str image_source : nom et extension de l'image initiale 
        str image_finale : nom et extension de l'image finale. cette valeur sera le nom du fichier image
    return : 
        void
    '''
    datas = ouvrir_fichier(image_source)

    hauteur = val_dec(datas[22:26])
    largeur = val_dec(datas[18:22])
    offset = val_dec(datas[10:14])
    
    # Données de l'image finale ; ici, ajout du header provenant de l'image source 
    datas_dest = bytearray(datas[0:offset])
    
    # On réouvre le fichier source de manière à utiliser .seek pour lire ses lignes
    src = open(image_source, 'rb')

    # Initialisation de la variable qui contiendra les copies des lignes
    ligne = bytearray()

    # Parcours toute la hauteur de l'image
    for i in range(hauteur):
        # Parcours les lignes unes à une en partant de la fin et les stocke (partir de la fin permet de faire la rotation)
        src.seek(offset+(i*largeur*3))
        ligne = src.read(largeur*3)

        # Ecris les lignes unes à unes, en partant de la fin via le sclicing
        for k in range(0, len(ligne), 3):
            # print(k)
            datas_dest.append(ligne[::-1][k+2])  #bleu
            datas_dest.append(ligne[::-1][k+1])  #vert
            datas_dest.append(ligne[::-1][k])    #rouge  

    print(len(datas_dest))
    fichier_final = open(image_finale, 'wb')
    fichier_final.write(datas_dest)
    fichier_final.close()

