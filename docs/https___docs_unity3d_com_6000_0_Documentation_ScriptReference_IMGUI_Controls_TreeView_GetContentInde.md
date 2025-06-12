* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.GetContentIndent.html

#  [TreeView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.html).GetContentIndent
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
protected float GetContentIndent([IMGUI.Controls.TreeViewItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeViewItem.html) item); 
### Parameters
Parameter | Description  
---|---  
item | Item used to determine the indent.  
### Returns
**float** Indent. 
### Description
Returns the horizontal content offset for an item. This is where the content should begin (after the foldout arrow).
Use this when overriding [TreeView.RowGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.RowGUI.html) to make custom GUI content for the item.  
  
Additional resources: [GetFoldoutIndent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.GetFoldoutIndent.html).
* * *
