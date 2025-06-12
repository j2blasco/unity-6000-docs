* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.SetupDepthsFromParentsAndChildren.html

#  [TreeView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.html).SetupDepthsFromParentsAndChildren
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
protected static void SetupDepthsFromParentsAndChildren([IMGUI.Controls.TreeViewItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeViewItem.html) root); 
### Parameters
Parameter | Description  
---|---  
root | TreeViewItem from which the descendentans should have their depth updated.  
### Description
Utility method using the depth of the input TreeViewItem to set the correct depths for all its descendant TreeViewItems.
This method can be used to intitialize the TreeViewItems depth values after setting up the children properties of the TreeViewItems.  
  
Additional resources: [SetupDepthsFromParentsAndChildren](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.SetupDepthsFromParentsAndChildren.html), [BuildRoot](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.BuildRoot.html).
* * *
