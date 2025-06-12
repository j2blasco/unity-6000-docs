* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.GatherHoles.html

#  [PaintContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.html).GatherHoles
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
public void GatherHoles(); 
### Description
Gathers the Terrain holes information into `sourceRenderTexture`.
This function collects the Terrain holes data from all Terrain tiles in the Paint Context, and saves the information in `sourceRenderTexture`.  
  
This function is called internally by [TerrainPaintUtility.BeginPaintHoles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.TerrainPaintUtility.BeginPaintHoles.html).  
  
Additional resources: [PaintContext.ScatterHoles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.ScatterHoles.html). 
* * *
