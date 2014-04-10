syslog-generator
================

Generates syslog messages from a user defined file and sends them to a remote host. 

### Functionality
This script generates random hostnames, syslog levels, and tags to be used in a message. The variables and data structures can be modified to fit your needs by changing them towards the top of the script. The script also randomly pulls messages from a user defined file to provide variety to log data.  

### Usage
This script is written for Python 3+ and is meant to be run from the command line.

#### Required Arguments

* --host: IP or hostname to send syslog messages.
* --port: UDP port to send syslog messages.  
* --file: Filename to read syslog messasges from. This file should contain ONLY the text of the message. Syslog format is handled by the script. 
* --count: Number of messages to send at one time. 

#### Optional Arguments

* --sleep: Number of seconds to sleep until the next batch of messages is sent. Using this argument continues the script indefinitely or until the CTRL-C combination is invoked.  

#### Example

Send 10 messages at once:
```
syslog_gen.py --host 192.168.1.100 --port 514 --file sample_logs --count 10 
```

Send 10 messages every 30 seconds:
```
syslog_gen.py --host 192.168.1.100 --port 514 --file sample_logs --count 10 --sleep 30 
```
