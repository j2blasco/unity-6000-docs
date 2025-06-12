* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.TerrainPaintUtility.EndPaintTexture.html

#  [TerrainPaintUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.TerrainPaintUtility.html).EndPaintTexture
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
public static void EndPaintTexture([TerrainTools.PaintContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.html) ctx, string editorUndoName); 
### Parameters
Parameter | Description  
---|---  
ctx | The texture paint context to complete.  
editorUndoName | Unique name used for the undo stack.  
### Description
Helper function to complete a texture alphamap modification.
Once the modified data is written to [PaintContext.destinationRenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext-destinationRenderTexture.html), call this function to copy the modifications back to the original Terrain tiles. This function also signals Unity to recalculate the basemap. This function will also release all allocated resources in the PaintContext.  
  
Additional resources: [TerrainPaintUtility.BeginPaintTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.TerrainPaintUtility.BeginPaintTexture.html), [PaintContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.html), and [PaintContext.ScatterAlphamap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.ScatterAlphamap.html). 
* * *
