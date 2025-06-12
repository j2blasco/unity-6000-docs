* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderingLayerMask.html

# RenderingLayerMask
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
The Render Pipeline allows you to use Rendering Layers, which are LayerMasks to make Lights or effects only affect specific Renderers.
Rendering Layers are also supported on decal projectors, and can be sampled from the ShaderGraph to implement custom effects.  
  
Rendering Layers are a Bitmask and it represents the 32 Layers and define them as `true` or `false`. Each bitmask describes whether the `RenderingLayer` is used. As an example, bit 5 can be set to 1 (`true`).  
  
`Edit->Settings->Tags and Layers` option shows the use of the 32 bitmasks. Each `RenderingLayer` is shown with a string setting. As an example `Layer 0` is set as `Default`. There is always at least one defined RenderingLayer.
### Static Properties
Property | Description  
---|---  
[defaultRenderingLayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderingLayerMask-defaultRenderingLayerMask.html) | Returns an instance of Default Rendering Layer Mask.  
### Properties
Property | Description  
---|---  
[value](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderingLayerMask-value.html) | Converts a layer mask value to an integer value.  
### Static Methods
Method | Description  
---|---  
[GetDefinedRenderingLayerCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderingLayerMask.GetDefinedRenderingLayerCount.html) | Returns a number of Rendering Layers defined in the Tags and Layers manager.  
[GetDefinedRenderingLayerNames](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderingLayerMask.GetDefinedRenderingLayerNames.html) | Returns a names of the defined Rendering Layers in the Tags and Layers manager.  
[GetDefinedRenderingLayersCombinedMaskValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderingLayerMask.GetDefinedRenderingLayersCombinedMaskValue.html) | Returns value that represents all defined Rendering Layers in the Tags and Layers manager.  
[GetDefinedRenderingLayerValues](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderingLayerMask.GetDefinedRenderingLayerValues.html) | Returns a values of the defined Rendering Layers in the Tags and Layers manager.  
[GetLastDefinedRenderingLayerIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderingLayerMask.GetLastDefinedRenderingLayerIndex.html) | Returns an index of the last defined Rendering Layer in the Tags and Layers manager.  
[GetMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderingLayerMask.GetMask.html) | Given a set of rendering layer names as defined in the Tags and Layers manager, returns the equivalent rendering layer mask for all of them.  
[GetRenderingLayerCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderingLayerMask.GetRenderingLayerCount.html) | Returns a number of Rendering Layers defined in the Tags and Layers manager including empty ones.  
[NameToRenderingLayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderingLayerMask.NameToRenderingLayer.html) | Given a rendering layer name, returns the rendering layer index as defined in the Tags and Layers manager.  
[RenderingLayerToName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderingLayerMask.RenderingLayerToName.html) | Given a rendering layer index, returns the name of the layer as defined in the Tags and Layers manager.  
### Operators
Operator | Description  
---|---  
[RenderingLayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderingLayerMask-operator_uint.html) | Implicitly converts uint to a RenderingLayerMask.  
* * *
