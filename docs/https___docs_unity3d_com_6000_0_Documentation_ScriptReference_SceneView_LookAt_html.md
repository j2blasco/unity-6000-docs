* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.LookAt.html

#  [SceneView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.html).LookAt
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
public void LookAt([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) point); 
## Declaration
public void LookAt([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) point, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) direction); 
## Declaration
public void LookAt([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) point, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) direction, float newSize); 
## Declaration
public void LookAt([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) point, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) direction, float newSize, bool ortho); 
## Declaration
public void LookAt([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) point, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) direction, float newSize, bool ortho, bool instant); 
### Parameters
Parameter | Description  
---|---  
point | The position in world space to frame.  
direction | The direction that the Scene view should view the target point from.  
newSize | The amount of camera zoom. Sets [size](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView-size.html).  
ortho | Whether the camera focus is in orthographic mode (true) or perspective mode (false).  
instant | Apply the movement immediately (true) or animate the transition (false).  
### Description
Moves the Scene view to focus on a target.
* * *
