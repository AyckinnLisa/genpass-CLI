# --- CHARACTERS HANDLING ---

import string, random
import fontcolor as fc


LOWER_LETTERS = string.ascii_lowercase
UPPER_LETTERS = string.ascii_uppercase
UPLO_LETTERS = (LOWER_LETTERS + UPPER_LETTERS)

NUMERICS = string.digits
LOWER_ALPHANUMERIC = (LOWER_LETTERS + NUMERICS)
UPPER_ALPHANUMERIC = (UPPER_LETTERS + NUMERICS)
FULL_ALPHANUMERIC = (UPLO_LETTERS + NUMERICS)

SYMBOLS = '+-*/=(){\}$€%&\'\"'
SYMBOLS_NUMERIC = (SYMBOLS + NUMERICS)
LOWER_AND_SYMBOLS = (LOWER_LETTERS + SYMBOLS)
UPPER_AND_SYMBOLS = (UPPER_LETTERS + SYMBOLS)
FULL_LETTERS_AND_SYMBOLS = (UPLO_LETTERS + SYMBOLS)
STRONGEST = (UPLO_LETTERS + NUMERICS + SYMBOLS)



def gen_pass(chars):
    length = int(input("\n Entrez le nombre de caractères souhaités : "))
    password = ''.join(random.sample(chars, length))
    print("\n Nouveau mot de passe : ", end="")
    print(fc.blue_font(f"{password}"))



def lower_pass():
    return gen_pass(LOWER_LETTERS)

def upper_pass():
    return gen_pass(UPPER_LETTERS)

def upper_and_lower_pass():
    return gen_pass(UPLO_LETTERS)

def numerics():
    return gen_pass(NUMERICS)

def lower_alphanum_pass():
    return gen_pass(LOWER_ALPHANUMERIC)

def upper_alphanum_pass():
    return gen_pass(UPPER_ALPHANUMERIC)

def full_alphanum_pass():
    return gen_pass(FULL_ALPHANUMERIC)

def symbols_pass():
    return gen_pass(SYMBOLS)

def symbols_num_pass():
    return gen_pass(SYMBOLS_NUMERIC)

def lower_symbols_pass():
    return gen_pass(LOWER_AND_SYMBOLS)

def upper_symbols_pass():
    return gen_pass(UPPER_AND_SYMBOLS)

def full_letters_symbols():
    return gen_pass(FULL_LETTERS_AND_SYMBOLS)

def full_strongest_pass():
    return gen_pass(STRONGEST)
