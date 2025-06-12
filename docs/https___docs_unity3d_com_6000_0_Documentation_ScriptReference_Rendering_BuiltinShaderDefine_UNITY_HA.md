* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BuiltinShaderDefine.UNITY_HARDWARE_TIER3.html

#  [BuiltinShaderDefine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BuiltinShaderDefine.html).UNITY_HARDWARE_TIER3
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
UNITY_HARDWARE_TIER3 is set when compiling shaders for [GraphicsTier.Tier3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTier.Tier3.html).
**Note:** Graphics tiers are only supported in the Built-in Render Pipeline.  
  
Unity generates tier shader variants if your shader source code includes `#pragma hardware_tier_variants`, or if the Tier settings for your project are not all identical.  
  
For more information on Graphics tiers and shader variants, see [Graphics tiers](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-tiers.html).  
  
Additional resources: [Graphics tiers](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-tiers.html), [TierSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.TierSettings.html) [GraphicsTier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTier.html), [Graphics.activeTier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics-activeTier.html), [EditorGraphicsSettings.GetTierSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.EditorGraphicsSettings.GetTierSettings.html), [EditorGraphicsSettings.SetTierSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.EditorGraphicsSettings.SetTierSettings.html).
* * *
