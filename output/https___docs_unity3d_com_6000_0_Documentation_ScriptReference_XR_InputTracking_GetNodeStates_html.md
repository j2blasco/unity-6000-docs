* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputTracking.GetNodeStates.html

#  [InputTracking](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputTracking.html).GetNodeStates
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
public static void GetNodeStates(List<XRNodeState> nodeStates); 
### Parameters
Parameter | Description  
---|---  
nodeStates | A list that is populated with [XRNodeState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRNodeState.html) objects.  
### Description
Describes all currently connected XRNodes and provides available tracking states for each.
Use this method to acquire all the currently available XR input Nodes, as an alternative to handling the node events [InputTracking.nodeAdded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputTracking-nodeAdded.html) and [InputTracking.nodeRemoved](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputTracking-nodeRemoved.html). The contents of `nodeStates` list will be cleared and replaced with fresh data.  
Not all XR platforms provide complete tracking data. Use the methods [XRNodeState.TryGetPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRNodeState.TryGetPosition.html), [XRNodeState.TryGetRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRNodeState.TryGetRotation.html), etc. to read the data if it's available.
* * *
