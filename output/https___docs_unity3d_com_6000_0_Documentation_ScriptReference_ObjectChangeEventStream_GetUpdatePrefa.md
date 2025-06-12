* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeEventStream.GetUpdatePrefabInstancesEvent.html

#  [ObjectChangeEventStream](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeEventStream.html).GetUpdatePrefabInstancesEvent
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
public void GetUpdatePrefabInstancesEvent(int eventIdx, out [UpdatePrefabInstancesEventArgs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UpdatePrefabInstancesEventArgs.html) data); 
### Parameters
Parameter | Description  
---|---  
eventIdx | The index of the event to get the data for.  
data | The data associated with the event.  
### Description
Retrieves the event data at the given index as a [UpdatePrefabInstancesEventArgs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UpdatePrefabInstancesEventArgs.html). Throws an exception if the event type requested does not match the event stored in the stream.
* * *
