from Domain.Produs import Produs
from RepoFileProdus import RepoFileProdus
repo = RepoFileProdus("teste.txt")
def test_loadfromfile_getall_storetofile():
    p1= Produs(473, "mancare", 94)
    p2 = Produs(43,"fructe", 953)
    l =[p1,p2]
    repo.set_lista(l)
    repo.storeToFile()
    
    repo.loadFromFile()
    lista = repo.get_all()
    p1= Produs(473, "mancare", 94)
    p2 = Produs(43,"fructe", 953)
    l =[p1,p2]
    assert lista[0].get_id() == p2.get_id()
    assert lista[0].get_denumire() == p2.get_denumire()
    assert lista[0].get_pret() == p2.get_pret()
    
    p3 = Produs(47,"videe", 32)
    l=[p3]
    repo.set_lista(l)
    listam = repo.get_all()
    
    assert listam[0].get_id() == p3.get_id()
    assert listam[0].get_denumire() == p3.get_denumire()
    assert listam[0].get_pret() == p3.get_pret()
    
    
def test_adaugare():
    
    p1= Produs(473, "mancare", 94)
    p2 = Produs(43,"fructe", 953)
    l =[p1,p1]
    repo.set_lista(l)
    repo.storeToFile()
    
    lista = repo.get_all()
    p3 =  Produs(47,"videe", 32)
    repo.adaugare(p3)
    listam= repo.get_all()
    
    assert listam[2].get_id() == p3.get_id()
    assert listam[2].get_denumire() == p3.get_denumire()
    assert listam[2].get_pret() == p3.get_pret()
    
def test_stergere():
    
    p1= Produs(473, "mancare", 94)
    p2 = Produs(43,"fructe", 953)
    l =[p1,p2]
    repo.set_lista(l)
    repo.storeToFile()
    
    lista = repo.get_all()
    assert len(lista) == 2

    repo.stergere(p2)
    listam = repo.get_all()
    
    assert len(listam) == 1
    
    
test_stergere()
test_adaugare()
test_loadfromfile_getall_storetofile()