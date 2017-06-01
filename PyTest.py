import time
import json

def lambda_handler(value, context):
    print "start"
    print value
    time.sleep(2)
    print "end"
    
