* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics-activeTier.html

#  [Graphics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.html).activeTier
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
[Rendering.GraphicsTier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTier.html) activeTier; 
### Description
The [GraphicsTier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTier.html) for the current device.
**Note:** Graphics tiers are only supported in the Built-in Render Pipeline.  
  
Unity auto-detects this value, and sets it during startup. This value determines which [TierSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.TierSettings.html) are in use, and which tier variants Unity loads when it loads shaders. Changing this value affects any subsequently loaded shaders. For more information, see [Graphics tiers](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-tiers.html).  
  
Additional resources: [Graphics tiers](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-tiers.html), [TierSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.TierSettings.html), [GraphicsTier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTier.html), [EditorGraphicsSettings.GetTierSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.EditorGraphicsSettings.GetTierSettings.html), [EditorGraphicsSettings.SetTierSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.EditorGraphicsSettings.SetTierSettings.html).
* * *
