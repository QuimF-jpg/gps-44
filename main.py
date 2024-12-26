# main.py

"""Mòdul principal per a la transformació de cadenes de text."""

import transform

def main():
    """Core de la prova"""
    string = input("Introdueix un string: ")
    
    print("Quina transformació vols?")
    print("[1] Text amb tot majúscules")
    print("[2] Text amb tot minúscules")
    print("[3] Text capitalitzat")

    opcio = input("Opció escollida: ")

    if opcio == "1":
        print(transform.to_upper_case(string))
    elif opcio == "2":
        print(transform.to_lower_case(string))
    elif opcio == "3":
        print(transform.to_capitalize(string))
    else:
        print("Opció no reconeguda")

if __name__ == '__main__':
    main()
