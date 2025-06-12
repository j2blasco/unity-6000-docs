* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshDeformation.GPU.html

#  [MeshDeformation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshDeformation.html).GPU
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
Enables Unity using compute shaders to process mesh deformations on the GPU.
Unity creates one dispatch call for each mesh and active blendshape. If you build for a graphics API that supports compute shaders and you render many skinned meshes, use [MeshDeformation.GPUBatched](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshDeformation.GPUBatched.html) for better performance.  
  
`MeshDeformation.GPU` works on all graphics APIs that support compute shaders, except OpenGL.
* * *
