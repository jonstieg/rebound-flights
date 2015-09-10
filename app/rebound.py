import json
import requests
import os
import operator
from datetime import datetime, date, timedelta

class ReBound():
  def reboundSearch(self, departingAirport, arrivingAirport, departingWeekday, returningWeekday):
    weekdays = {'mon': 0, 'tue': 1, 'wed': 2, 'thu': 3, 'fri': 4, 'sat': 5, 'sun': 6}
    dayOfWeekToLeave = weekdays[departingWeekday.lower()]
    dayOfWeekToReturn = weekdays[returningWeekday.lower()]
    weeksToSearch = 5

    api_key = "AIzaSyBZj9cQKwEbMVQoSAgbfP1nhntS7peg-Jw"
    url = "https://www.googleapis.com/qpxExpress/v1/trips/search?key=" + api_key
    headers = {'content-type': 'application/json'}

    dateGo = datetime.today()
    while dateGo.weekday() != dayOfWeekToLeave: 
        dateGo += timedelta(days=1)
    dateReturn = dateGo
    while dateReturn.weekday() != dayOfWeekToReturn: 
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
              "maxStops": 1,
              "permittedDepartureTime": {
                "earliestTime": "17:00",
              }
            },
            {
              "origin": arrivingAirport,
              "destination": departingAirport,
              "date": (dateReturn + timedelta(7 * x)).strftime('%Y-%m-%d'),
              "maxStops": 0,
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