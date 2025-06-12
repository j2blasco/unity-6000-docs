* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.EventService.Emit.html

#  [EventService](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.EventService.html).Emit
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
public static void Emit(string eventType, object args, int targetId, [MPE.EventDataSerialization](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.EventDataSerialization.html) eventDataSerialization); 
## Declaration
public static void Emit(string eventType, object[] args, int targetId, [MPE.EventDataSerialization](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.EventDataSerialization.html) eventDataSerialization); 
### Parameters
Parameter | Description  
---|---  
eventType | The message's type name.  
args | The arguments sent with the message.  
targetId | When you send the event to a specific connection, this is the connection ID. By default it is set to -1, which sends the message to all other EventServices.  
eventDataSerialization | Specifies how to serialize the request's arguments. This can be standard JSON, or JSON annotated with JsonUtility. You can use the latter to convert the argument to a concrete Unity object that supports [JsonUtility.FromJson](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JsonUtility.FromJson.html).  
### Description
Sends a fire-and-forget message to all [ChannelClient](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelClient.html)s connected to the "events" route.
* * *
