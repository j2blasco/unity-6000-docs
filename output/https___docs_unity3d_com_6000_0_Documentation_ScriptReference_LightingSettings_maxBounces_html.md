* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-maxBounces.html

#  [LightingSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings.html).maxBounces
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
maxBounces; 
### Description
Stores the maximum number of bounces the Progressive Lightmapper computes for indirect lighting. (Editor only)
To reduce the computational load and improve performance during bakes, the Progressive Lightmapper terminates light paths that contribute little to the appearance of the Scene lighting. Light paths are weighted so that those with low intensity are more likely to be terminated first. This technique is known as Russian Roulette.  
  
`maxBounces` determines the maximum number of bounces for an indirect light path.  
  
Default value: 2. Range: 0–100. The higher the value, the longer the bake time. Values of up to 10 are suitable for most Scenes. Values higher than 10 might lead to significantly longer bake times.  
  
To disable the Russian Roulette technique, set `maxBounces` to the same value as LightmapSettings.minBounces.  
  
When Unity serializes this `LightingSettings` object as a [Lighting Settings Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightingSettings.html), this property corresponds to the **Max Bounces** property in the Lighting Settings Asset Inspector.  
  
Additional resources: [Lighting Settings Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightingSettings.html), LightmapSettings.minBounces.
* * *
