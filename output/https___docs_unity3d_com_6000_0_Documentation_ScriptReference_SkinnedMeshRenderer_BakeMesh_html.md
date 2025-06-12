* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinnedMeshRenderer.BakeMesh.html

#  [SkinnedMeshRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinnedMeshRenderer.html).BakeMesh
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-SkinnedMeshRenderer.html "Go to SkinnedMeshRenderer Component in the Manual")
## Declaration
public void BakeMesh([Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh); 
## Declaration
public void BakeMesh([Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh, bool useScale); 
### Parameters
Parameter | Description  
---|---  
mesh | A static mesh that will receive the snapshot of the skinned mesh.  
useScale | Whether to compensate for the SkinnedMeshRenderer's Transform scale. If true, the baked Mesh is the same size as the original. If false, the baked Mesh matches the scaling of the SkinnedMeshRenderer's Transform component. The default value is false.  
### Description
Creates a snapshot of SkinnedMeshRenderer and stores it in `mesh`.
The vertices are relative to the SkinnedMeshRenderer Transform component.  
This function always compensates for the position and rotation values of the Transform component with the origin of the baked mesh always the same as the origin of the original mesh.  
  
**Notes** :  
The snapshot is still computed even when [updateWhenOffscreen](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinnedMeshRenderer-updateWhenOffscreen.html) is set to false and the skinned mesh object is currently offscreen.  
When this function is called the skinning process will always take place on the CPU, regardless of the [GPU Skinning](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings-gpuSkinning.html) setting.
* * *
