# /etc/init.d/sample.py
### BEGIN INIT INFO
# Provides:          resetAfter2h.py
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start daemon at boot time
# Description:       Enable service provided by daemon.
### END INIT INFO

# Auto start via init.d directory

# sudo cp /home/pi/resetAfter2h.py /etc/init.d/

# cd /etc/init.d

# sudo chmod +x resetAfter2h.py

# sudo update-rc.d resetAfter2h.py defaults

import os
import time

time.sleep(7200)
os.system('systemctl reboot -i')

# yif you don't want to give root privileges to the python process, you can use systemctl reboot -i.
# however, this will ignore all inhibitors, including other users logged in, etc. Use with caution.