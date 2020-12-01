def returnstring(dict,C):
    dict.pop("id")
    string="Data of "+str(C)+"\n\n\n ---------------------\n"
    l=dict.items()
    for i,j in l:
        string+= (str(i)+"  :" +str(j) +"\n\n")
    return  string
    #print(string)

import kivy
from kivy.app import App
from kivy.uix.label import Label
from covid import Covid
covid = Covid()
countries_list = covid.list_countries()
countries=list()

for ele in countries_list:
    countries.append(ele['name'].lower())
Countryname=input("Enter country: ").strip().lower()
#print(countries,Countryname)
if Countryname in countries:
    ins=covid.get_status_by_country_name(Countryname)
    string=returnstring(ins,Countryname)

    #string="Data of "+str(Countryname)+"\n\nActive cases :" + str() +"\nConfirmed cases : " +str(covid.get_total_confirmed_cases()) + "\nRecovered  :" +str(covid.get_total_recovered()) + "\nDeath  :"  + str(covid.get_total_deaths())
else:
    string="Invalid country"

kivy.require('1.11.0')

class MyFirstKivyApp(App):

    def build(self):

        return Label(text=string)

MyFirstKivyApp().run()