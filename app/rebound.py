import json
import requests
import os
import operator
from datetime import datetime, date, timedelta

class ReBound():
  def reboundSearch(self, departingAirport, arrivingAirport, departingWeekday, returningWeekday, maxStopsDeparting, maxStopsReturning):
    departingWeekday = int(departingWeekday)
    returningWeekday = int(returningWeekday)
    weeksToSearch = 1

    api_key = "AIzaSyBZj9cQKwEbMVQoSAgbfP1nhntS7peg-Jw"
    url = "https://www.googleapis.com/qpxExpress/v1/trips/search?key=" + api_key
    headers = {'content-type': 'application/json'}

    dateGo = datetime.today()
    while dateGo.weekday() != departingWeekday: 
        dateGo += timedelta(days=1)
    dateReturn = dateGo
    while dateReturn.weekday() != returningWeekday: 
        dateReturn += timedelta(days=1)
    data = {};

    for x in range(1,weeksToSearch+1):
      params = {
        "request": {
          "slice": [
            {
              "origin": departingAirport,
              "destination": arrivingAirport,
              "date": (dateGo + timedelta(7 * x)).strftime('%Y-%m-%d'),
              "maxStops": maxStopsDeparting,
              "permittedDepartureTime": {
                "earliestTime": "17:00",
              }
            },
            {
              "origin": arrivingAirport,
              "destination": departingAirport,
              "date": (dateReturn + timedelta(7 * x)).strftime('%Y-%m-%d'),
              "maxStops": maxStopsReturning,
              "permittedDepartureTime": {
                "earliestTime": "13:30",
                "latestTime": "23:00"
              }
            }
          ],
          "passengers": {
            "adultCount": 1,
          },
          "solutions": 1,
        }
      }

      response = requests.post(url, data=json.dumps(params), headers=headers)
      data[x]=response.json()

    # write out results to file
    # print json.dumps(data, indent=1)

    flights = {}
    for x in range(1,weeksToSearch+1):
      try:
        flights[data[x]["trips"]["tripOption"][0]["slice"][0]["segment"][0]["leg"][0]["departureTime"]] = data[x]["trips"]["tripOption"][0]["saleTotal"][3:]
      except:
        pass
    for key,value in sorted(flights.items(), key=operator.itemgetter(1)):
      try:
        print key + ", " + value
        file1.write(key + ", " + value)
      except:
        pass
    return sorted(flights.items(), key=operator.itemgetter(1))