* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemTrailTextureMode.html

# ParticleSystemTrailTextureMode
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
Choose how textures are applied to Particle Trails.
### Properties
Property | Description  
---|---  
[Stretch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemTrailTextureMode.Stretch.html) | Map the texture once along the entire length of the trail.  
[Tile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemTrailTextureMode.Tile.html) | Repeat the texture along the trail. To set the tiling rate, use Material.SetTextureScale.  
[DistributePerSegment](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemTrailTextureMode.DistributePerSegment.html) | Map the texture once along the entire length of the trail, assuming all vertices are evenly spaced.  
[RepeatPerSegment](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemTrailTextureMode.RepeatPerSegment.html) | Repeat the texture along the trail, repeating at a rate of once per trail segment. To adjust the tiling rate, use Material.SetTextureScale.  
[Static](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemTrailTextureMode.Static.html) | Trails do not change the texture coordinates of existing points when they add or remove points.  
* * *
