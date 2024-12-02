## About the connector
Perform actions like Get incident details, Retrieve incidents, Close Incidents and Create Alert from JSON source using Proofpoint TRAP
<p>This document provides information about the Proofpoint TRAP Connector, which facilitates automated interactions, with a Proofpoint TRAP server using FortiSOAR&trade; playbooks. Add the Proofpoint TRAP Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Proofpoint TRAP.</p>

### Version information

Connector Version: 1.1.0


Authored By: Fortinet

Certified: No
## Release Notes for version 1.1.0
Following enhancements have been made to the Proofpoint TRAP Connector in version 1.1.0:
<ul>
<li>New action: Close Incidents, Execute an API Request </li>
<li>Updated Get Incidents action</li>
<li><p>In Get Incidents action: </p>

<ul>
<li>Removed Closed After Date and Cclosed Before Date parameter</li>
<li>Added Close Summary and Email Message ID parameter</li>
</ul></li>
</ul>

## Installing the connector
<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>
<pre>yum install cyops-connector-proofpoint-trap</pre>

## Prerequisites to configuring the connector
- You must have the credentials of Proofpoint TRAP server to which you will connect and perform automated operations.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Proofpoint TRAP server.

## Minimum Permissions Required
- Not applicable

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Proofpoint TRAP</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server Address</td><td>URL of the Proofpoint TRAP server to which you will connect and perform automated operations.
</td>
</tr><tr><td>API Token</td><td>Specify the API Token that you have generated in Proofpoint TRAP application
</td>
</tr><tr><td>Verify SSL</td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set to True.</td></tr>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Create Alert from JSON Source</td><td>Creates ProofPoint Alert based on Alert Source ID and other parameters provided</td><td>create_alert_from_json_source <br/>Investigation</td></tr>
<tr><td>Get Incident Details</td><td>Retrieves incident details based on the incident ID and other parameters provided</td><td>get_incident_details <br/>Investigation</td></tr>
<tr><td>Get Incidents</td><td>Retrieves all Incident details based on the parameters provided</td><td>get_incidents <br/>Investigation</td></tr>
<tr><td>Close Incidents</td><td>Closes the Incident on the basis of given TRAP incident IDs</td><td>close_incidents <br/>Investigation</td></tr>
<tr><td>Execute an API Request</td><td>Sends an API request to any API endpoint based on specified HTTP method, endpoint, and other input parameters that you have specified, enabling flexible API interactions tailored to user needs. </td><td>execute_api_request <br/>Investigation</td></tr>
</tbody></table>

### operation: Create Alert from JSON Source
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Alert Source ID</td><td>Specify the Alert Source ID of which you want to create the alert
</td></tr><tr><td>Data</td><td>Specify the Alert Data of which you want to create the alert
</td></tr></tbody></table>

#### Output

 No output schema is available at this time.

### operation: Get Incident Details
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Incident ID</td><td>Specify the Incident ID whose details you want to fetch
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "id": "",
    "type": "",
    "summary": "",
    "description": "",
    "score": "",
    "state": "",
    "created_at": "",
    "false_positive_count": "",
    "event_count": "",
    "event_sources": [],
    "users": [],
    "assignee": "",
    "team": "",
    "hosts": {},
    "incident_field_values": [],
    "events": [],
    "comments": [],
    "quarantine_results": [],
    "successful_quarantines": "",
    "failed_quarantines": "",
    "pending_quarantines": ""
}</pre>

### operation: Get Incidents
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>State</td><td>Select state of the incident
</td></tr><tr><td>Created After Date</td><td>Retrieve incidents that were created after specified date, in ISO 8601 format (UTC)
</td></tr><tr><td>Created Before Date</td><td>Retrieve incidents that were created before specified date, in ISO 8601 format (UTC)
</td></tr><tr><td>Email Message ID</td><td>Specify comma separated value of multiple message-ids.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "result": "",
    "api_data": ""
}</pre>

### operation: Close Incidents
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Incident IDs</td><td>Specify the comma separated values of Incidents IDs which you want to Close
</td></tr><tr><td>Close Summary</td><td>Specify the Closing summary to be placed into each closed incident.
</td></tr><tr><td>Close Detail</td><td>Specify the Closing details to be placed into each closed incident.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.

### operation: Execute an API Request
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>HTTP Method</td><td>Select an HTTP action for the request. You can select from the following options:  

DELETE 

GET 

PATCH 

POST 

PUT 
</td></tr><tr><td>Endpoint</td><td>Specify the target endpoint for the request like /api/incidents/
</td></tr><tr><td>Query Parameters</td><td>(Optional) Specify any optional parameters to add to the URL and refine the request.
</td></tr><tr><td>Request Payload</td><td>(Optional) Specify data, as JSON, to be sent as the request payload (typically for POST or PUT requests). 
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
## Included playbooks
The `Sample - proofpoint-trap - 1.1.0` playbook collection comes bundled with the Proofpoint TRAP connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR&trade; after importing the Proofpoint TRAP connector.

- Close Incidents
- Create Alert from JSON Source
- Execute an API Request
- Get Incident Details
- Get Incidents

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.
