import requests
import sys
import json

# 3rd Party API Client ID
client_id = 'a1b2c3d4e5f6g7h8i9j0'

# API Key
api_key = 'a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6'

# If not using the North America console update this appropriately
region = 'api.amp.cisco.com'

# URL used to create new event streams
url = 'https://{}/v1/event_streams'.format(region)

# Ask the user for an event stream name
name = raw_input('Enter a name for the event stream you would like to create: ')

# All of the event type IDs
# Edit this list if you do not want all events
all_events = [1003,1004,1005,553648130,553648135,553648136,553648137,553648143,553648145,553648146,553648147,
              553648149,553648150,553648151,553648152,553648154,553648155,553648158,553648166,553648168,553648170,
              553648171,553648173,553648176,553648179,553648195,553648196,553648197,554696714,554696715,554696756,
              554696757,570425394,570425396,570425397,570425398,570425399,1090519054,1090519081,1090519084,
              1090519089,1090519096,1090519097,1090519103,1090519105,1090519107,1090524040,1090524041,1091567628,
              1091567670,1107296257,1107296258,1107296260,1107296261,1107296262,1107296263,1107296264,1107296265,
              1107296266,1107296267,1107296268,1107296269,1107296270,1107296271,1107296272,1107296273,1107296274,
              1107296275,1107296276,1107296277,1107296278,1107296279,1107296280,1107296281,1107296282,1107296283,
              1107296284,2164260866,2164260880,2164260884,2164260889,2164260892,2164260893,2164260895,
              2164260903,2164260910,2164260911,2164260914,2164260922,2164260931,2165309453,2165309495,2181038130]
			  
# Leave this list empty if you want to collect events from all groups
# Otherwise, populate it with the group guids of the groups you would like to collect events from
group_guid = []

# Set the headers for the request
headers = {'accept': 'application/json', 'content-type': 'application/json', 'Accept-Encoding': 'gzip, deflate'}

# Build the payload
payload = {"name":name,"event_type":all_events,"group_guid":group_guid}

# POST to API to create new event stream
r = requests.post(url, headers=headers, data=json.dumps(payload), auth=(client_id,api_key))

# Check if errors were returned
if r.status_code // 100 != 2:
	reason = r.json()['errors'][0]['details'][0]
	sys.exit('\nFailed to create stream: {}'.format(reason))

# Decode the returned JSON
response = r.json()

# Name the values in the JSON
data = response['data']
id = data['id']
name = data['name']
user_name = data['amqp_credentials']['user_name']
password = data['amqp_credentials']['password']
queue_name = data['amqp_credentials']['queue_name']
host = data['amqp_credentials']['host']
port = data['amqp_credentials']['port']
proto = data['amqp_credentials']['proto']

# Print the values for the new stream
print 'Stream Created Sucesfully!\n'
print '{:.<15} {}'.format('Stream Name:',name)
print '{:.<15} {}'.format('Stream ID:',id)
print '\nAMQP Credentials:'
print '{:.<15} {}'.format('User Name:',user_name)
print '{:.<15} {}'.format('Password:',password)
print '{:.<15} {}'.format('Host:',host)
print '{:.<15} {}'.format('Port:',port)
print '{:.<15} {}'.format('Queue Name:',queue_name)

# Construct the stream URL
stream_url = 'amqps://{}:{}@{}:{}'.format(user_name,password,host,port)

print '\n{}'.format(stream_url)
print '''\nNOTE: If you are writing your own client make sure to set the 'passive' and 'durable' bits True'''




