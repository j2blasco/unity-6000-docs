* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.IOnInspectorGUI.ShowBrushesGUI.html

#  [IOnInspectorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.IOnInspectorGUI.html).ShowBrushesGUI
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
public void ShowBrushesGUI(int spacing, [TerrainTools.BrushGUIEditFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.BrushGUIEditFlags.html) flags, int textureResolutionPerTile); 
### Parameters
Parameter | Description  
---|---  
spacing | Pixel spacing for the brush GUI controls.  
flags | Specifies which brush controls to display in the Terrain tool UI.  
textureResolutionPerTile | The resolution per Terrain tile of the Texture, which the tool is editing. Unity uses this value to calculate Brush size limits.  
### Description
Displays the default controls for the brush in the tool inspector.
If the tool is editing multiple Textures on a Terrain, textureResolutionPerTile is the largest resolution among them. Additional resources: [IOnPaint.brushSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.IOnPaint-brushSize.html) and [IOnPaint.brushStrength](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.IOnPaint-brushStrength.html).
* * *
