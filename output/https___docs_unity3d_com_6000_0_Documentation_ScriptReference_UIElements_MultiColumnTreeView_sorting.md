* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MultiColumnTreeView-sortingMode.html

#  [MultiColumnTreeView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MultiColumnTreeView.html).sortingMode
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
[UIElements.ColumnSortingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ColumnSortingMode.html) sortingMode; 
### Description
Indicates how to sort columns. To enable sorting, set it to [ColumnSortingMode.Default](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ColumnSortingMode.Default.html) or [ColumnSortingMode.Custom](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ColumnSortingMode.Custom.html). The `Default` mode uses the sorting algorithm provided by [MultiColumnController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MultiColumnController.html), acting on indices. You can also implement your own sorting with the `Custom` mode, by responding to the columnSortingChanged event. 
**Note** : If there is at least one sorted column, reordering is temporarily disabled. 
* * *
