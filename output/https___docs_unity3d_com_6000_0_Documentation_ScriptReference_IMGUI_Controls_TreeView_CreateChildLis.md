* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.CreateChildListForCollapsedParent.html

#  [TreeView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.html).CreateChildListForCollapsedParent
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
protected static List<TreeViewItem> CreateChildListForCollapsedParent(); 
### Description
Creates a dummy TreeViewItem list. Useful when overriding [BuildRows](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.BuildRows.html) to prevent building a full tree of items.
When building the rows in BuildRows, it is not necessary to create items for descendants of collapsed items because these descendants are not visible. This can be a useful optimization, particularly in large trees or trees that change often. However, collapsed items still require a foldout arrow to be shown to indicate the presence of children. This is achieved by creating a dummy list and assigning it to the [TreeViewItem.children](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeViewItem-children.html) property of the collapsed parent TreeViewItem.  
  
Additional resources: [BuildRows](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.BuildRows.html). [IsChildListForACollapsedParent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.IsChildListForACollapsedParent.html).
* * *
