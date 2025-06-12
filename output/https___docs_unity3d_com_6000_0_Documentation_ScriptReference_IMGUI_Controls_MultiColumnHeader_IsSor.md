* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader.IsSortedAscending.html

#  [MultiColumnHeader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader.html).IsSortedAscending
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
public bool IsSortedAscending(int columnIndex); 
### Parameters
Parameter | Description  
---|---  
columnIndex | Column index.  
### Returns
**bool** True if sorted ascending. 
### Description
Check the sorting order state for a column.
This function checks and returns the sorting order; true for ascending order and false for descending order. The order is preserved for each column so it can be used to sort other columns. Use [sortedColumnIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader-sortedColumnIndex.html) to check if any column is actively used for sorting. You can then use that column index to get the sorting order.
* * *
