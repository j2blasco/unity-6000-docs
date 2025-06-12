* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.BeginRename.html

#  [TreeView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.html).BeginRename
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
public bool BeginRename([IMGUI.Controls.TreeViewItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeViewItem.html) item); 
## Declaration
public bool BeginRename([IMGUI.Controls.TreeViewItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeViewItem.html) item, float delay); 
### Parameters
Parameter | Description  
---|---  
item | Item to rename.  
delay | Delay in seconds until the rename overlay shows.  
### Returns
**bool** Returns true if renaming was started. Returns false if renaming was already active. 
### Description
Shows the rename overlay for a TreeViewItem.
This renames the [TreeViewItem.displayName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeViewItem-displayName.html) string.
* * *
