* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeEventStream.GetEventType.html

#  [ObjectChangeEventStream](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeEventStream.html).GetEventType
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
public [ObjectChangeKind](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeKind.html) GetEventType(int eventIdx); 
### Parameters
Parameter | Description  
---|---  
eventIdx | The index of the event whose type should be returned.  
### Returns
**ObjectChangeKind** The type of the event at the specified index. 
### Description
Returns the type of the event at the specified index.
Use this function to query the type of an event before using any of the other functions (e.g. ObjectChangeEventStream.GetChangeAssetObjectEvent) to retrieve the event data.
* * *
