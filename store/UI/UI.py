'''
Created on Feb 16, 2019

@author: Andrea
'''
from Domain.Produs import Produs
class UI():
    def __init__(self,service):
        self.__service = service

            
    def run(self):
        print("               MENIU                  ")
        print("1 pentru a adauga un produs in fisier ")
        print("2 pentru a sterge produse dupa id-ul lor")
        print("3 pentru filtrarea produselor")
        print("4 pentru undo")
        print("5 pentru modificare denumire si pret")
        print("6 pentru a genera random produse in fisier")
        print("7 pentru a prelua produse din fisier")
        print("8  Schimbare filtru")
        print("9 Afisare produse filtre active")
        print("10 pentru a sorta lista de produse")
        while True:
            cmd = int(input("Introduceti o comanda!"))
            
            if cmd ==1:
                id = int(input("Introduceti un id: "))
                denumire = str(input("Introduceti denumirea produsului: "))
                pret = int(input("Introduceti pretul produsului: "))
                self.__service.adaugare(id,denumire,pret)
            
            if cmd == 2:
                cifra = input("Introduceti cifra: ")
                contor = self.__service.stergere(cifra)
                print("Au fost sterse", contor, "elemente din fisier")
            if cmd==3:
                print("Sirul vid daca nu se mai doreste filtrarea dupa denumire ")
                print("-1 daca nu se mai doreste filtrarea dupa pret")
                comanda = input("Introduceti sirul vid sau -1 ")
                if comanda == " ":
                    print(self.__service.sortareDupaPret())
                if int(comanda) == -1:
                    print(self.__service.sortareDupaDenumire())
            if cmd == 4:
                self.__servUndo.perfom_undo()
            if cmd==5:
                id = int(input("Introduceti id-ul produsului: "))
                denumire= str(input("Introduceti noua denumire produsului: "))
                pret = int(input("Introduceti noul pret: "))
                self.__service.modificare(id,denumire,pret)
            if cmd == 6:
                nr = input("Dati numarul de generari pe care le doriti: ")
                self.__service.aleator(nr)
            if cmd ==7:
                fis =input("Dati fisierul: ")
                nr = self.__service.importul(fis)
                print("Au fost introduse  ", nr, "produse in fisier")
            if cmd ==8:
                care = input("dati numele filtrului: ")
                val = input("dati valoarea cu care vreti sa schimbati: ")
                self.__service.modificareFiltru(val,care)
            if cmd == 9:
                lista = self.__service.afisareFiltre()
                for i in lista:
                    print(i)
                    print("---------------------------------")
            
            if cmd == 10:
                lista = self.__service.getAll()
                print(self.__service.sortare(lista))