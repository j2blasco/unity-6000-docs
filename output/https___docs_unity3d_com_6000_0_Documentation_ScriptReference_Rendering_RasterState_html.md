* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RasterState.html

# RasterState
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
Values for the raster state.
Use this with [RenderStateBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderStateBlock.html) and ScriptableRenderContext.DrawRenderers to override the GPU's render state.  
  
Corresponds to the `Conservative`, `Cull`, `ZClip`, and `Offset` commands in [ShaderLab](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Reference.html).  
  
Additional resources: [RenderStateBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderStateBlock.html), [[ScriptableRenderContext.DrawRenderers], [ShaderLab command: Stencil](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Stencil.html).
### Static Properties
Property | Description  
---|---  
[defaultValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RasterState-defaultValue.html) | Default values for the raster state.  
### Properties
Property | Description  
---|---  
[conservative](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RasterState-conservative.html) | Enables conservative rasterization. Before using check for support via SystemInfo.supportsConservativeRaster property.  
[cullingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RasterState-cullingMode.html) | Controls which sides of polygons should be culled (not drawn).  
[depthClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RasterState-depthClip.html) | Enable clipping based on depth.  
[offsetFactor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RasterState-offsetFactor.html) | Scales the maximum Z slope in the GPU's depth bias setting.  
[offsetUnits](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RasterState-offsetUnits.html) | Scales the minimum resolvable depth buffer value in the GPU's depth bias setting.  
### Constructors
Constructor | Description  
---|---  
[RasterState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RasterState-ctor.html) | Creates a new raster state with the given values.  
* * *
