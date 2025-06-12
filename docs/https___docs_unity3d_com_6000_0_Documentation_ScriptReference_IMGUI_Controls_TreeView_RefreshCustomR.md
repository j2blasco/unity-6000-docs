* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.RefreshCustomRowHeights.html

#  [TreeView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.html).RefreshCustomRowHeights
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
protected void RefreshCustomRowHeights(); 
### Description
Refreshes the cache of custom row rects based on the heights returned by [GetCustomRowHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.GetCustomRowHeight.html).
This method calls [GetCustomRowHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.GetCustomRowHeight.html) for each of the current rows and caches the results. It is called automatically by the TreeView after [BuildRows](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.BuildRows.html) is called to ensure heights are in sync with the rows. Calling this method manually is needed when row heights changes dynamically e.g after a user action changes the content of a row.
* * *
