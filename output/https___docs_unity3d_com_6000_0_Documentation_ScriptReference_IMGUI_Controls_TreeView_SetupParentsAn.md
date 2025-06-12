* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.SetupParentsAndChildrenFromDepths.html

#  [TreeView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.html).SetupParentsAndChildrenFromDepths
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
protected static void SetupParentsAndChildrenFromDepths([IMGUI.Controls.TreeViewItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeViewItem.html) root, IList<TreeViewItem> rows); 
### Parameters
Parameter | Description  
---|---  
root | The hidden root item.  
rows | TreeViewItems where only the depth property have been set.  
### Description
Utility method for initializing all the parent and children properties of the rows using the order and the depths values that have been set.
Some tree data models are based on order and depth information only. This method can be called after creating all the rows to initalize the ‘parent’ and ‘children’ properties for each TreeViewItem in ‘rows’ based on the depth information for each item. This method assumes that the data presented in `rows` is in the order it should appear from top to bottom in the TreeView.  
  
Additional resources: [SetupDepthsFromParentsAndChildren](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.SetupDepthsFromParentsAndChildren.html), [BuildRoot](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.BuildRoot.html).
* * *
