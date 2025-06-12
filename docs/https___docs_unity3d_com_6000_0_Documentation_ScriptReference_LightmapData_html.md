* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapData.html

# LightmapData
class in UnityEngine
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
Data of a lightmap.
A Scene can have several lightmaps stored in it, and [Renderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) components can use those lightmaps. This makes it possible to use the same material on multiple objects, while each object can refer to a different lightmap or different portion of the same lightmap.  
  
You must set the following properties or Unity might render objects incorrectly: 
  * `lightmapDir` if you use [LightmapsMode.CombinedDirectional](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapsMode.CombinedDirectional.html).
  * `shadowMask` if you use [MixedLightingMode.Shadowmask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MixedLightingMode.Shadowmask.html).


Additional resources: [LightmapSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapSettings.html) class, [Renderer.lightmapIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-lightmapIndex.html)
### Properties
Property | Description  
---|---  
[lightmapColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapData-lightmapColor.html) | Lightmap storing color of incoming light.  
[lightmapDir](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapData-lightmapDir.html) | Lightmap storing dominant direction of incoming light.  
[shadowMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapData-shadowMask.html) | Texture storing occlusion mask per light (ShadowMask, up to four lights).  
* * *
