* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain.GetActiveTerrains.html

#  [Terrain](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain.html).GetActiveTerrains
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
public static void GetActiveTerrains(List<Terrain> terrainList); 
### Parameters
Parameter | Description  
---|---  
activeTerrainsList |  A List of Terrains this function populates with the active Terrains in the Scene.  
### Description
Populates a List of Terrains with the active Terrains in the Scene.
This function differs from [Terrain.activeTerrains](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-activeTerrains.html) in that it gives you control of memory allocation. Additional resources: [Terrain.activeTerrains](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-activeTerrains.html).
* * *
