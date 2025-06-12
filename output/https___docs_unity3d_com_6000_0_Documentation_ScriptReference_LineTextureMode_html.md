* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineTextureMode.html

# LineTextureMode
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
Choose how textures are applied to Lines and Trails.
### Properties
Property | Description  
---|---  
[Stretch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineTextureMode.Stretch.html) | Map the texture once along the entire length of the line.  
[Tile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineTextureMode.Tile.html) | Repeat the texture along the line, based on its length in world units. To set the tiling rate, use Material.SetTextureScale.  
[DistributePerSegment](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineTextureMode.DistributePerSegment.html) | Map the texture once along the entire length of the line, assuming all vertices are evenly spaced.  
[RepeatPerSegment](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineTextureMode.RepeatPerSegment.html) | Repeat the texture along the line, repeating at a rate of once per line segment. To adjust the tiling rate, use Material.SetTextureScale.  
[Static](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineTextureMode.Static.html) | Trails do not change the texture coordinates of existing points when they add or remove points.  
* * *
