* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-lightmapScaleOffset.html

#  [Renderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html).lightmapScaleOffset
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
[Vector4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html) lightmapScaleOffset; 
### Description
The UV scale & offset used for a lightmap.
A lightmap is a texture atlas and multiple Renderers can use different portions of the same lightmap.  
  
The vector's x and y refer to UV scale, while z and w refer to UV offset.  
  
Note: this property is only serialized when building the player. In all the other cases it's the responsibility of the Unity lightmapping system (or a custom script that brings external lightmapping data) to set it when the Scene loads or playmode is entered.  
  
Additional resources: [LightmapSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapSettings.html) class, [lightmapIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-lightmapIndex.html) property, [ShaderLab properties](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Properties.html).
* * *
