### AMP for Endpoints Event Stream Creator

Simple script for creating an event stream using the /v1/event_streams endpoint documented [here](https://api-docs.amp.cisco.com/api_actions/details?api_action=POST+%2Fv1%2Fevent_streams&api_host=api.amp.cisco.com&api_resource=EventStream&api_version=v1)

Before using you must update the following:
- Line 6: client_id 
- Line 9: api_key

If you're not provisioned in the North American console you must also change line 12

Example script output:  
```
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
