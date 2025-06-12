* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BlendShapeBufferRange.html

# BlendShapeBufferRange
struct in UnityEngine
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
Describes the location of blend shape vertex data in a [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html).
When you call [Mesh.GetBlendShapeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetBlendShapeBuffer.html) with [BlendShapeBufferLayout.PerShape](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendShapeBufferLayout.PerShape.html), Unity returns a [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) that contains blend shape vertex data, ordered by blend shape.  
  
When you call [Mesh.GetBlendShapeBufferRange](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetBlendShapeBufferRange.html) for a given blend shape, Unity returns this struct. Use this struct to locate the data for that blend shape in the `GraphicsBuffer`.
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
  
        // Iterate over all Blend Shapes in a mesh
        for (int blendShapeIndex = 0; blendShapeIndex  < mesh.blendShapeCount; ++blendShapeIndex)
        {
            // Fetch which indices in the buffer that is part of this Blend Shape
            var blendShapeRange = mesh.GetBlendShapeBufferRange(blendShapeIndex);  
  
            // Set the start and end indices of the Blend Shape in the compute shader
            computeShader.SetInt("_StartIndex", (int)blendShapeRange.startIndex);
            computeShader.SetInt("_EndIndex", (int)blendShapeRange.endIndex);  
  
            // Dispatch compute shader and access data between start and end index for this Blend Shape
            computeShader.Dispatch(0, 64, 1, 1);
        }  
  
        // Dispose of GraphicsBuffer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) to avoid leak memory
        perShapeBuffer.Dispose();
    }
}

```

Additional resources: [Mesh.GetBlendShapeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetBlendShapeBuffer.html), [Mesh.GetBlendShapeBufferRange](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetBlendShapeBufferRange.html), [BlendShapeBufferLayout.PerShape](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendShapeBufferLayout.PerShape.html).
### Properties
Property | Description  
---|---  
[endIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BlendShapeBufferRange-endIndex.html) | The index of the last blend shape vertex for the requested blend shape.  
[startIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BlendShapeBufferRange-startIndex.html) | The index of the first blend shape vertex for the requested blend shape.  
* * *
