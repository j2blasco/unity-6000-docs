* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.TerrainPaintTool_1.OnInspectorGUI.html

#  [TerrainPaintTool<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.TerrainPaintTool_1.html).OnInspectorGUI
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
public void OnInspectorGUI([Terrain](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain.html) terrain, [TerrainTools.IOnInspectorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.IOnInspectorGUI.html) editContext); 
### Parameters
Parameter | Description  
---|---  
terrain | Active Terrain object.  
editContext | Interface used to communicate between Editor and Paint tools.  
### Description
Custom terrain tool OnInspectorGUI callback.
Unity calls this method to run tool-specific inspector controls and behavior. Additional resources: [Editor.OnInspectorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.OnInspectorGUI.html). 
* * *
