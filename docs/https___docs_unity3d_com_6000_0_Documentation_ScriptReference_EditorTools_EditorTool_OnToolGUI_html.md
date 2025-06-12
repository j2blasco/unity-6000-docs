* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool.OnToolGUI.html

#  [EditorTool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool.html).OnToolGUI
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
public void OnToolGUI([EditorWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html) window); 
### Parameters
Parameter | Description  
---|---  
window | The window that is displaying the custom editor tool.  
### Description
Use this method to implement a custom editor tool.
This method is called for each window where the custom editor tool is active. If the custom editor tool is subscribed to SceneView.onSceneGUIDelegate, use this method to replace the callback. The onSceneGUIDelegate method is called for every open SceneView.
* * *
