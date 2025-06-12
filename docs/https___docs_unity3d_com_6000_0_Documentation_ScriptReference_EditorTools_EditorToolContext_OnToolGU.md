* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolContext.OnToolGUI.html

#  [EditorToolContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolContext.html).OnToolGUI
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
window | The window that is displaying the active [EditorTool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool.html).  
### Description
Implements any common functionality for the set of manipulation tools available for this context.
Unity calls this method for each window where the current editor tool is active.
* * *
