* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRNodeState.html

# XRNodeState
struct in UnityEngine.XR
/
Implemented in:[UnityEngine.XRModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.XRModule.html)
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
Describes the state of a node tracked by an XR system.
To track available XR nodes and acquire state data, handle the [InputTracking.nodeAdded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputTracking-nodeAdded.html) and [InputTracking.nodeRemoved](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputTracking-nodeRemoved.html) events or call [InputTracking.GetNodeStates](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputTracking.GetNodeStates.html).  
Not all XR platforms provide complete tracking data. Use the methods [XRNodeState.TryGetPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRNodeState.TryGetPosition.html), [XRNodeState.TryGetRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRNodeState.TryGetRotation.html), etc. to read the data if it's available.  
  
XR devices can be accessed in different ways, with the XR Node representing a physical input source such as a head position, hand, or camera.  
See [XR Input](https://docs.unity3d.com/6000.0/Documentation/Manual/xr_input.html) for an overview of accessing XR devices. 
### Properties
Property | Description  
---|---  
[acceleration](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRNodeState-acceleration.html) | Sets the vector representing the current acceleration of the tracked node.  
[angularAcceleration](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRNodeState-angularAcceleration.html) | Sets the vector representing the current angular acceleration of the tracked node.  
[angularVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRNodeState-angularVelocity.html) | Sets the vector representing the current angular velocity of the tracked node.  
[nodeType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRNodeState-nodeType.html) | The type of the tracked node as specified in XRNode.  
[position](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRNodeState-position.html) | Sets the vector representing the current position of the tracked node.  
[rotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRNodeState-rotation.html) | Sets the quaternion representing the current rotation of the tracked node.  
[tracked](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRNodeState-tracked.html) |  Set to true if the node is presently being tracked by the underlying XR system, and false if the node is not presently being tracked by the underlying XR system.  
[uniqueID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRNodeState-uniqueID.html) | The unique identifier of the tracked node.  
[velocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRNodeState-velocity.html) | Sets the vector representing the current velocity of the tracked node.  
### Public Methods
Method | Description  
---|---  
[TryGetAcceleration](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRNodeState.TryGetAcceleration.html) | Attempt to retrieve a vector representing the current acceleration of the tracked node.  
[TryGetAngularAcceleration](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRNodeState.TryGetAngularAcceleration.html) | Attempt to retrieve a Vector3 representing the current angular acceleration of the tracked node.  
[TryGetAngularVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRNodeState.TryGetAngularVelocity.html) | Attempt to retrieve a Vector3 representing the current angular velocity of the tracked node.  
[TryGetPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRNodeState.TryGetPosition.html) | Attempt to retrieve a vector representing the current position of the tracked node.  
[TryGetRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRNodeState.TryGetRotation.html) | Attempt to retrieve a quaternion representing the current rotation of the tracked node.  
[TryGetVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRNodeState.TryGetVelocity.html) | Attempt to retrieve a vector representing the current velocity of the tracked node.  
* * *
