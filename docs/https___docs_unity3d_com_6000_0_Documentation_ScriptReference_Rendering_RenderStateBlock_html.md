* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderStateBlock.html

# RenderStateBlock
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
A set of values that Unity uses to override the GPU's render state.
When you call ScriptableRenderContext.DrawRenderers, you can use this to override the render state for some or all of the geometry.  
  
**Note:** You must set [mask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderStateBlock-mask.html) to tell Unity which parts of the render state to override to apply. For example, to apply the values in [blendState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderStateBlock-blendState.html), [mask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderStateBlock-mask.html) must include [RenderStateMask.Blend](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderStateMask.Blend.html).
```
using UnityEngine;
using UnityEngine.Rendering;  
  
public class OverrideRenderStateExample
{
    ScriptableRenderContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.html) scriptableRenderContext;  
  
    // Placeholder data
    DrawingSettings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.DrawingSettings.html) exampleDrawingSettings;
    CullingResults[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingResults.html) exampleCullingResults = new CullingResults[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingResults.html)();
    FilteringSettings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.FilteringSettings.html) exampleFilteringSettings = new FilteringSettings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.FilteringSettings.html)();  
  
    public void OverrideRenderState()
    {
        // Tell Unity how to override the render state when it draws the geometry.
        var stateBlock = new RenderStateBlock[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderStateBlock.html)(RenderStateMask.Depth[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderStateMask.Depth.html));
        stateBlock.depthState = new DepthState[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.DepthState.html)(true, CompareFunction.LessEqual[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CompareFunction.LessEqual.html));  
  
        // Schedule the drawing operation.
        scriptableRenderContext.DrawRenderers(exampleCullingResults, ref exampleDrawingSettings, ref exampleFilteringSettings, ref stateBlock);  
  
        // Perform all scheduled tasks, in the order that they were scheduled.
        scriptableRenderContext.Submit();
    }
}

```

Additional resources: ScriptableRenderContext.DrawRenderers, [RenderStateMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderStateMask.html).
### Properties
Property | Description  
---|---  
[blendState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderStateBlock-blendState.html) | Specifies the new blend state.  
[depthState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderStateBlock-depthState.html) | Specifies the new depth state.  
[mask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderStateBlock-mask.html) | Specifies which parts of the GPU's render state to override.  
[rasterState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderStateBlock-rasterState.html) | Specifies the new raster state.  
[stencilReference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderStateBlock-stencilReference.html) | The value to be compared against and/or the value to be written to the buffer, based on the stencil state.  
[stencilState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderStateBlock-stencilState.html) | Specifies the new stencil state.  
### Constructors
Constructor | Description  
---|---  
[RenderStateBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderStateBlock-ctor.html) | Creates a new render state block with the specified mask.  
* * *
