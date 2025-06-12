* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-lightmapBakeType.html

#  [Light](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html).lightmapBakeType
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Light.html "Go to Light Component in the Manual")
[LightmapBakeType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapBakeType.html) lightmapBakeType; 
### Description
This property describes what part of a light's contribution can be baked (Editor only).
If this setting is [LightmapBakeType.Realtime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapBakeType.Realtime.html), realtime indirect GI can be precomputed, and then updated at runtime. If this setting is [LightmapBakeType.Baked](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapBakeType.Baked.html), this light will be baked and won't be evaluated at runtime. If this setting is [LightmapBakeType.Mixed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapBakeType.Mixed.html), this light will be a composition of baked and run time evaluation based on the selected Mixed Light mode in the lighting window's Settings tab.  
  
This property is only exposed to Editor scripts. It is not exposed during Play mode.
* * *
