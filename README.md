[![Gitter chat](https://img.shields.io/badge/gitter-join%20chat-brightgreen.svg)](https://gitter.im/CiscoSecurity/AMP-for-Endpoints "Gitter chat")

### AMP for Endpoints Create Event Stream:

Script for creating an event stream using the /v1/event_streams endpoint documented [here](https://api-docs.amp.cisco.com/api_actions/details?api_action=POST+%2Fv1%2Fevent_streams&api_host=api.amp.cisco.com&api_resource=EventStream&api_version=v1). This script will automatically determine which AMP clound to create the event stream on based on the credentials. It also queries the /event_types API endpoint to get a current list of ALL event_type IDs at time of creation. By default, event streams created by this script will collect all events for all groups in an organization.

### Before using you must update the following:
- client_id 
- api_key

### Usage:
```
python create_event_stream.py
```

### Example script output:  
```
Sucesfully authenticated to: North America
Enter a name for the event stream you would like to create: All Groups All Events
Stream Created Sucesfully!

Stream Name:... All Groups All Events
Stream ID:..... 1474

AMQP Credentials:
User Name:..... 1474-92a4d13197b6bbeb40f0
Password:...... 0c02fc2fa59c6460833ad7e1c55c864802e9fbda
Host:.......... export-streaming.amp.cisco.com
Port:.......... 443
Queue Name:.... event_stream_1474

amqps://1474-92a4d13197b6bbeb40f0:0c02fc2fa59c6460833ad7e1c55c864802e9fbda@export-streaming.amp.cisco.com:443

NOTE: If you are writing your own client make sure to set the 'passive' and 'durable' bits True
```
