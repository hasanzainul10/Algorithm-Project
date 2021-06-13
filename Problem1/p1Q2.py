import googlemaps



def getDistance(originPoint, destinationPoint):
    apikey = "AIzaSyCp8CD7iAXNePYibtVrNiTqo8SeUTQFU24"
    gmapclient = googlemaps.Client(key=apikey)
    d_goog = gmapclient.distance_matrix(
        originPoint, destinationPoint, mode="driving"
    )
    new_d = d_goog["rows"][0]["elements"][0]["distance"]["value"]
    print(f"Driving distance from {originPoint} to {destinationPoint} :")
    print((new_d / 1000), "km")



def start():


            originPoint = "Rawang"
            destinationPoint = "Bukit Jelutong"
            getDistance(originPoint,destinationPoint)

            originPoint = "Subang Jaya"
            destinationPoint = "Puncak Alam"
            getDistance(originPoint, destinationPoint)

            originPoint = "Ampang"
            destinationPoint = "Cyber Jaya"
            getDistance(originPoint, destinationPoint)

            print("")


