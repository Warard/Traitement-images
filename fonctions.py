# from index import image_source, val_dec, ouvrir_fichier
image_source = 'vinci.bmp'
image_finale = 'vinci_modifiee.bmp'

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


def dupliquer_image(image_finale, image_source = image_source, octets_a_dupliquer=[0, 0]):
    '''
    Duplique une image, et créé un nouveau fichier image dans le dossier local courant
    arg : 
        str image_source : nom et extension du fichier source à dupliquer
        str image_finale : nom et extension du fichier qui contiendra la duplication
        list octets_a_dupliquer : djébut et fin des octets à dupliquer. Si vaut [0, 0] tout est recopié
    return : 
        byte image_finale : image contenant la duplication de l'image source
    '''

    # Ouverture image source en lecture binaire 
    image_src = ouvrir_fichier(image_source)

    hauteur = val_dec(image_src[22:26])
    largeur = val_dec(image_src[18:22])
    
    offset = val_dec(image_src[10:14])

    # Ouveture image source en écriture binaire
    image_fnl = open(image_finale, 'wb')
    
    # Dupliquer toute l'image
    if octets_a_dupliquer == [0, 0]:
        image_fnl.write(image_src)
        image_fnl.close()
        return image_fnl
   
    #Ne dupliquer qu'une certaine partie, et stocker le reste dans une variable
    else:
        image_fnl.write(image_src[octets_a_dupliquer[0]:octets_a_dupliquer[1]])
        codage_img = image_src[offset:hauteur*largeur]

        image_fnl.close()
        return image_fnl, codage_img, 


def valeurs_pixels(image_source=image_source, valeur_a_afficher = []):
    '''
    Affiche la valeur RGB des pixels d'une image
    arg : 
        str image_source : Image sur laquelle analyser la valeur des pixels
        list valeurs_a_afficher : Position x et y (en partant en bas à gauche) du pixel à afficher
    return : 
        void
    '''
    datas = ouvrir_fichier(image_source)

    hauteur = val_dec(datas[22:26])
    largeur = val_dec(datas[18:22])
    
    offset = val_dec(datas[10:14])
    x = 0
    y = 0
    for i in range(offset, len(datas), 3):
        if len(valeur_a_afficher) != 0:
            if x == valeur_a_afficher[0] and y ==  valeur_a_afficher[1]:
                print('----x=',x, 'y=', y,'------')
                print('couleur ROUGE : ', ' ', val_dec(datas[i+2:i+3]))
                print('couleur VERTE : ', ' ', val_dec(datas[i+1:i+2]))
                print('couleur BLEUE : ', ' ', val_dec(datas[i:i+1]), '\n')
        else:
            print('----x=',x, 'y=', y,'------')
            print('couleur ROUGE : ', ' ', val_dec(datas[i+2:i+3]))
            print('couleur VERTE : ', ' ', val_dec(datas[i+1:i+2]))
            print('couleur BLEUE : ', ' ', val_dec(datas[i:i+1]), '\n')

        x+=1
        if x == largeur:
            y += 1
            x = 0
    print('x finale :', x, 'y finale : ', y)