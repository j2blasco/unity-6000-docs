* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.TerrainPaintTool_1.OnPaint.html

#  [TerrainPaintTool<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.TerrainPaintTool_1.html).OnPaint
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
public bool OnPaint([Terrain](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain.html) terrain, [TerrainTools.IOnPaint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.IOnPaint.html) editContext); 
### Parameters
Parameter | Description  
---|---  
terrain | Active Terrain object.  
editContext | Interface used to communicate between Editor and Paint tools.  
### Returns
**bool** Return true to temporarily hide tree, grass, and detail layers on the terrain. 
### Description
Custom terrain tool paint callback.
Unity calls this method when the mouse button is pressed or dragged, which is typically when a tool applies its modifications. Some tools may instead want to apply their modifications in custom painting logic from within OnSceneGUI. When the method returns true, the layers on top of the terrain, such as trees, grass, and other details, are not rendered.  
  
Additional resources: [PaintContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.html)
* * *
