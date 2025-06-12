* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.MarkTransformLateLatched.html

#  [XRDisplaySubsystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.html).MarkTransformLateLatched
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
public void MarkTransformLateLatched([Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) transform, [XR.XRDisplaySubsystem.LateLatchNode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.LateLatchNode.html) nodeType); 
### Parameters
Parameter | Description  
---|---  
transform | The transform of the GameObject to be late latched.  
nodeType | The late latch node type to be associated with the transform.  
### Description
This marks a given GameObject's transform to be late latched in the next frame. Once marked for late latching, the GameObject transform and its descendants will be updated with the latest VR pose updates before rendering is submitted to the GPU.
* * *
