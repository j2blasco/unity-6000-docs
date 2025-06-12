* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintDetailsToolUtility.DrawClampedDetailPatchGUI.html

#  [PaintDetailsToolUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintDetailsToolUtility.html).DrawClampedDetailPatchGUI
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
public static void DrawClampedDetailPatchGUI(int mouseOnPatchIndex, List<Vector4> clampedDetailPatchIconScreenPositions, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) detailMinMaxHeight, [Terrain](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain.html) terrain, [TerrainTools.IOnSceneGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.IOnSceneGUI.html) editContext); 
### Parameters
Parameter | Description  
---|---  
mouseOnPatchIndex | The index of the patch that the mouse is hovering over.  
clampedDetailPatchIconScreenPositions | The list of screen detail patch icons within the screen positions.  
detailMinMaxHeight | The minimum and maximum height of the details within the terrain.  
terrain | The target terrain.  
editContext | The edit context object.  
### Description
Displays the clamped detail patches.
Use this method to visualize the clamped patches when scattering details across a terrain. These clamped patches are areas where the maximum amount of detail patches are exceeded.  
  
Additional resources: [PaintDetailsToolUtility.ClampedDetailPatchesGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintDetailsToolUtility.ClampedDetailPatchesGUI.html)
* * *
