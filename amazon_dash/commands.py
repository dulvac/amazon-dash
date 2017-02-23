import lifx
import time
import thread


# Lifx
# Create the client and start discovery
lights = lifx.Client()
lights_on = True
def rediscover_lights():
    while True:
        global lights
    	lights = lifx.Client()
    	time.sleep(7)

# rediscover lights forever
thread.start_new_thread(rediscover_lights, ())

# Actual commands
def test():
    print "test!"

def toggle_lights():
    global lights
    global lights_on
    print "Turning lights " + ("ON" if not lights_on else "OFF")
    # Turn all bulbs off
    for l in lights.get_devices():
        try: 
            print 'Toggling %s. ' % l.label
            l.power = not lights_on
        except Exception as e:
            print e
    lights_on = not lights_on
