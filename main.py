from taxi import Taxi
from taxi_company import Taxi_Company

class InvalidTaxiNAME(Exception):
    pass


    

company = Taxi_Company()
taxi1 = Taxi.toString(1,  "Anvar", "Spark", "01P234AA")
taxi2 = Taxi.toString(2,  "Anvar", "Spark", "01P234AA")
company.addTaxi(taxi1)
company.addTaxi(taxi2)
