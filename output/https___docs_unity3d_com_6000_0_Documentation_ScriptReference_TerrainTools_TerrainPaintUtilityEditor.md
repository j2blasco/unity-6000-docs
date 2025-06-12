* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.TerrainPaintUtilityEditor.ShowDefaultPreviewBrush.html

#  [TerrainPaintUtilityEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.TerrainPaintUtilityEditor.html).ShowDefaultPreviewBrush
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
public static void ShowDefaultPreviewBrush([Terrain](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain.html) terrain, [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) brushTexture, float brushSize); 
### Parameters
Parameter | Description  
---|---  
terrain | Terrain object.  
brushTexture | Brush texture.  
brushSize | Brush size.  
### Description
Helper function to display a default preview brush with no rotation or custom materials.
This method determines the position on the Terrain object under the mouse and draws a brush preview at that position using the specified texture and brush size. Additional resources: [TerrainPaintUtilityEditor.DrawBrushPreview](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.TerrainPaintUtilityEditor.DrawBrushPreview.html)
* * *
