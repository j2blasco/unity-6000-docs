* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshDeformation.GPUBatched.html

#  [MeshDeformation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshDeformation.html).GPUBatched
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
Enables Unity using compute shaders to process mesh deformations on the GPU, and combining multiple meshes and blendshapes into batches.
If you enable this property, Unity uses batching and reordering to combine meshes and blendshapes into fewer dispatch calls to the GPU.   
  
Batching provides better performance on high-end platforms. Unity can process multiple meshes more quickly and reduce synchronisation issues. On other platforms, you might need to use [MeshDeformation.GPU](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshDeformation.GPU.html) instead, because batching uses dynamic branching which has a high resource intensity.  
  
Unity uses batching if the following applies: 
  * The Graphics API supports batching.
  * You process 3 or more batchable meshes in one frame - this is the number of meshes where batching usually becomes faster than [non-batched GPU skinning](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshDeformation.GPU.html).


To make sure a mesh is batchable, check the mesh is compatible with standard non-batched GPU skinning, and that its vertex data layout exactly matches one of the following: 
  * position
  * position, normal
  * position, normal, tangent


If Unity can't use batching, it reverts to non-batched GPU skinning. 
* * *
