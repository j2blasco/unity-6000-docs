* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings-meshDeformation.html

#  [PlayerSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.html).meshDeformation
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html "Go to PlayerSettings Component in the Manual")
[MeshDeformation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshDeformation.html) meshDeformation; 
### Description
Specifies which method Unity uses to process mesh deformations for skinning.
If set to [MeshDeformation.CPU](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshDeformation.CPU.html), Unity uses the CPU to process mesh deformations.  
  
If set to [MeshDeformation.GPU](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshDeformation.GPU.html), Unity uses compute shaders to process mesh deformations on the GPU, and creates one dispatch call for each mesh and active blendshape. If you build for a graphics API that supports compute shaders and you render many skinned meshes, use [MeshDeformation.GPUBatched](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshDeformation.GPUBatched.html) for better performance.  
  
If set to [MeshDeformation.GPUBatched](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshDeformation.GPUBatched.html), Unity uses compute shaders to process mesh deformations on the GPU, and combines multiple meshes and blendshapes into batches. See [MeshDeformation.GPUBatched](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshDeformation.GPUBatched.html) for more information.  
  
The default value is [MeshDeformation.GPUBatched](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshDeformation.GPUBatched.html). 
* * *
