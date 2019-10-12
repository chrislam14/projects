import urllib.parse
import urllib.request
import json

class MapQuest:
    def __init__(self, key):
        self._BASEURL = "http://open.mapquestapi.com/directions/v2/route?"
        self._BASEURL1 = "http://www.mapquestapi.com/geocoding/v1/address?"
        self._BASEURL2 = "http://www.mapquestapi.com/search/v4/place?"
        self._API_key = key
    def buildURL(self, start, end):
        queryparameters = [('key',self._API_key),('from',start),('to',end)]
        return self._BASEURL+urllib.parse.urlencode(queryparameters, True)
    def buildURL1(self, location):
        queryparameters = [('key',self._API_key),('location',location)]
        return self._BASEURL1+urllib.parse.urlencode(queryparameters, True)
    def buildURL2(self, location:list, keyword:str, result:int):
        queryparameters = [('location',location),('sort','distance'),('key',self._API_key),('pageSize',result),('q',keyword)]
        return self._BASEURL2+urllib.parse.urlencode(queryparameters, True)
    def getResult(self, url):
        response = None
        try:
            response = urllib.request.urlopen(url)
            return json.load(response)
        finally:
            if response != None:
                response.close()
    def printResults (self, results):
        for item in results:
            for i in results[item]:
                print(str(item)+': '+ str(i)+": "+str(results[item][i]))
    def totalDistance(self, locations:list)->float:
        if len(locations) <= 1:
            return 0
        else:
            endlocations = []
            totalDist = 0
            for l in locations:
                if l != locations[0]:
                    endlocations.append(l) 
            query_string = self.buildURL(locations[0],endlocations)
            result = self.getResult(query_string)
            totalDist = result['route']['distance']
            return totalDist
    def totalTime(self, locations:list)->float:
        if len(locations) <= 1:
            return 0
        else:
            endlocations = []
            totaltime = 0
            for l in locations:
                if l != locations[0]:
                    endlocations.append(l) 
            query_string = self.buildURL(locations[0],endlocations)
            result = self.getResult(query_string)
            totaltime = result['route']['time']
            return totaltime
    def directions(self,locations:list)->str:
        directionsstr = ""
        if len(locations) <= 1:
            return 0
        else:
            endlocations = []
            for l in locations:
                if l != locations[0]:
                    endlocations.append(l)
            query_string = self.buildURL(locations[0],endlocations)
            result = self.getResult(query_string)
            for m1 in range(len(result['route']['legs'])):
                for m2 in range(len(result['route']['legs'][m1]['maneuvers'])):
                    directionsstr += result['route']['legs'][m1]['maneuvers'][m2]['narrative']+'\n'
        return directionsstr
    def pointOfInterest(self,locations:str, keyword:str, result:int)->list:
        POIlist = []
        url1 = self.buildURL1(locations)
        result1 = self.getResult(url1)
        coordinates = str(result1['results'][0]['locations'][0]['latLng']['lng'])+','+str(result1['results'][0]['locations'][0]['latLng']['lat'])
        url2 = self.buildURL2(coordinates,keyword,result)
        result2 = self.getResult(url2)
        for r in result2['results']:
            POIlist.append(r['displayString'])
        return POIlist
