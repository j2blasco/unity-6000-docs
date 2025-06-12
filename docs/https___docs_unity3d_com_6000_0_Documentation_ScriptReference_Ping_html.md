* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ping.html

# Ping
class in UnityEngine
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
### Description
Ping any given IP address (given in dot notation).
The ping operation is asynchronous and a ping object can be polled for status using [Ping.isDone](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ping-isDone.html). When a response is received it is in [Ping.time](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ping-time.html).  
  
**Windows Store Apps** : A stream socket is used to mimic ping functionality, it will try to open a connection to specified IP address using port 80. For this to work correctly, InternetClient capability must be enabled in Package.appxmanifest.  
  
**Android** : ICMP sockets are used for ping operation if they're available, otherwise Unity spawns a child process **/system/bin/ping** for ping operations. To check if ICMP sockets are available, you need to read the contents for **/proc/sys/net/ipv4/ping** _**group** _**range**. If ICMP sockets are available, this file should contain an entry for **0 2147483647**.
### Properties
Property | Description  
---|---  
[ip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ping-ip.html) | The IP target of the ping.  
[isDone](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ping-isDone.html) | Has the ping function completed?  
[time](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ping-time.html) | This property contains the ping time result in milliseconds after isDone returns true.  
### Constructors
Constructor | Description  
---|---  
[Ping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ping-ctor.html) | Perform a ping to the supplied target IP address.  
* * *
