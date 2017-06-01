import boto3
import json

#from __future__ import print_function

def lambda_handler(value, context):
    event_val = 0
    lam = boto3.client('lambda')
    print "Call started"
    for event_val in range (0,100):
        print "Call: %d" % event_val
        test = json.dumps({"value":event_val})

#comment the functions that are not being invoked
        #python invocation
        resp = lam.invoke(
            FunctionName = 'PyTest',
            InvocationType='Event',
            LogType='None',
            Payload=test
            )

        '''# Node.js invocation
        resp = lam.invoke(
            FunctionName = 'NodeTest',
            InvocationType='Event',
            LogType='None',
            Payload='{ "value": "node.js" }'
            )
        '''
        '''# C# invocation
        resp = lam.invoke(
            FunctionName = 'DotnetTest',
            InvocationType='Event',
            LogType='None',
            Payload=test
            )
        '''
        print (resp)
        event_val += 1
    return True
    
    
