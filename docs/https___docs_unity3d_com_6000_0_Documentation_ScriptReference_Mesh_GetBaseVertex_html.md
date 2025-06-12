* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetBaseVertex.html

#  [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html).GetBaseVertex
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Mesh.html "Go to Mesh Component in the Manual")
## Declaration
public uint GetBaseVertex(int submesh); 
### Parameters
Parameter | Description  
---|---  
submesh | The sub-mesh index. See [subMeshCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-subMeshCount.html).  
### Returns
**uint** The offset applied to all vertex indices of this sub-mesh. 
### Description
Gets the base vertex index of the given `sub-mesh`.
The base vertex can be used to achieve meshes that are larger than 65535 vertices while using 16 bit index buffers, as long as each sub-mesh fits within its own 65535 vertex area. Alternatively, 32 bit index buffers can be used via [indexFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-indexFormat.html).  
  
Additional resources: [SetIndices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetIndices.html).
* * *
