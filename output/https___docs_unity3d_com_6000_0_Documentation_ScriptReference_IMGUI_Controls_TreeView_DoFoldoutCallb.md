* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.DoFoldoutCallback.html

#  [TreeView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.html).DoFoldoutCallback
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
public delegate bool DoFoldoutCallback([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, bool expandedState, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style); 
### Parameters
Parameter | Description  
---|---  
position | Rect to draw the foldout.  
expandedState | Current foldout state.  
style | Toggle button style.  
### Returns
**bool** Returns true if the foldout is still expanded. Otherwise, returns false. 
### Description
Callback signature used to override the TreeView foldout. See [foldoutOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView-foldoutOverride.html).
* * *
