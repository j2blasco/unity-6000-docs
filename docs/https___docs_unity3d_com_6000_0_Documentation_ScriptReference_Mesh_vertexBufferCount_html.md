* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-vertexBufferCount.html

#  [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html).vertexBufferCount
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
vertexBufferCount; 
### Description
Gets the number of vertex buffers present in the Mesh. (Read Only)
Most Meshes contain only one vertex buffer, but some (such as skinned Meshes on some platforms) might contain more than one. This property is mostly useful together with [GetNativeVertexBufferPtr](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetNativeVertexBufferPtr.html) to enable Mesh manipulation from [native code plugins](https://docs.unity3d.com/6000.0/Documentation/Manual/native-plugin-interface.html).
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
  
        // Prints 2 (two vertex streams)
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Vertex[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Vertex.html) stream count: {mesh.vertexBufferCount}");  
  
        // Cleanup
        Object.DestroyImmediate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DestroyImmediate.html)(mesh);
    }
}

```

Additional resources: [Native code plugins](https://docs.unity3d.com/6000.0/Documentation/Manual/native-plugin-interface.html), [GetNativeVertexBufferPtr](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetNativeVertexBufferPtr.html), [SetVertexBufferParams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetVertexBufferParams.html), [GetVertexAttributeOffset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetVertexAttributeOffset.html).
* * *
