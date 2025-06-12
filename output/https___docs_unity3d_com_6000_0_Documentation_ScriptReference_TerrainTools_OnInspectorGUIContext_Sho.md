* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.OnInspectorGUIContext.ShowBrushesGUI.html

#  [OnInspectorGUIContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.OnInspectorGUIContext.html).ShowBrushesGUI
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
spacing | Indicate how much spacing to use in the GUILayout.  
flags | Indicates which brush attributes to display.  
textureResolutionPerTile | The height map resolution of the terrain.  
### Description
Calls on IMGUI code to create the inspector for showing terrain brushes. This takes in flags that allow the user to select which brush attributes to display, such as opacity, size, or all.
* * *
