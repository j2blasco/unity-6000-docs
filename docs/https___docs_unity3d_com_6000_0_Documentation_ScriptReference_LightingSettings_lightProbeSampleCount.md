* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-lightProbeSampleCountMultiplier.html

#  [LightingSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings.html).lightProbeSampleCountMultiplier
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightingSettings.html "Go to LightingSettings Component in the Manual")
lightProbeSampleCountMultiplier; 
### Description
Specifies the number of samples to use for Light Probes relative to the number of samples for lightmap texels. (Editor only).
The default value is 4.  
  
This value is a multiplier of [directSampleCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-directSampleCount.html), [indirectSampleCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-indirectSampleCount.html) and [environmentSampleCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-environmentSampleCount.html). This multiplier is used to account for the fact that Light Probes have to sample a larger area and therefore require more samples than a lightmap texel. If you increase this value, the quality of your Light Probes might improve, but baking takes more time. This can help in cases where Light Probes appear inconsistent with other baked lighting in the Scene.  
  
When Unity serializes this `LightingSettings` object as a [Lighting Settings Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightingSettings.html), this property corresponds to the **Light Probe Sample Multiplier** property in the Lighting Settings Asset Inspector.  
  
Additional resources: [Lighting Settings Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightingSettings.html).
* * *
