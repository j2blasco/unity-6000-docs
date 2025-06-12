* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendShapeBufferLayout.PerShape.html

#  [BlendShapeBufferLayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendShapeBufferLayout.html).PerShape
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
Order the data by blend shape.
When you call [Mesh.GetBlendShapeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetBlendShapeBuffer.html) with this option, it returns a [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) containing blend shape vertex data ordered by blend shape.  
  
In this buffer, each blend shape vertex comprises: 
  * An int that represents the index of the mesh vertex to which this data relates.
  * A [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) that represents the position delta.
  * A [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) that represents the normal delta.
  * A [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) that represents the tangent delta.


In this buffer, all the data for each blend shape vertex is contiguous. The data layout is as follows:  
  
* All blend shape vertices that belong to a single blend shape are stored contiguously, followed by all blend shape vertices that belong to another blend shape, and so on  
  
The contiguous blend shape vertex data is stored as an array of 32-bit values. You must manually convert the data to an appropriate type.  
  
To determine which data relates to which blend shape, use [Mesh.GetBlendShapeBufferRange](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetBlendShapeBufferRange.html).  
  
Unity creates this buffer when it creates the mesh. Accessing this buffer does not result in additional memory allocations.
```
using UnityEngine;
using UnityEngine.Rendering;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh;
    public ComputeShader[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html) computeShader;  
  
    void Start()
    {
        // Fetch GraphicsBuffer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) with Blend Shape data, ordered per shape, from the mesh
        var perShapeBuffer = mesh.GetBlendShapeBuffer(BlendShapeBufferLayout.PerShape[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendShapeBufferLayout.PerShape.html));  
  
        // Set Blend Shape data buffer to a compute shader
        computeShader.SetBuffer(0, "PerShape_BlendShapeBuffer", perShapeBuffer);  
  
        // Dispatch compute shader and access Blend Shape Data[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Data.html) on the GPU
        computeShader.Dispatch(0, 64, 1, 1);  
  
        // Dispose of GraphicsBuffer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) to avoid leaking memory
        perShapeBuffer.Dispose();
    }
}

```

Additional resources: [Mesh data: blend shapes](https://docs.unity3d.com/6000.0/Documentation/Manual/AnatomyofaMesh.html#blend-shapes.html), [Mesh.GetBlendShapeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetBlendShapeBuffer.html), UnityEngine.BlendShapeBufferRange.
* * *
