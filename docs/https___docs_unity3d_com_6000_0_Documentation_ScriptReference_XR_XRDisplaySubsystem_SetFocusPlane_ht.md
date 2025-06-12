* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.SetFocusPlane.html

#  [XRDisplaySubsystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.html).SetFocusPlane
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
public void SetFocusPlane([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) point, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) normal, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) velocity); 
### Parameters
Parameter | Description  
---|---  
point | The position of the focal point in the Scene, relative to the Camera.  
normal | Surface normal of the plane being viewed at the focal point.  
velocity | A vector that describes how the focus point moves in the Scene at this point in time. This allows the device to compensate for both your head movement and the movement of the object in the Scene.  
### Description
Sets a point in 3D space that acts as the focal point of the Scene for this frame. This helps to improve the visual fidelity of content around this point. You must set this value every frame.  
  
Note that specifying body-locked content in focus improves the fidelity of body-locked content at the expense of content not locked to the body. This is especially apparent when the user moves. 
* * *
