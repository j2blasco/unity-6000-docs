* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.IOnSceneGUI.html

# IOnSceneGUI
interface in UnityEditor.TerrainTools
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
### Description
Interface that provides parameters and utility functions for the OnSceneGUI event of the terrain paint tools.
Additional resources: [TerrainPaintTool<T0>.OnSceneGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.TerrainPaintTool_1.OnSceneGUI.html).
### Properties
Property | Description  
---|---  
[brushSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.IOnSceneGUI-brushSize.html) | Read only. Current brush size in terrain units (equivalent size to world units).  
[brushStrength](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.IOnSceneGUI-brushStrength.html) | Read only. Current brush strength.  
[brushTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.IOnSceneGUI-brushTexture.html) | Read only. Current selected brush texture.  
[controlId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.IOnSceneGUI-controlId.html) | The control ID for the current Terrain Inspector. (Read Only)  
[hitValidTerrain](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.IOnSceneGUI-hitValidTerrain.html) | Read only. True if the mouse is over a valid Terrain object; otherwise false.  
[raycastHit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.IOnSceneGUI-raycastHit.html) | Read only. The raycast result for the current mouse position. This is valid when hitValidTerrain is true.  
[sceneView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.IOnSceneGUI-sceneView.html) | Read only. SceneView object.  
### Public Methods
Method | Description  
---|---  
[Repaint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.IOnSceneGUI.Repaint.html) | Instructs the Editor to repaint the tool UI, the Scene view, or both.  
* * *
