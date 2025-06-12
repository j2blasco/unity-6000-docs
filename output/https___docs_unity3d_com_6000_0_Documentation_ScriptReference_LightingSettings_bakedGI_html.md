* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-bakedGI.html

#  [LightingSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings.html).bakedGI
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
bakedGI; 
### Description
Whether to enable the Baked Global Illumination system for this Scene.
When this is set to `true`, this Scene uses the Baked Global Illumination system. This means that you are able to generate baked lightmaps, Light Probes and Reflection Probes for this Scene.  
  
When this is set to `false`, this Scene does not use the Baked Global Illumination system. This means that you are unable to generate baked lightmaps and Light Probes for this Scene. At runtime, Unity will not load precomputed lighting data for this Scene, and Baked Lights and Mixed Lights will behave as real-time Lights.  
  
When Unity serializes this `LightingSettings` object as a [Lighting Settings Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightingSettings.html), this property corresponds to the **Baked GI** property in the Lighting Settings Asset Inspector.  
  
Additional resources: [Lighting Settings Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightingSettings.html), [realtimeGI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-realtimeGI.html).
* * *
