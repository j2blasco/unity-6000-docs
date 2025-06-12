* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.HasVertexAttribute.html

#  [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html).HasVertexAttribute
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
public bool HasVertexAttribute([Rendering.VertexAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttribute.html) attr); 
### Parameters
Parameter | Description  
---|---  
attr | Vertex data attribute to check for.  
### Returns
**bool** Returns true if the data attribute is present in the mesh. 
### Description
Checks if a specific vertex data attribute exists on this Mesh.
Most of possible mesh vertex data attributes are optional, for example a mesh might contain only vertex positions, normals and one UV coordinate. HasVertexAttribute check for these attributes will return true in that case, and will return false for all other attributes.  
  
Additional resources: [VertexAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttribute.html), [GetVertexAttributeDimension](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetVertexAttributeDimension.html), [GetVertexAttributes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetVertexAttributes.html).
* * *
