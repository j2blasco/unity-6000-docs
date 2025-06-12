* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.GetClampedDetailPatches.html

#  [TerrainData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.html).GetClampedDetailPatches
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
public Vector2Int[] GetClampedDetailPatches(float density); 
### Parameters
Parameter | Description  
---|---  
density | The detail density value. See [Terrain.detailObjectDensity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-detailObjectDensity.html).  
### Description
Returns an array of detail patches, which are each identified by X-Z coordinates. Detail objects in the patches are clamped to the maximum count.
This function is only available in the Editor.
* * *
