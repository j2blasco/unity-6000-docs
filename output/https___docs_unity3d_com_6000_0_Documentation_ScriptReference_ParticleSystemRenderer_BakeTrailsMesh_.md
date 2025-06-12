* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.BakeTrailsMesh.html

#  [ParticleSystemRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.html).BakeTrailsMesh
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
public void BakeTrailsMesh([Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh, [ParticleSystemBakeMeshOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemBakeMeshOptions.html) options); 
## Declaration
public void BakeTrailsMesh([Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh, [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) camera, [ParticleSystemBakeMeshOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemBakeMeshOptions.html) options); 
**Obsolete** BakeTrailsMesh with useTransform is deprecated. Use BakeTrailsMesh with ParticleSystemBakeMeshOptions instead.
## Declaration
public void BakeTrailsMesh([Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh, bool useTransform); 
**Obsolete** BakeTrailsMesh with useTransform is deprecated. Use BakeTrailsMesh with ParticleSystemBakeMeshOptions instead.
## Declaration
public void BakeTrailsMesh([Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh, [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) camera, bool useTransform); 
### Parameters
Parameter | Description  
---|---  
mesh | A static Mesh to receive the snapshot of the particle trails.  
camera | The Camera used to determine which way camera-space trails face.  
options | Specifies whether to include the rotation and scale of the Transform in the baked Mesh.  
useTransform | Specifies whether to include the rotation and scale of the Transform in the baked Mesh.  
### Description
Creates a snapshot of ParticleSystem Trails and stores them in a `mesh`.
* * *
