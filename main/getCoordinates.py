from geopy.geocoders import GoogleV3

GOOGLE_API_KEY = 'AIzaSyAuAvpH821BGqu3s2PMTJpEx5DUxMO5ts4'


def coordinates(location: str) -> (float, float):
    # llamamos a un localizador, en este caso es el de google (mayor cantidad de datos)
    # pasamos la llave del api
    geolocator = GoogleV3(api_key=GOOGLE_API_KEY)

    # tranformamos la direccion a un objeto geocode.location
    location = geolocator.geocode(location+", Kyiv")

    # retornamos la longitud y latitud
    return location.latitude, location.longitude

