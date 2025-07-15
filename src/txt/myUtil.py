##############################################################################
# File name: myUtil.py                                                       #
# Date     : 2025-07-12                                                      #
# Author   : Fábio Marques (fmarques@fmarques.eti.br)                        #
# Purpose  : Utilitary functions file                                        #
##############################################################################

import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def wait():
    input('\nPress any key to continue...')