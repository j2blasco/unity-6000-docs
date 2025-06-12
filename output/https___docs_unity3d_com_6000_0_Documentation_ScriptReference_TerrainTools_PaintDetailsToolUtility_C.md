* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintDetailsToolUtility.CopyDetailPrototype.html

#  [PaintDetailsToolUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintDetailsToolUtility.html).CopyDetailPrototype
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
public static int CopyDetailPrototype([Terrain](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain.html) terrain, [Terrain](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain.html) sourceTerrain, int sourceDetail); 
### Parameters
Parameter | Description  
---|---  
terrain | The target terrain.  
sourceTerrain | The source terrain.  
sourceDetail | The index of the source detail.  
### Returns
**int** Returns the index of the copied detail prototype. 
### Description
Copies a detail prototype between two terrains.
Use this method when you need a copy of a detail prototype on a different terrain. 
* * *
