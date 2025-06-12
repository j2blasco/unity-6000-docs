* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TrailRenderer.BakeMesh.html

#  [TrailRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TrailRenderer.html).BakeMesh
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TrailRenderer.html "Go to TrailRenderer Component in the Manual")
## Declaration
public void BakeMesh([Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh, bool useTransform); 
## Declaration
public void BakeMesh([Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh, [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) camera, bool useTransform); 
### Parameters
Parameter | Description  
---|---  
mesh | A static mesh that will receive the snapshot of the trail.  
camera | The camera used for determining which way camera-space trails will face.  
useTransform | Include the rotation and scale of the Transform in the baked mesh.  
### Description
Creates a snapshot of TrailRenderer and stores it in `mesh`.
* * *
