* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.GetDescendantsThatHaveChildren.html

#  [TreeView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.html).GetDescendantsThatHaveChildren
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
protected IList<int> GetDescendantsThatHaveChildren(int id); 
### Parameters
Parameter | Description  
---|---  
id | TreeViewItem ID.  
### Returns
**IList <int>** Descendants that have children. 
### Description
Returns all descendants for the item with ID id that have children.
It is used for expanding entire sub-trees. It is called automatically from some TreeView methods. If the full item tree has not been built in BuildRoot(), then override this method and use your back-end data to find the correct descendants for the given item.   
  
  
Default behavior: The item with ID id is found by searching from the rootItem through all its descendants. Once found, all its descendants that have children are collected. Assumes the full tree has been built.  
  
Additional resources: [GetAncestors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.GetAncestors.html).
* * *
