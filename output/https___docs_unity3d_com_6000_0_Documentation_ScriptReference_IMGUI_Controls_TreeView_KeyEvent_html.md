* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.KeyEvent.html

#  [TreeView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.html).KeyEvent
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
protected void KeyEvent(); 
### Description
Override this method to handle events when the TreeView has keyboard focus.
The TreeView should not handle key events if it does not have keyboard focus therefore this method is only called when [GUIUtility.keyboardControl](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility-keyboardControl.html) == [treeViewControlID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView-treeViewControlID.html).
* * *
