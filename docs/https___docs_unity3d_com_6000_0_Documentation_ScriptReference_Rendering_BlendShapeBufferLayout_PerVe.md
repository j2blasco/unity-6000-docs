* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendShapeBufferLayout.PerVertex.html

#  [BlendShapeBufferLayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendShapeBufferLayout.html).PerVertex
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
Order the data by mesh vertex.
When you call [Mesh.GetBlendShapeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetBlendShapeBuffer.html) with this option, it returns a [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) containing blend shape vertex data ordered by mesh vertex.  
  
In this buffer, each blend shape vertex comprises: 
  * An int that represents the index of the blend shape to which this data relates.
  * A [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) that represents the position delta.
  * A [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) that represents the normal delta.
  * A [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) that represents the tangent delta.


In this buffer, the exact layout depends on the number of mesh vertices. It works as follows: 
  * Elements 0 to (mesh vertex count + 1) contain indices. These indices describe the start and end positions for the data in the rest of the buffer, ordered by mesh vertex. For example, element 0 is the start position of the data for mesh vertex 0; element 1 is the end position of the data for mesh vertex 0 and the start position of the data for mesh vertex 1, and so on.
  * Element at (mesh vertex count + 1) describes the end position for the data for the final mesh vertex.
  * After that, the blend shape vertices that relate to each mesh vertex are stored contiguously. For example, all the blend shape vertices that relate to mesh vertex 0 are contiguous, followed by all the blend shape vertices that relate to mesh vertex 1, and so on.


The contiguous blend shape vertex data is stored as an array of 32-bit values. You must manually convert the data to an appropriate type.  
  
Unity does not create this buffer when it first creates the mesh. Instead, it creates this buffer on-demand, the first time you access it. This means that the first time you access the buffer, it results in CPU and GPU memory allocations.
```
using UnityEngine;
using UnityEngine.Rendering;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh;
    public ComputeShader[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html) computeShader;  
  
    void Start()
    {
        // Fetch GraphicsBuffer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) with Blend Shape data, ordered per vertex, from the mesh
        var perVertexBuffer = mesh.GetBlendShapeBuffer(BlendShapeBufferLayout.PerVertex[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendShapeBufferLayout.PerVertex.html));  
  
        // Set Blend Shape data buffer to a compute shader
        computeShader.SetBuffer(0, "PerVertex_BlendShapeBuffer", perVertexBuffer);  
  
        // Dispatch compute shader and access Blend Shape Data[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Data.html) on the GPU
        computeShader.Dispatch(0, 64, 1, 1);  
  
        // Dispose of GraphicsBuffer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) to avoid leaking memory
        perVertexBuffer.Dispose();
    }
}

```

Additional resources: [Mesh data: blend shapes](https://docs.unity3d.com/6000.0/Documentation/Manual/AnatomyofaMesh.html#blend-shapes.html), [Mesh.GetBlendShapeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetBlendShapeBuffer.html), [QualitySettings.skinWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-skinWeights.html).
* * *
