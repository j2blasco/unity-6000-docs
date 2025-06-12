* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttributeDescriptor-stream.html

#  [VertexAttributeDescriptor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttributeDescriptor.html).stream
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
stream; 
### Description
Which vertex buffer stream the attribute should be in.
Unity supports up to 4 vertex streams, most meshes use one stream for all attributes. Default value is 0.  
  
For a mesh to be compatible with a [SkinnedMeshRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinnedMeshRenderer.html), it must have multiple vertex streams: one for deformed data (positions, normals, tangents), one for static data (colors and texture coordinates), and one for skinning data (blend weights and blend indices).  
  
Additional resources: [Mesh.SetVertexBufferParams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetVertexBufferParams.html).
* * *
