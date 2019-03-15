[![Gitter chat](https://img.shields.io/badge/gitter-join%20chat-brightgreen.svg)](https://gitter.im/CiscoSecurity/AMP-for-Endpoints "Gitter chat")

### AMP for Endpoints Event Stream Creator:

Script for deleting an event stream using the /v1/event_streams/{:id} endpoint documented [here](https://api-docs.amp.cisco.com/api_actions/details?api_action=DELETE+%2Fv1%2Fevent_streams%2F%7B%3Aid%7D&api_host=api.amp.cisco.com&api_resource=EventStream&api_version=v1). This script will automatically determine which AMP clound to delete the event stream from on based on the credentials. 

### Before using you must update the following:
- AMP_CLIENT_ID 
- AMP_API_KEY

### Usage:
```
python create_event_stream.py
```

### Example script output:  
```
Successfully authenticated to: North America

-=== WARNING THIS SCRIPT WILL DELETE THINGS ===-
Are you sure you want to continue? (y/n): y
 ID         Name
1692 - All Events All Groups
1819 - Threat Detected North America
2541 - Threat Quarantined Events
Enter the ID of the stream you would like to delete: 2541
Are you sure you want to continue? (y/n): y
Request to delete 2541 sent Successfully
```
