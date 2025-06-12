* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetVertexAttributeFormat.html

#  [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html).GetVertexAttributeFormat
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
public [Rendering.VertexAttributeFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttributeFormat.html) GetVertexAttributeFormat([Rendering.VertexAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttribute.html) attr); 
### Parameters
Parameter | Description  
---|---  
attr | Vertex data attribute to check for.  
### Returns
**VertexAttributeFormat** Format of the data attribute. 
### Description
Get format of a specific vertex data attribute on this Mesh.
Meshes usually use a known format for data layout, for example, a normal is a [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) by default. But meshes can use different vertex data formats, for example [colors32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-colors32.html) and [colors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-colors.html) set up vertex color in different formats. You can use this function to query this format.  
  
Additional resources: [VertexAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttribute.html), [HasVertexAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.HasVertexAttribute.html), [GetVertexAttributeDimension](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetVertexAttributeDimension.html), [GetVertexAttributes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetVertexAttributes.html).
* * *
