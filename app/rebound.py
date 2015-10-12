import json
import requests
import os
import operator
import time
from datetime import datetime, date, timedelta
from easygui import msgbox


class ReBound():
  def reboundSearch(self, dateGo, departingAirport, arrivingAirport, departingWeekday, returningWeekday, maxStopsDeparting, maxStopsReturning, departingTimeEarly, departingTimeEarlyAMPM, departingTimeLate, departingTimeLateAMPM, returningTimeEarly, returningTimeEarlyAMPM, returningTimeLate, returningTimeLateAMPM):
    departingWeekday = int(departingWeekday)
    returningWeekday = int(returningWeekday)

    departingTimeEarly = "00:00" if departingTimeEarly == '' else str(int(departingTimeEarly) + int(departingTimeEarlyAMPM)) + ":00"
    returningTimeEarly = "00:00" if returningTimeEarly == '' else str(int(returningTimeEarly) + int(returningTimeEarlyAMPM)) + ":00"
    departingTimeLate = "23:59" if departingTimeLate == '' else str(int(departingTimeLate) + int(departingTimeLateAMPM)) + ":00"
    returningTimeLate = "23:59" if returningTimeLate == '' else str(int(returningTimeLate) + int(returningTimeLateAMPM)) + ":00"
    weeksToSearch = 1

    # time.sleep(35)

    api_key = os.environ['googAPI']
    msgbox(os.environ['googAPI'])

    url = "https://www.googleapis.com/qpxExpress/v1/trips/search?key=" + api_key
    headers = {'content-type': 'application/json'}

    #dateGo = datetime.today()
    while dateGo.weekday() != departingWeekday: 
        dateGo += timedelta(days=1)
    dateReturn = dateGo + timedelta(days=1)
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
                "earliestTime": departingTimeEarly,
                "latestTime": departingTimeLate
              }
            },
            {
              "origin": arrivingAirport,
              "destination": departingAirport,
              "date": (dateReturn + timedelta(7 * x)).strftime('%Y-%m-%d'),
              "maxStops": maxStopsReturning,
              "permittedDepartureTime": {
                "earliestTime": returningTimeEarly,
                "latestTime": returningTimeLate
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