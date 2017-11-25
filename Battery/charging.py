import sys
from time import sleep
import notify2
notify2.init("charge")

battery_status_file = "/sys/class/power_supply/BAT1/uevent"

try:
    while True:
        with open(battery_status_file) as state:

            for s in state:
                if s.split('=')[0] == 'POWER_SUPPLY_STATUS':
                    status = s.split('=')[1].strip('\n')

                if s.split('=')[0] == 'POWER_SUPPLY_CAPACITY':
                    battery = s.split('=')[1].strip('\n')
        
        battery = int(battery)
        
        if battery < 40 and status == 'Discharging':
            head = 'Connect Charger'
            message = 'Charge remaining: ' + str(battery) + '%'
            notify2.Notification(head, message).show()

        if battery > 80 and (status == 'Charging' or status == 'Full'):
            head = 'Disconnect Charger'
            message = 'Charge remaining: ' + str(battery) + '%'
            notify2.Notification(head, message).show()

        sleep(15)


except KeyboardInterrupt:
    print("\nCtrl+C pressed. Exiting.")
