* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.EventService.Request.html

#  [EventService](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.EventService.html).Request
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
public static void Request(string eventType, Action<Exception,object[]> promiseHandler, object args, long timeoutInMs, [MPE.EventDataSerialization](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.EventDataSerialization.html) eventDataSerialization); 
## Declaration
public static void Request(string eventType, Action<Exception,object[]> promiseHandler, object[] args, long timeoutInMs, [MPE.EventDataSerialization](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.EventDataSerialization.html) eventDataSerialization); 
### Parameters
Parameter | Description  
---|---  
eventType | The request's event type name.  
promiseHandler | The handler called when the Request is either fulfilled or cancelled, or times out.  
args | Arguments sent with the request event.  
timeoutInMs | The timeout value in milliseconds. After this amount of time passes the Request is considered to be cancelled.  
eventDataSerialization | Specifies how to serialize the request's arguments. This can be standard JSON, or JSON annotated with JsonUtility. You can use the latter to convert the argument to a concrete Unity object that supports [JsonUtility.FromJson](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JsonUtility.FromJson.html).  
### Description
Sends a request to all connected clients on the "events" channel.
Any client can attempt fulfill the request but only the first client that acknowledges the request can actually fulfill it.
* * *
