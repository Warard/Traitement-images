# -*- coding: utf-8 -*-
"""
Created on Tue May 25 14:51:22 2021

@author: trouillem
"""

    '''
    Ouvre un fichier, et retourne son contenu de manière spécifique : 
        Si octets_to_read est nul, tout le fichier est lue et renvoyé,
        Sinon : La lecture s'arrête au octets_to_read-ème octet du fichier

        Si specific_octets_to_read est nul, le comportement ci-dessus s'applique
        Sinon, seul les specific_octets_to_read de longueur len_specific_values sont lus dans le fichier
      
    arg : 
        str file_name : nom du fichier et son extension
        int octets_to_read: Nombre d'octets à lire
        list specific_octets_to_read : indices des indices spéciaux à lire
    return:
        list datas : liste des valeurs spécifiques lues
        binary file : fichier 
    '''

    # PLUTOT UTILISER UN SLICING SUR LES LISTES !? cf fonction inf_image
    if len(specific_octets_to_read) != 0:
        i = 0
        # Pour toutes les valeurs spécifiques 
        for n in specific_octets_to_read:
            # Placer l'indice à la valeur spécifique
            source.seek(n)
            # Ouvir le fichier et lire les valeurs spécifiques
            file = source.read(len_specific_values[i])
            # Ajouter ces valeurs spécifiques à la liste finale 
            datas.append(file)
            i += 1

        source.close()
        return datas