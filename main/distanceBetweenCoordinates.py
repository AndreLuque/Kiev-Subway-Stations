import haversine as hs
from haversine import Unit


def getDistance(loc1: (float, float), loc2: (float, float)) -> float:
    """
    FORMULA DE HAVERSINE PARA CALCULAR LA DISTANCIA

    from math import radians, cos, sin, asin, sqrt
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # Radius of earth in kilometers.
    return c * r
    """

    # devolvemos la distancia en metros
    return round(hs.haversine(loc1, loc2, unit=Unit.METERS))

# test
# loc1=(28.426846,77.088834)
# loc2=(28.394231,77.050308)
# print(getDistance(loc1, loc2))

