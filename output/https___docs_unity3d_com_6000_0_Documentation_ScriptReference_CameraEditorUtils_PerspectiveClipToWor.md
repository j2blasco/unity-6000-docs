* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditorUtils.PerspectiveClipToWorld.html

#  [CameraEditorUtils](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditorUtils.html).PerspectiveClipToWorld
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
public static [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) PerspectiveClipToWorld([Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) clipToWorld, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) viewPositionWS, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) positionCS); 
### Parameters
Parameter | Description  
---|---  
clipToWorld | Clip to world matrix to use.  
viewPositionWS | The viewer's position in world space.  
positionCS | The position in clip space.  
### Returns
**Vector3** The corresponding world space position. 
### Description
Calculate the world space position of a point in clip space.  
  
The z component will be used to get the point at the distance z from the viewer.
* * *
