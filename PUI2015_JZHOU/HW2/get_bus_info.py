
import json
import sys
import urllib2
import csv

if __name__=='__main__':
	url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (sys.argv[1], sys.argv[2].upper())
	request = urllib2.urlopen(url)
	metadata = json.load(request)
	VehAc = metadata["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]
	
	with open(sys.argv[3], 'wb') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(['Latitude', 'Longitude', 'Stop Name', 'Stop Status'])

		for EachBus in VehAc:
			latitude = EachBus["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"]
			longitude = EachBus["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]
			if EachBus["MonitoredVehicleJourney"]["OnwardCalls"] == {}:
				StopName = "N/A"
				StopStatus = "N/A"
			else:
				StopName = EachBus["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"][0]["StopPointName"]
				StopStatus = EachBus["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"][0]["Extensions"]["Distances"]["PresentableDistance"]
			row = [latitude, longitude, StopName, StopStatus]
			writer.writerow(row)
			
	print '%s, %s, %s, %s' %(latitude, longitude, StopName, StopStatus)
		
#	 metadata["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"][0/1/2/...]["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]
	
	
	
	