'''
Created on Feb 16, 2019

@author: Andrea
'''
from RepoFileProdus.RepoFileProdus import RepoFileProdus
from Validator.ValidatorProdus import ValidatorProdus
from Service.serviceProdus import ServiceProdus
from UI.UI import UI

repo = RepoFileProdus("Produse.txt")

validator = ValidatorProdus()
service = ServiceProdus(repo,validator)
ui = UI(service)

ui.run()