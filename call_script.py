import os
import sys
os.system('echo "tatti" > /home/shreyakupadhyay/Documents/yatra-hackathon/data_file.txt')
os.system('/usr/bin/python /home/shreyakupadhyay/Documents/yatra-hackathon/get_id.py '+ sys.argv[1] + ' ' + '>> /home/shreyakupadhyay/Documents/yatra-hackathon/data_file.txt')
