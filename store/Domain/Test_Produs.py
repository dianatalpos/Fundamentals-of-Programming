'''
Created on Feb 16, 2019

@author: Andrea
'''
from Domain.Produs import Produs
def test_produs():
    p1 = Produs(34,"mancare",90)
    assert p1.get_denumire() == "mancare"
    assert p1.get_id() == 34
    assert p1.get_pret() == 90

test_produs()