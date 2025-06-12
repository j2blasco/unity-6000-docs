* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttributeDescriptor-ctor.html

# VertexAttributeDescriptor Constructor
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
public VertexAttributeDescriptor([Rendering.VertexAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttribute.html) attribute, [Rendering.VertexAttributeFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttributeFormat.html) format, int dimension, int stream); 
### Parameters
Parameter | Description  
---|---  
attribute | The [VertexAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttribute.html).  
format | Format of the vertex attribute. Default is [VertexAttributeFormat.Float32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttributeFormat.Float32.html).  
dimension | Dimensionality of the vertex attribute (1 to 4). Default is 3.  
stream | Vertex buffer stream that the attribute should be placed in. Default is 0.  
### Description
Create a [VertexAttributeDescriptor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttributeDescriptor.html) structure.
Additional resources: [Mesh.SetVertexBufferParams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetVertexBufferParams.html), [Mesh.GetVertexAttributes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetVertexAttributes.html).
* * *
