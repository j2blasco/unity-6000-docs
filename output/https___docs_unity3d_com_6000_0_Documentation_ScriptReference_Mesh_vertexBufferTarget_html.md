* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-vertexBufferTarget.html

#  [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html).vertexBufferTarget
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
[GraphicsBuffer.Target](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.html) vertexBufferTarget; 
### Description
The intended target usage of the Mesh GPU vertex buffer.
By default, Mesh vertex buffers have [GraphicsBuffer.Target.Vertex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.Vertex.html) usage target. If you want to access the mesh vertex buffer from a compute shader, additional targets need to be requested, for example [GraphicsBuffer.Target.Raw](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.Raw.html).
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh;
    public ComputeShader[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html) computeShader;
    void Start()
    {
        // Mark the vertex buffer as needing "Raw"
        // (ByteAddressBuffer, RWByteAddressBuffer in HLSL shaders)
        // access.
        mesh.vertexBufferTarget |= GraphicsBuffer.Target.Raw[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.Raw.html);
        // Get the vertex buffer of the Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html), and set it up
        // as a buffer parameter to a compute shader.
        var vertexBuffer = mesh.GetVertexBuffer(0);
        computeShader.SetBuffer(0, "MeshVertexBuffer", vertexBuffer);
        vertexBuffer.Dispose();
    }
}

```

Additional resources: [Target](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.html), [GetVertexBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetVertexBuffer.html), [indexBufferTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-indexBufferTarget.html).
* * *
