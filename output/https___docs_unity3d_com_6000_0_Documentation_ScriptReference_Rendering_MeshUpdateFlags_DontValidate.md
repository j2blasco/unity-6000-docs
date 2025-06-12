* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.DontValidateIndices.html

#  [MeshUpdateFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.html).DontValidateIndices
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
Indicates that Unity should not check index values when you use [Mesh.SetIndexBufferData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetIndexBufferData.html) to modify a Mesh's data.
When you use [Mesh.SetIndexBufferData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetIndexBufferData.html) to modify a Mesh's data, Unity's default behaviour is to validate the indices array that you supplied, to check for out-of-bounds index values. Unity throws an exception if it finds any.  
  
You can make Unity skip these checks by using the `MeshUpdateFlags.DontValidateIndices` flag. This can be beneficial to performance, however if you use this flag you must make sure that you pass valid data to the Mesh.  
  
Additional resources: [Mesh.SetIndexBufferData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetIndexBufferData.html).
* * *
