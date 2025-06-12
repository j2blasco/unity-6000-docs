* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRNode.html

# XRNode
enumeration
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
Enumeration of XR nodes which can be updated by XR input or sent haptic data.
**Note:** The types GameController, TrackingReference, and HardwareTracker are considered non-singleton nodes, as there can be many of each available. As a result, InputTracking.GetLocalPosition, and InputTracking.GetLocalRotation will not work with those values. Please use [InputTracking.GetNodeStates](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputTracking.GetNodeStates.html) instead. **Note:** Only XR nodes with valid haptic devices as endpoints can be sent haptic data.
### Properties
Property | Description  
---|---  
[LeftEye](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRNode.LeftEye.html) | Node representing the left eye.  
[RightEye](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRNode.RightEye.html) | Node representing the right eye.  
[CenterEye](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRNode.CenterEye.html) | Node representing a point between the left and right eyes.  
[Head](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRNode.Head.html) | Node representing the user's head.  
[LeftHand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRNode.LeftHand.html) | Node representing the left hand.  
[RightHand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRNode.RightHand.html) | Node representing the right hand.  
[GameController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRNode.GameController.html) | Represents a tracked game Controller not associated with a specific hand.  
[TrackingReference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRNode.TrackingReference.html) | Represents a stationary physical device that can be used as a point of reference in the tracked area.  
[HardwareTracker](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRNode.HardwareTracker.html) | Represents a physical device that provides tracking data for objects to which it is attached.  
* * *
