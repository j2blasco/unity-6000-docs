* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RendererListParams.html

# RendererListParams
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
Struct holding the arguments that are needed to create a renderers [RendererList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RendererList.html).
### Static Properties
Property | Description  
---|---  
[Invalid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RendererListParams.Invalid.html) | Returns an empty RendererListParams.  
### Properties
Property | Description  
---|---  
[cullingResults](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RendererListParams-cullingResults.html) | The set of visible objects to draw. You typically obtain this from ScriptableRenderContext.Cull.  
[drawSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RendererListParams-drawSettings.html) | A struct that describes how to draw the objects.  
[filteringSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RendererListParams-filteringSettings.html) | A struct that describes how to filter the set of visible objects, so that Unity only draws a subset.  
[isPassTagName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RendererListParams-isPassTagName.html) | If set to true, tagName specifies a Pass Tag. Otherwise, tagName specifies a SubShader Tag.  
[stateBlocks](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RendererListParams-stateBlocks.html) | An array of structs that describe which parts of the GPU's render state to override.  
[tagName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RendererListParams-tagName.html) | The name of a SubShader Tag or Pass Tag.  
[tagValues](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RendererListParams-tagValues.html) | An array of ShaderTagId structs, where the name is the value of a given SubShader Tag or Pass Tag.  
### Constructors
Constructor | Description  
---|---  
[RendererListParams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RendererListParams-ctor.html) | Create a RendererListParams struct.  
* * *
