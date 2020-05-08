import urllib2
from bs4 import BeautifulSoup
from mechanize import ParseResponse, urlopen


class VehicleScrape:
    def __init__(self, reg):
        self.reg = reg

    def auto_trader(self):
        req = urllib2.Request('https://www.vehiclecheck.co.uk/', urllib2.urlencode({'vrm': self.reg}))
        response = urllib2.urlopen(req)
        the_page = response.read()
        soup = BeautifulSoup(the_page, "lxml")
        vehicle_model = soup.find('input', {'id': 'VehicleModel'}).get('value')
        vehicle_make = soup.find('input', {'id': 'VehicleMake'}).get('value')  # TODO: pass this as an argument for uk_gov method
        vehicle_colour = soup.find('input', {'id': 'VehicleColour'}).get('value')
        registration_year = soup.find('input', {'id': 'RegistrationYear'}).get('value')

    def uk_gov(self):
        response = urlopen('https://www.check-mot.service.gov.uk/')
        forms = ParseResponse(response, backwards_compat=False)
        form = forms[0]
        form['registration'] = self.reg
        form['manufacturer'] = vehicle_make
        soup = BeautifulSoup(urlopen(form.click()).read(), "lxml")
        fuel_type = soup.find('strong', {'id': 'FuelTypeShown'}).string
        cylinder_capacity = str(soup.find('li', {'id': 'CylinderCapacity'}).text
                                .replace("Cylinder capacity (cc) ", "")
                                .replace("\n", "")
                                .replace("cc", ""))
