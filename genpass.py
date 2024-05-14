#!usr/bin/env python3
# -*- coding: utf-8 -*-

import os, time
import fontcolor as fc
import allchars


while True:
    os.system('clear')

    print(fc.green_font(''' 
 # =======================================================================
 # =   GENPASS - Générateur de mots de passe                             =
 # =                                                                     =
 # =      - Version   : 1.0                                              =
 # =      - Author    : Ayckinn                                          =
 # =      - Site      : www.ayckinn.fr                                   =
 # =      - Mail      : contact@ayckinn.fr                               =
 # =      - Release   : May 14' 2024                                     =
 # =      - Github    : https://github.com/AyckinnLisa?tab=repositories  =
 # =      - Copyright : 2024 - ayckinn.fr                                =
 # ======================================================================='''))

    print(fc.red_font("\n /!\\ NOTEZ BIEN CE MOT DE PASSE !"))
    print(fc.red_font(" Une fois le programme fermé, IL NE SERA PLUS POSSIBLE DE LE RETROUVER..."))

    print("\n\n Sélectionnez les caractères de votre mot de passe :\n ")
    print(fc.yellow_font("    [01]"), fc.magenta_font("Lettres minuscules seulement"))
    print(fc.yellow_font("    [02]"), fc.magenta_font("Lettres majuscules seulement"))
    print(fc.yellow_font("    [03]"), fc.magenta_font("Lettres majuscules et minuscules\n"))
    print(fc.yellow_font("    [04]"), fc.magenta_font("Numérique\n"))
    print(fc.yellow_font("    [05]"), fc.magenta_font("Alpha-Numérique Minuscules"))
    print(fc.yellow_font("    [06]"), fc.magenta_font("Alpha-Numérique Majuscules"))
    print(fc.yellow_font("    [07]"), fc.magenta_font("Alpha-Numérique complet\n"))
    print(fc.yellow_font("    [08]"), fc.magenta_font("Symboles"))
    print(fc.yellow_font("    [09]"), fc.magenta_font("Symboles + Numérique"))
    print(fc.yellow_font("    [10]"), fc.magenta_font("Symboles + Minucules"))
    print(fc.yellow_font("    [11]"), fc.magenta_font("Symboles + Majuscules"))
    print(fc.yellow_font("    [12]"), fc.magenta_font("Lettres complètes + Symboles\n"))

    print(fc.yellow_font("    [13]"), fc.magenta_font("Le plus robuste !\n"))

    print(fc.yellow_font("    [!q]"), fc.blue_font("Quitter le programme"))


    menu = input("\n\n Votre choix (ex : 01, 05, 10) >> ")

    if "01" in menu:
        allchars.lower_pass()
        break

    elif "02" in menu:
        allchars.upper_pass()
        break

    elif "03" in menu:
        allchars.upper_and_lower_pass()
        break

    elif "04" in menu:
        allchars.numerics()
        break

    elif '05' in menu:
        allchars.lower_alphanum_pass()
        break

    elif "06" in menu:
        allchars.upper_alphanum_pass()
        break

    elif "07" in menu:
        allchars.full_alphanum_pass()
        break

    elif "08" in menu:
        allchars.symbols_pass()
        break

    elif "09" in menu:
        allchars.symbols_num_pass()
        break

    elif "10" in menu:
        allchars.lower_symbols_pass()
        break

    elif '11' in menu:
        allchars.upper_symbols_pass()
        break

    elif '12' in menu:
        allchars.full_letters_symbols()
        break

    elif '13' in menu:
        allchars.full_strongest_pass()
        break

    elif "!q" in menu:
        exit()

    else:
        print(fc.red_font("\n Mauvais choix !"))
        time.sleep(2)
