* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.Eyes.html

# Eyes
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
Contains eye tracking data from the device at an [XRNode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRNode.html) in the XR input subsystem.
Represents eye tracking data collected by the device. The Eyes type contains eye position, rotation, and data indicating the eye fixation point and blink values for both the left and right eye. All eye spatial information is in the Unity coordinate space.
### Public Methods
Method | Description  
---|---  
[TryGetFixationPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.Eyes.TryGetFixationPoint.html) | Gets the point represents the convergence of the line of sight for both eyes.  
[TryGetLeftEyeOpenAmount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.Eyes.TryGetLeftEyeOpenAmount.html) | Gets a value that represents the how far the left eye is open.  
[TryGetLeftEyePosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.Eyes.TryGetLeftEyePosition.html) | Gets the Vector3 that describes the position of the left eye.  
[TryGetLeftEyeRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.Eyes.TryGetLeftEyeRotation.html) | Gets the Quaternion that describes the rotation of the left eye.  
[TryGetRightEyeOpenAmount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.Eyes.TryGetRightEyeOpenAmount.html) | Gets a value that represents the how far the right eye is open.  
[TryGetRightEyePosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.Eyes.TryGetRightEyePosition.html) | Gets the Vector3 that describes the position of the right eye.  
[TryGetRightEyeRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.Eyes.TryGetRightEyeRotation.html) | Gets the Quaternion that describes the rotation of the right eye.  
* * *
