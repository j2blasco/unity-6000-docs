* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-lightmapIndex.html

#  [Renderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html).lightmapIndex
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
lightmapIndex; 
### Description
The index of the baked lightmap applied to this renderer.
The index refers to the [LightmapSettings.lightmaps](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapSettings-lightmaps.html) array. A value of -1 (0xFFFF) means no lightmap has been assigned, which is the default. A value of 0xFFFE is internally used for objects that have their scale in lightmap set to 0; they affect lightmaps, but don't have a lightmap assigned themselves. The index is 16 bits internally and can't be larger than 65533 (0xFFFE).  
  
Note: this property is only serialized when building the player. In all the other cases it's the responsibility of the Unity lightmapping system (or a custom script that brings external lightmapping data) to set it when the Scene loads or playmode is entered.  
  
A lightmap is a texture atlas and multiple Renderers can use different portions of the same lightmap.  
  
Additional resources: [LightmapSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapSettings.html) class, [lightmapScaleOffset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-lightmapScaleOffset.html) property, [ShaderLab properties](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Properties.html).
* * *
