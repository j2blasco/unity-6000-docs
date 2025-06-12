* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.LookAt.html

#  [Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html).LookAt
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
public static [Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) LookAt([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) from, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) to, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) up); 
### Parameters
Parameter | Description  
---|---  
from | The source point.  
to | The target point.  
up | The vector describing the up direction (typically [Vector3.up](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html)).  
### Returns
**Matrix4x4** The resulting transformation matrix. 
### Description
Create a "look at" matrix.
Given a source point, a target point, and an up vector, computes a transformation matrix that corresponds to a camera viewing the target from the source, such that the right-hand vector is perpendicular to the up vector.  
  
The resulting matrix corresponds to `Matrix4x4.TRS(from, Quaternion.LookRotation(to-from, up), Vector3.one)`.  
  
Additional resources: [Matrix4x4.TRS](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.TRS.html), [Quaternion.LookRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.LookRotation.html), [Camera.worldToCameraMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-worldToCameraMatrix.html), [CommandBuffer.SetViewMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetViewMatrix.html).
* * *
