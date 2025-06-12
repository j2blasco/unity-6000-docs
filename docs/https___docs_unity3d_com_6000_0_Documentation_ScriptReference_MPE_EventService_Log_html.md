* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.EventService.Log.html

#  [EventService](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.EventService.html).Log
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
## Declaration
public static void Log(string msg); 
## Declaration
public static void Log(string msg, [LogType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LogType.html) logType); 
### Parameters
Parameter | Description  
---|---  
msg | The message to send.  
logType | The type of the message (i.e. Info, Warning or Error).  
### Description
Sends a log message to the [ChannelService](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.html). Log messages are printed to the Console window.
* * *
