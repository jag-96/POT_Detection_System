import gps
 
# Listen on port 2947 (gpsd) of localhost
session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
 
while True:
    try:
        report = session.next()
        # Wait for a 'TPV' report and display the current time
        # To see all report data, uncomment the line below
        #print(report) #shows all report attributes, comment out so just see certain ones
        if (report['class'] == 'TPV'):
          	if hasattr(report, 'time') and hasattr(report, 'lat') and hasattr(report, 'lon'):
        	       	print('Time: '+str(report.time)+'\tLat: '+str(report.lat)+'\tLon: '+str(report.lon))
    except KeyError:
        pass
    except KeyboardInterrupt:
        quit()
    except StopIteration:
        session = None
        print("GPSD has terminated")