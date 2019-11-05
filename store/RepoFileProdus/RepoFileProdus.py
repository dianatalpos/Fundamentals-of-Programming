'''
Created on Feb 16, 2019

@author: Andrea
'''
from Domain.Produs import Produs
from Errors.Error import RepoError
class RepoFileProdus():
    def __init__(self,fileName):
        self.__fileName = fileName
        self.__lista = []
        self.__fdenumire = []
        self.__fpret = -1
    
    def get_fdenumire(self):
        return self.__fdenumire
    
    def get_fpret(self):
        return self.__fpret
    
    def loadFromFile(self):
        self.__lista = []
        with open(self.__fileName, 'r') as produs:
            linie = produs.readline().strip()
            while linie!="":
                sir = produs.readline().split(",")
                id = int(sir[0])
                denumire = str(sir[1])
                pret = int(sir[2])
                p1 = Produs(id,denumire,pret)
                self.__lista.append(p1)
                linie= produs.readline().strip()
    
    def storeToFile(self):
        with open(self.__fileName, 'w') as produs:
            for i in self.__lista:
                linie = str(i.get_id())+","
                linie+=str(i.get_denumire())+","
                linie+=str(i.get_pret())
                linie+="\n"
                produs.write(linie)
    
    def get_all(self):
        return self.__lista
    
    def set_lista(self,l):
        self.__lista = l
    
    def cautare_produs(self,id):
        for i in range(0,len(self.__lista)):
            curent = self.__lista[i]
            if int(curent.get_id()) == int(id):
                return i 
        return -1
        
    def adaugare(self, produs):
        val = self.cautare_produs(produs.get_id())
        if val!=-1:
            raise RepoError("Produsul exista deja")
        else:
            self.__lista.append(produs)
            self.storeToFile()
    
    def stergere(self, produs):
        val = self.cautare_produs(produs.get_id())
        if val==-1:
            raise RepoError("Produsul nu exista pentru a fi sters")
        else:
            del self.__lista[val]
            self.storeToFile()
            
    def modificare(self, id,denumire,pret):
        val = self.cautare_produs(id)
        if val!=-1:
            self.__lista[val].set_denumire(denumire)
            self.__lista[val].set_pret(pret)
            self.storeToFile()
        else:
            raise RepoError("Nu exista acest produs!")
                    
    def modificarefiltru(self,val,care):
        if str(care) == "denumire":
            self.__fdenumire = str(val)

        if str(care) == "pret":
            self.__fpret = int(val)
    
    def aplicareFiltru(self):
        lista =[]
        for i in self.__lista:
            if str(i.get_denumire()) == str(self.__fdenumire):
                lista.append(i)
            if int(i.get_pret()) == int(self.__fpret):
                lista.append(i)
        return lista 