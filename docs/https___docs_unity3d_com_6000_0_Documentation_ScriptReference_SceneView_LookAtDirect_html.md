* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.LookAtDirect.html

#  [SceneView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.html).LookAtDirect
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
public void LookAtDirect([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) point, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) direction); 
## Declaration
public void LookAtDirect([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) point, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) direction, float newSize); 
### Parameters
Parameter | Description  
---|---  
point | The position in world space to frame.  
direction | The direction from which the Scene view should view the point.  
newSize | The amount of camera zoom. Sets [size](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView-size.html).  
### Description
[LookAt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.LookAt.html) without animating the scene movement.
* * *
