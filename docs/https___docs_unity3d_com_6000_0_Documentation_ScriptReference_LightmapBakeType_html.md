* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapBakeType.html

# LightmapBakeType
enumeration
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
Enum describing what part of a light contribution can be baked.
### Properties
Property | Description  
---|---  
[Realtime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapBakeType.Realtime.html) | Real-time lights cast run time light and shadows. They can change position, orientation, color, brightness, and many other properties at run time. No lighting gets baked into lightmaps or light probes..  
[Baked](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapBakeType.Baked.html) | Baked lights cannot move or change in any way during run time. All lighting for static objects gets baked into lightmaps. Lighting and shadows for dynamic objects gets baked into Light Probes.  
[Mixed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapBakeType.Mixed.html) | Mixed lights allow a mix of real-time and baked lighting, based on the Mixed Lighting Mode used. These lights cannot move, but can change color and intensity at run time. Changes to color and intensity only affect direct lighting as indirect lighting gets baked. If using Subtractive mode, changes to color or intensity are not calculated at run time on static objects.  
* * *
