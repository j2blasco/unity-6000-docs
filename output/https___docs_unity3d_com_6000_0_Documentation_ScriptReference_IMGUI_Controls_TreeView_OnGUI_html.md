* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.OnGUI.html

#  [TreeView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.html).OnGUI
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
public void OnGUI([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) rect); 
### Parameters
Parameter | Description  
---|---  
rect | Rect where the TreeView is rendered.  
### Description
This is the main GUI method of the TreeView, where the TreeViewItems are processed and drawn.
Call this at the point at which the TreeView should be rendered in the given Rect. If the TreeView is constructed with a [MultiColumnHeader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader.html) the header is included in the rect provided.
* * *
