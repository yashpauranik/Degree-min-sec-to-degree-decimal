import json

def lambda_handler(event, context):
    dd = event["degree"] + float(event["min"])/60 + float(event["sec"])/3600
    return str(dd)