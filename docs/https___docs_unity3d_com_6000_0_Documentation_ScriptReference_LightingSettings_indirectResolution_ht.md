* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-indirectResolution.html

#  [LightingSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings.html).indirectResolution
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
indirectResolution; 
### Description
Defines the number of texels that Enlighten Realtime Global Illumination uses per world unit when calculating indirect lighting. (Editor only).
The default value is 2. Increasing this value can improve lightmap quality, but also increases bake times. Doubling this value causes the number of texels to quadruple, because the value refers to both the height and width of the lightmap. See the Occupied texels count in the statistics area at the bottom of the Lighting window.  
  
This setting affects the lower-resolution, indirect-only lightmaps that the Enlighten Realtime Global Illumination lightmapper generates. These lightmaps are compatible with both the Baked Global Illumination system and the Enlighten Realtime Global Illumination system.  
  
Note that when these indirect-only lightmaps are used with the Baked Global Illumination system, Unity composites them into the final lightmaps, along with the full-resolution direct and ambient occlusion lighting data. The resolution of the final lightmaps is controlled by the [LightingSettings.lightmapResolution](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-lightmapResolution.html) property. Changing this value therefore does not affect the resolution of the final lightmaps, although it can affect the fidelity of the indirect-only data within them.  
  
When Unity serializes this `LightingSettings` object as a [Lighting Settings Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightingSettings.html), this property corresponds to the **Indirect Resolution** property in the Lighting Settings Asset Inspector.  
  
Additional resources: [Lighting Settings Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightingSettings.html), [LightingSettings.lightmapResolution](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-lightmapResolution.html).
* * *
