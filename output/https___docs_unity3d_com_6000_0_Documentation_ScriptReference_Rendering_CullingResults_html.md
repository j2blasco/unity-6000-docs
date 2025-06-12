* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingResults.html

# CullingResults
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
A struct containing the results of a culling operation.
In the Scriptable Render Pipeline, when Unity performs a culling operation, it stores the results in a `CullingResults` struct. This data includes information about visible objects, lights, and reflection probes. Unity uses this data to render objects and process lights. A `CullingResults` struct also provides several functions to aid shadow rendering.  
  
To obtain a `CullingResults` struct, call [ScriptableRenderContext.Cull](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.Cull.html).  
  
A `CullingResults` struct is valid within the scope of a [RenderPipeline.Render](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipeline.Render.html) function; its data goes out of scope when the `Render` function returns. You can use the same `CullingResults` struct multiple times within the same render loop, and you can share a `CullingResults` struct between multiple [Cameras](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) if you know that they can see the same objects. This can save on wasted CPU operations, and therefore improve performance.  
  
This example demonstrates how to obtain a `CullingResults` struct, and then pass it to ScriptableRenderContext.DrawRenderers.
```
using UnityEngine;
using UnityEngine.Rendering;  
  
public class ExampleRenderPipeline : RenderPipeline[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipeline.html)
{
    public ExampleRenderPipeline()
    {
    }  
  
    protected override void Render(ScriptableRenderContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.html) context, Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)[] cameras)
    {
        foreach (Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) camera in cameras)
        {
            // Get the culling parameters from the current camera
            camera.TryGetCullingParameters(out var cullingParameters);  
  
            // Schedule the cull operation that populates the CullingResults[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingResults.html) struct
            CullingResults[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingResults.html) cullingResults = context.Cull(ref cullingParameters);  
  
            // Place code that schedules drawing operations using the CullingResults[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingResults.html) struct here
            // See ScriptableRenderContext.DrawRenderers for details and examples
            // …  
  
            // Execute all of the scheduled operations, in order
            context.Submit();
        }
    }
}

```

### Properties
Property | Description  
---|---  
[lightAndReflectionProbeIndexCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingResults-lightAndReflectionProbeIndexCount.html) | Gets the number of per-object light and reflection probe indices.  
[lightIndexCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingResults-lightIndexCount.html) | Gets the number of per-object light indices.  
[reflectionProbeIndexCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingResults-reflectionProbeIndexCount.html) | Gets the number of per-object reflection probe indices.  
[visibleLights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingResults-visibleLights.html) | Array of visible lights.  
[visibleOffscreenVertexLights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingResults-visibleOffscreenVertexLights.html) | Off-screen lights that still affect visible vertices.  
[visibleReflectionProbes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingResults-visibleReflectionProbes.html) | Array of visible reflection probes.  
### Public Methods
Method | Description  
---|---  
[ComputeDirectionalShadowMatricesAndCullingPrimitives](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingResults.ComputeDirectionalShadowMatricesAndCullingPrimitives.html) | Calculates the view and projection matrices and shadow split data for a directional light.  
[ComputePointShadowMatricesAndCullingPrimitives](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingResults.ComputePointShadowMatricesAndCullingPrimitives.html) | Calculates the view and projection matrices and shadow split data for a point light.  
[ComputeSpotShadowMatricesAndCullingPrimitives](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingResults.ComputeSpotShadowMatricesAndCullingPrimitives.html) | Calculates the view and projection matrices and shadow split data for a spot light.  
[FillLightAndReflectionProbeIndices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingResults.FillLightAndReflectionProbeIndices.html) | Fills a buffer with per-object light indices.  
[GetLightIndexMap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingResults.GetLightIndexMap.html) | If a RenderPipeline sorts or otherwise modifies the VisibleLight list, an index remap will be necessary to properly make use of per-object light lists.  
[GetReflectionProbeIndexMap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingResults.GetReflectionProbeIndexMap.html) | If a RenderPipeline sorts or otherwise modifies the VisibleReflectionProbe list, an index remap will be necessary to properly make use of per-object reflection probe lists.  
[GetShadowCasterBounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingResults.GetShadowCasterBounds.html) | Returns the bounding box that encapsulates the visible shadow casters. Can be used to, for instance, dynamically adjust cascade ranges.  
[SetLightIndexMap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingResults.SetLightIndexMap.html) | If a RenderPipeline sorts or otherwise modifies the VisibleLight list, an index remap will be necessary to properly make use of per-object light lists.  
[SetReflectionProbeIndexMap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingResults.SetReflectionProbeIndexMap.html) | If a RenderPipeline sorts or otherwise modifies the VisibleReflectionProbe list, an index remap will be necessary to properly make use of per-object reflection probe lists.  
* * *
