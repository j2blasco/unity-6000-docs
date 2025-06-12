* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-minBounces.html

#  [LightingSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings.html).minBounces
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
minBounces; 
### Description
Stores the minimum number of bounces the Progressive Lightmapper computes for indirect lighting. (Editor only)
To reduce the computational load and improve performance during bakes, the Progressive Lightmapper terminates light paths that contribute little to the appearance of the Scene lighting. Light paths are weighted so that those with low intensity are more likely to be terminated first. This technique is known as Russian Roulette.  
  
`minBounces` determines the minimum number of bounces for an indirect light path before Unity applies the Russian Roulette technique.  
  
Default value: 2. Range: 0–100. Lower values reduce bake times, but increase lightmap noise. Higher values increase bake times, but reduce lightmap noise.  
  
To disable the Russian Roulette technique, set `minBounces` to the same value as LightmapSettings.maxBounces.  
  
When Unity serializes this `LightingSettings` object as a [Lighting Settings Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightingSettings.html), this property corresponds to the **Min Bounces** property in the Lighting Settings Asset Inspector.  
  
Additional resources: [Lighting Settings Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightingSettings.html), LightmapSettings.maxBounces.
* * *
