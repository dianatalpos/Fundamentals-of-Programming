'''
Created on Feb 16, 2019

@author: Andrea
'''
from Domain.Produs import Produs
from Errors.Error import ValidError, RepoError
from Errors.Error import UndoError,RedoError
from Domain.Undo import Undo, CascadeOperation
from RepoFileProdus.RepoFileProdus import RepoFileProdus
import random
class ServiceProdus():
    def __init__(self,repo,validator):
        self.__repo = repo 
        self.__validator = validator
    
    def adaugare(self,id,denumire,produs):
        p1 = Produs(id,denumire,produs)
        try:
            self.__validator.ValidatorProdus(p1)
            self.__repo.adaugare(p1)
        except ValidError as ve:
            print(str(ve))
        except ValueError as vee:
            print(str(ve))
        except RepoError as re:
            print(str(re))
        
    def stergere(self, cifra):
        contor = 0
        lista = self.__repo.get_all()
        for i in lista:
            nr = int(i.get_id())
            while nr>0:
                uc = nr%10
                if uc == int(cifra):
                    self.__repo.stergere(i)
                    contor = contor +1
                    nr = -1
                else:
                    nr = nr//10
            if nr == 0:
                if nr%10 == int(cifra):
                    contor+=1
        for i in lista:
            nr = int(i.get_id())
            while nr>0:
                uc = nr%10
                if uc == int(cifra):
                    self.__repo.stergere(i)
                    contor = contor +1
                    nr = -1
                else:
                    nr = nr//10
            if nr == 0:
                if nr%10 == int(cifra):
                    contor+=1
        return contor
    
    def modificare(self,id,denumire,pret):
        produs = Produs(id,denumire,pret)
        try:
            self.__validator.ValidatorProdus(produs)
            self.__repo.modificare(id,denumire,pret)
        except ValidError as ve:
            print(str(ve))
        except RepoError as re:
            print(str(re))
            
    def construire(self):
        consoane = "qwrtyupsdfghjklzxcvbnm"
        vocale = "euioa"
        cuv = []
        rez=[]
        prima = random.randint(1,2)
        val = random.randint(3,15)
        if prima==1:
            while val!=0:
                cuv.append(random.choice(consoane))
                val=val-1
                if val!=0:
                    cuv.append(random.choice(vocale))
                    val=val-1
        else:
            while val!=0:
                cuv.append(random.choice(vocale))
                val=val-1
                if val!=0:
                    cuv.append(random.choice(consoane))
                    val=val-1
        rez+=cuv
        rez+=[" "]
        raspuns=""
        for i in rez:
            raspuns+=i
        return raspuns 
    
    def aleator(self, nr):
        j=1
        while j<=int(nr):
            id = random.randint(1,500)
            denumire = self.construire()
            pret = random.randint(1,1000)
            produs = Produs(id,denumire,pret)
            self.__repo.adaugare(produs) 
            j= j+1
    
    def importul(self, fisier):
        nr =0
        with open(fisier, 'r') as produs:
            linie = produs.readline().strip()
            while linie!="":
                sir = linie.split(" ")
                val = self.__repo.cautare_produs(int(sir[0]))
                if val==-1:
                    p1 = Produs(int(sir[0]),str(sir[1]), random.randint(1,500))
                    self.__repo.adaugare(p1)
                    nr=nr+1
                linie = produs.readline().strip()
        return nr
    def getAll(self):
        self.__repo.get_all()
    def denumire(self):
        return self.__repo.get_fdenumire()
    
    def pret(self):
        return self.__repo.get_fpret()
    
    def modificareFiltru(self,val,care):
        self.__repo.modificarefiltru(val,care)
        
    def afisareFiltre(self):
        self.__repo.aplicareFiltru()
    
    def sortare(self,l):
        l.sort(key=lambda x: x.get_denumire(), reverse = True)
        self.__repo.storeToFile()
        return l 
                    