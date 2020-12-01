import kivy
from kivy.app import App
from kivy.uix.label import Label
from covid import Covid
covid = Covid()
countries_list = covid.list_countries()
countries=list()
for ele in countries_list:
    countries.append(ele['name'])
Countryname=input("Enter country: ").strip().capitalize()
if Countryname in countries:
    string='''Data of "+str(Countryname)+"\n\nActive cases :" + str(covid.get_total_active_cases()) +"\nConfirmed cases : " +str(covid.get_total_confirmed_cases()) + "\nRecovered  :" +str(covid.get_total_recovered()) + "\nDeath  :"  + str(covid.get_total_deaths()+ "   " ''')
else:
    string="Invalid country"

kivy.require('1.11.0')
k="123"
class MyFirstKivyApp(App):

    def build(self):

        return Label(text=string)

MyFirstKivyApp().run()