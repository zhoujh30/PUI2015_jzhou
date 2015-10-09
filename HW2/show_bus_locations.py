
import json
import sys
import urllib2

if __name__=='__main__':
	url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (sys.argv[1], sys.argv[2].upper())
	request = urllib2.urlopen(url)
	metadata = json.load(request)
	
	print "Bus Line : %s" % (sys.argv[2].upper())
	
	VehAc = metadata["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]
	
	count = 0
		
	for EachBus in VehAc:
		latitude = EachBus["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"]
		longitude = EachBus["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]
		print "Bus %s is at latitude %s and longitude %s" %(count, latitude, longitude)
		count += 1
#	
	print "Number of Active Buses : %s" %(count)
#		
#	 metadata["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"][0/1/2/...]["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]
#	
#	
#	
#	