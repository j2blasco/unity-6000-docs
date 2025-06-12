* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-autoGenerate.html

**Method group is Obsolete**   

#  [LightingSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings.html).autoGenerate
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
**Obsolete** LightingSettings.autoGenerate is obsolete. public bool autoGenerate; 
### Description
Deprecated as Auto Generate lighting is no longer supported. Whether the Unity Editor automatically precomputes lighting data when the Scene data changes. (Editor only).
When this is set to `true`, the Editor automatically bakes lightmaps, Light Probes and Reflection Probes when you make changes to your Scene. When this is set to `false`, Unity does not automatically bake this data. The default value is `false`.  
  
When this is set to `false`, you can instruct Unity to perform the bake by pressing the **Generate Lighting** button in the [Lighting window](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-window.html), or by using the [Lightmapping.Bake](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.Bake.html) or [Lightmapping.BakeAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.BakeAsync.html) APIs.  
  
This setting applies to the Baked Global Illumination system and the Enlighten Realtime Global Illumination system.  
  
When Unity serializes this `LightingSettings` object as a [Lighting Settings Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightingSettings.html), this property corresponds to the **Auto Generate** property in the Lighting Settings Asset Inspector.  
  
Additional resources: [Lighting Settings Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightingSettings.html), [Lighting window](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-window.html), [Lightmapping.Bake](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.Bake.html), [Lightmapping.BakeAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.BakeAsync.html).
* * *
