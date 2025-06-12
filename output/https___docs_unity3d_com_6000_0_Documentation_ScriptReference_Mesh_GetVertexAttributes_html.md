* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetVertexAttributes.html

#  [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html).GetVertexAttributes
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
public VertexAttributeDescriptor[] GetVertexAttributes(); 
### Returns
**VertexAttributeDescriptor[]** Array of vertex attribute information. 
### Description
Get information about vertex attributes of a Mesh.
Many of mesh vertex data attributes are optional, for example a mesh might contain only vertex positions, normals and one UV coordinate. Each attribute might use a different data type for storage. Use this function to query information about all attributes that describe vertices of this Mesh.  
  
The returned array contains as many elements as there are vertex attributes. For example, if a Mesh has [position](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-vertices.html) and [normals](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-normals.html) set up, but no other attributes, then the returned array will have two elements (one describing position, the other describing normal).  
  
Additional resources: [VertexAttributeDescriptor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttributeDescriptor.html), [HasVertexAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.HasVertexAttribute.html), [SetVertexBufferParams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetVertexBufferParams.html).
* * *
## Declaration
public int GetVertexAttributes(VertexAttributeDescriptor[] attributes); 
## Declaration
public int GetVertexAttributes(List<VertexAttributeDescriptor> attributes); 
### Parameters
Parameter | Description  
---|---  
attributes | Collection of vertex attributes to receive the results.  
### Returns
**int** The number of vertex attributes returned in the attributes container. 
### Description
Get information about vertex attributes of a Mesh, without memory allocations.
Use these overloads of the `GetVertexAttributes` function to avoid having to allocate a new array each time the function is called. The `List` variant only allocates memory if the list does not have enough capacity to hold all the vertex attributes. The array variant never allocates memory; if the array is too small then only a part of all the vertex attributes is returned.  
  
Alternative way to query vertex attributes that does not need any memory allocations at all, is to use [vertexAttributeCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-vertexAttributeCount.html) and [GetVertexAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetVertexAttribute.html) functions.
* * *
