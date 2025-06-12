* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttributeDescriptor.html

# VertexAttributeDescriptor
struct in UnityEngine.Rendering
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
Information about a single [VertexAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttribute.html) of a Mesh vertex.
[Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) vertex data comprised of different Vertex Attributes. For example, a vertex can include a Position, Normal, TexCoord0, and Color. Meshes usually use a known format for data layout, for example, a position is most often a 3-component float vector ([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)), but you can also specify non-standard data formats and their layout for a Mesh.  
  
You can use `VertexAttributeDescriptor` to specify custom mesh data layout in [Mesh.SetVertexBufferParams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetVertexBufferParams.html).  
  
Vertex data is laid out in separate "streams" (each stream goes into a separate vertex buffer in the underlying graphics API). Unity supports up to four vertex streams, but you usually use only one stream. Separate streams are most useful when some vertex attributes don't need to be processed, or you need to give the vertex attributes a specific data layout.  
  
Within each stream, attributes of a vertex are laid out one after another, in this order: [VertexAttribute.Position](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttribute.Position.html), [VertexAttribute.Normal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttribute.Normal.html), [VertexAttribute.Tangent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttribute.Tangent.html), [VertexAttribute.Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttribute.Color.html), [VertexAttribute.TexCoord0](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttribute.TexCoord0.html), ..., [VertexAttribute.TexCoord7](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttribute.TexCoord7.html), [VertexAttribute.BlendWeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttribute.BlendWeight.html), [VertexAttribute.BlendIndices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttribute.BlendIndices.html).  
  
If you include `BlendWeight` or `BlendIndices` attributes in your vertex data, use Unity's default stream layout so Unity doesn't reorder your vertex attributes or incorrectly render your vertices in a [SkinnedMeshRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinnedMeshRenderer.html). 
  1. In the first stream, add [VertexAttribute.Position](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttribute.Position.html), [VertexAttribute.Normal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttribute.Normal.html) and [VertexAttribute.Tangent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttribute.Tangent.html).
  2. In the second stream, add [VertexAttribute.Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttribute.Color.html), and [VertexAttribute.TexCoord0](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttribute.TexCoord0.html) to [VertexAttribute.TexCoord7](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttribute.TexCoord7.html).
  3. In the third stream, add [VertexAttribute.BlendWeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttribute.BlendWeight.html) and [VertexAttribute.BlendIndices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttribute.BlendIndices.html).


All the attributes in the second stream are optional. If you don't include any `Color` or `TexCoord` attributes, add `BlendWeight` and `BlendIndices` to the second stream instead.  
  
Not all [format](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttributeDescriptor-format.html) and [dimension](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttributeDescriptor-dimension.html) combinations are valid. Specifically, the data size of a vertex attribute must be a multiple of 4 bytes. For example, a [VertexAttributeFormat.Float16](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttributeFormat.Float16.html) format with dimension `3` is not valid. Additional resources: [SystemInfo.SupportsVertexAttributeFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.SupportsVertexAttributeFormat.html).
```
var mesh = new Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html)();
// specify vertex layout with:
// - floating point positions,
// - half-precision (FP16) normals with two components,
// - low precision (UNorm8) tangents
var layout = new[]
{
    new VertexAttributeDescriptor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttributeDescriptor.html)(VertexAttribute.Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttribute.Position.html), VertexAttributeFormat.Float32[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttributeFormat.Float32.html), 3),
    new VertexAttributeDescriptor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttributeDescriptor.html)(VertexAttribute.Normal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttribute.Normal.html), VertexAttributeFormat.Float16[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttributeFormat.Float16.html), 2),
    new VertexAttributeDescriptor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttributeDescriptor.html)(VertexAttribute.Tangent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttribute.Tangent.html), VertexAttributeFormat.UNorm8[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttributeFormat.UNorm8.html), 4),
};
var vertexCount = 10;
mesh.SetVertexBufferParams(vertexCount, layout);
```

A C# struct (for use with [Mesh.SetVertexBufferData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetVertexBufferData.html)) matching this vertex layout could look like this:
```
[System.Runtime.InteropServices.StructLayout(System.Runtime.InteropServices.LayoutKind.Sequential)]
struct ExampleVertex
{
    public Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) pos;
    public ushort normalX, normalY;
    public Color32[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32.html) tangent;
}
```

Additional resources: [Mesh.SetVertexBufferParams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetVertexBufferParams.html), [Mesh.SetVertexBufferData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetVertexBufferData.html), [Mesh.GetVertexAttributes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetVertexAttributes.html).
### Properties
Property | Description  
---|---  
[attribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttributeDescriptor-attribute.html) | The vertex attribute.  
[dimension](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttributeDescriptor-dimension.html) | Dimensionality of the vertex attribute.  
[format](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttributeDescriptor-format.html) | Format of the vertex attribute.  
[stream](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttributeDescriptor-stream.html) | Which vertex buffer stream the attribute should be in.  
### Constructors
Constructor | Description  
---|---  
[VertexAttributeDescriptor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttributeDescriptor-ctor.html) | Create a VertexAttributeDescriptor structure.  
* * *
