* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.DrawingSettings.html

# DrawingSettings
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
Settings for ScriptableRenderContext.DrawRenderers.
DrawingSettings describes how to sort visible objects ([sortingSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.DrawingSettings-sortingSettings.html)) and which shader passes to use ([shaderPassName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.DrawingSettings-shaderPassName.html)).  
  
Additional resources: ScriptableRenderContext.DrawRenderers, [ScriptableRenderContext.Cull](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.Cull.html), [FilteringSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.FilteringSettings.html).  
  
OverrideMaterial vs. OverrideShader: Using the overrideMaterial parameter will override all rendered materials and their properties. The overrideShader property will force the renderers to use a different shader while preserving current material properties. Properties on the overriden material can then be accessed in the override shader. The use of override shaders is currently not supported with SRPBatcher and BatchRendererGroups. Override Shaders will have an impact on performance and should be avoided where overrideMaterial can be used. OverrideShader and OverrideMaterial can't both be used in the same drawRenderers call.
### Static Properties
Property | Description  
---|---  
[maxShaderPasses](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.DrawingSettings-maxShaderPasses.html) | The maxiumum number of passes that can be rendered in 1 DrawRenderers call.  
### Properties
Property | Description  
---|---  
[enableDynamicBatching](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.DrawingSettings-enableDynamicBatching.html) | Controls whether dynamic batching is enabled.  
[enableInstancing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.DrawingSettings-enableInstancing.html) | Controls whether instancing is enabled.  
[fallbackMaterial](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.DrawingSettings-fallbackMaterial.html) | Sets the Material to use for any drawers in this group that don't meet the requirements.  
[mainLightIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.DrawingSettings-mainLightIndex.html) | Configures what light should be used as main light.  
[overrideMaterial](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.DrawingSettings-overrideMaterial.html) | Sets the Material to use for all drawers that would render in this group.  
[overrideMaterialPassIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.DrawingSettings-overrideMaterialPassIndex.html) | Selects which pass of the override material to use.  
[overrideShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.DrawingSettings-overrideShader.html) | Sets the shader to use for all drawers that would render in this group. Override shaders do not override existing material properties.  
[overrideShaderPassIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.DrawingSettings-overrideShaderPassIndex.html) | Selects which pass of the override shader to use.  
[perObjectData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.DrawingSettings-perObjectData.html) | What kind of per-object data to setup during rendering.  
[sortingSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.DrawingSettings-sortingSettings.html) | How to sort objects during rendering.  
### Constructors
Constructor | Description  
---|---  
[DrawingSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.DrawingSettings-ctor.html) | Create a draw settings struct.  
### Public Methods
Method | Description  
---|---  
[GetShaderPassName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.DrawingSettings.GetShaderPassName.html) | Get the name of the shader pass.  
[SetShaderPassName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.DrawingSettings.SetShaderPassName.html) | Set the name of the shader pass.  
* * *
