* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain.SetNeighbors.html

#  [Terrain](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain.html).SetNeighbors
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
## Declaration
public void SetNeighbors([Terrain](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain.html) left, [Terrain](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain.html) top, [Terrain](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain.html) right, [Terrain](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain.html) bottom); 
### Parameters
Parameter | Description  
---|---  
left | The Terrain tile to the left is in the negative X direction.  
top | The Terrain tile to the top is in the positive Z direction.  
right | The Terrain tile to the right is in the positive X direction.  
bottom | The Terrain tile to the bottom is in the negative Z direction.  
### Description
Lets you set up the connection between neighboring Terrain tiles. This ensures LOD matches up on neighboring Terrain tiles.
Note that it isn't enough to call this function on one Terrain; you need to set the neighbors of each Terrain.
* * *
