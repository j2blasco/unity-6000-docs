* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetVertexAttributeOffset.html

#  [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html).GetVertexAttributeOffset
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
public int GetVertexAttributeOffset([Rendering.VertexAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttribute.html) attr); 
### Parameters
Parameter | Description  
---|---  
attr | The vertex data attribute to check for.  
### Returns
**int** The byte offset within a atream of the data attribute, or -1 if it is not present. 
### Description
Get offset within a vertex buffer stream of a specific vertex data attribute on this Mesh.
Meshes usually use a single vertex buffer stream, but it is possible to set up a vertex layout where attributes use different vertex buffers (see [SetVertexBufferParams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetVertexBufferParams.html)). When you use such a layout, use this function to query where a given attribute is located in a stream.  
  
Note that this function returns the byte offset within a stream, without specifying which stream. To identify the stream that contains a given attribute, use [GetVertexAttributeStream](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetVertexAttributeStream.html).
```
using UnityEngine;
using UnityEngine.Rendering;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Create a Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) with custom vertex data layout:
        // position and normal go into stream 0,
        // color goes into stream 1.
        var mesh = new Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html)();
        mesh.SetVertexBufferParams(10,
            new VertexAttributeDescriptor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttributeDescriptor.html)(VertexAttribute.Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttribute.Position.html), VertexAttributeFormat.Float32[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttributeFormat.Float32.html), 3, stream:0),
            new VertexAttributeDescriptor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttributeDescriptor.html)(VertexAttribute.Normal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttribute.Normal.html), VertexAttributeFormat.Float32[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttributeFormat.Float32.html), 3, stream:0),
            new VertexAttributeDescriptor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttributeDescriptor.html)(VertexAttribute.Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttribute.Color.html), VertexAttributeFormat.UNorm8[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttributeFormat.UNorm8.html), 4, stream:1));  
  
        // Prints offsets: 0, 12, 0
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Position.html) offset {mesh.GetVertexAttributeOffset(VertexAttribute.Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttribute.Position.html))}");
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Normal offset {mesh.GetVertexAttributeOffset(VertexAttribute.Normal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttribute.Normal.html))}");
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) offset {mesh.GetVertexAttributeOffset(VertexAttribute.Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttribute.Color.html))}");  
  
        // Cleanup
        Object.DestroyImmediate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DestroyImmediate.html)(mesh);
    }
}

```

Additional resources: [VertexAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttribute.html), [HasVertexAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.HasVertexAttribute.html), [GetVertexAttributeStream](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetVertexAttributeStream.html), [vertexBufferCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-vertexBufferCount.html), [GetVertexBufferStride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetVertexBufferStride.html).
* * *
