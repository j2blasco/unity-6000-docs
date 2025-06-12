* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.SortItemIDsInRowOrder.html

#  [TreeView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.html).SortItemIDsInRowOrder
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
protected IList<int> SortItemIDsInRowOrder(IList<int> ids); 
### Parameters
Parameter | Description  
---|---  
ids | TreeViewItem IDs.  
### Description
Returns a list sorted in the order in which they are shown in the TreeView.
This can be useful when drag-and-dropping a multiselection, and you need the order of the dropped items to be the same as they are in the TreeView. By default, dragged items are in the order the selection was made.
* * *
