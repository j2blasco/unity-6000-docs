* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintDetailsToolUtility.FindDetailPrototype.html

#  [PaintDetailsToolUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintDetailsToolUtility.html).FindDetailPrototype
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
public static int FindDetailPrototype([Terrain](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain.html) terrain, [Terrain](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain.html) sourceTerrain, int sourceDetail); 
### Parameters
Parameter | Description  
---|---  
terrain | The target terrain.  
sourceTerrain | The source terrain.  
sourceDetail | The index of the source detail.  
### Returns
**int** Returns the index position of the similar detail. Otherwise, returns an invalid index of -1. 
### Description
Gets the index position of similar details between two terrains.
This method returns the index position of the detail within the target terrain that matches the detail on the source terrain. If the same detail doesn't exist on the target terrain, then an invalid index is passed. 
* * *
