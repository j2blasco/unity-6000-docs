* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.SetTerrainLayersRegisterUndo.html

#  [TerrainData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.html).SetTerrainLayersRegisterUndo
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
public void SetTerrainLayersRegisterUndo(TerrainLayer[] terrainLayers, string undoName); 
### Parameters
Parameter | Description  
---|---  
terrainLayers | The Terrain Layer assets to set.  
undoName | The name of the Editor's undo action.  
### Description
This function sets the [terrainLayers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData-terrainLayers.html) property, and in addition, registers the action to the Editor's undo stack.
This function is only available in the Editor.
* * *
