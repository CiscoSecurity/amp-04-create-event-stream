import sys
import json
import requests

def verify_auth():
    """ Verify which AMP cloud the provided client_id and api_key are valid for.
        Return the Domain and Region Name for the cloud the credentials are valid in.
    """
    region_domains = {'api.amp.cisco.com':'North America',
                      'api.apjc.amp.cisco.com':'Asia',
                      'api.eu.amp.cisco.com':'Europe'
                     }

    for named_domain in region_domains:
        version_url = 'https://{}/v1/version'.format(named_domain)
        request = session.get(version_url)

        if request.status_code == 200:
            return named_domain, region_domains[named_domain]

    sys.exit('It doesn\'t look like the credentials you provided are valid in any region')

# 3rd Party API Client ID
client_id = 'a1b2c3d4e5f6g7h8i9j0'

# API Key
api_key = 'a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6'

# Set the headers for the requests
headers = {'accept': 'application/json',
           'content-type': 'application/json',
           'Accept-Encoding': 'gzip, deflate'}

# Creat a session object and update the auth and headers
session = requests.session()
session.auth = (client_id, api_key)
session.headers.update(headers)

# Check which cloud the credentials are valid in
domain, region = verify_auth()

# Output which region will be used
print('Sucesfully authenticated to: {}\n'.format(region))

# URL used to create new event streams
event_streams_url = 'https://{}/v1/event_streams'.format(domain)
event_types_url = 'https://{}/v1/event_types'.format(domain)

# Query the event_types API endpoint to get a list of all event types
# If you would like to specify only some event types remove the comprehension and enter them manualy
all_events = [event['id'] for event in session.get(event_types_url).json()['data']]

# Ask the user for an event stream name
name = input('Enter a name for the event stream you would like to create: ')

# Leave this list empty if you want to collect events from all groups
# Otherwise, populate it with the group guids of the groups you would like to collect events from
group_guid = []

# Build the payload
payload = {"name":name, "event_type":all_events, "group_guid":group_guid}

# POST to API to create new event stream
post_req = session.post(event_streams_url, data=json.dumps(payload))

# Check if errors were returned
if post_req.status_code // 100 != 2:
    reason = post_req.json()['errors'][0]['details'][0]
    sys.exit('\nFailed to create stream: {}'.format(reason))

# Decode the returned JSON
response = post_req.json()

# Name the values in the JSON
data = response['data']
stream_id = data['id']
name = data['name']
user_name = data['amqp_credentials']['user_name']
password = data['amqp_credentials']['password']
queue_name = data['amqp_credentials']['queue_name']
host = data['amqp_credentials']['host']
port = data['amqp_credentials']['port']
proto = data['amqp_credentials']['proto']

# Print the values for the new stream
print('Stream Created Sucesfully!\n')
print('{:.<15} {}'.format('Stream name:', name))
print('{:.<15} {}'.format('Stream ID:', stream_id))
print('\nAMQP Credentials:')
print('{:.<15} {}'.format('User Name:', user_name))
print('{:.<15} {}'.format('Password:', password))
print('{:.<15} {}'.format('Host:', host))
print('{:.<15} {}'.format('Port:', port))
print('{:.<15} {}'.format('Queue Name:', queue_name))

# Construct the stream URL
stream_url = 'amqps://{}:{}@{}:{}'.format(user_name, password, host, port)

print('\n{}'.format(stream_url))
print('''\nNOTE: If you are writing your own client make sure to set the 'passive' and 'durable' bits True''')
