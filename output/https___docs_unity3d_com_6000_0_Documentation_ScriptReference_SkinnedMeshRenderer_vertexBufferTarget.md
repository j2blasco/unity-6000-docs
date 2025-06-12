* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinnedMeshRenderer-vertexBufferTarget.html

#  [SkinnedMeshRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinnedMeshRenderer.html).vertexBufferTarget
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-SkinnedMeshRenderer.html "Go to SkinnedMeshRenderer Component in the Manual")
[GraphicsBuffer.Target](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.html) vertexBufferTarget; 
### Description
The intended target usage of the skinned mesh GPU vertex buffer.
By default, skinned mesh renderer vertex buffers have [GraphicsBuffer.Target.Vertex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.Vertex.html) usage target. If you want to access the vertex buffer from a compute shader, additional targets need to be requested, for example [GraphicsBuffer.Target.Raw](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.Raw.html).
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Mark the vertex buffer as needing "Raw"
        // (ByteAddressBuffer, RWByteAddressBuffer in HLSL shaders)
        // access. We can then use GetVertexBuffer and
        // use it with compute shaders.
        GetComponent<SkinnedMeshRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinnedMeshRenderer.html)>().vertexBufferTarget |= GraphicsBuffer.Target.Raw[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.Raw.html);
    }
}

```

Additional resources: [Target](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.html), [GetVertexBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinnedMeshRenderer.GetVertexBuffer.html), [GetPreviousVertexBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinnedMeshRenderer.GetPreviousVertexBuffer.html).
* * *
