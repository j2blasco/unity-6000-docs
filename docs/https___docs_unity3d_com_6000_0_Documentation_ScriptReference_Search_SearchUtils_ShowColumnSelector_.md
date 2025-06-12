* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.ShowColumnSelector.html

#  [SearchUtils](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.html).ShowColumnSelector
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
public static void ShowColumnSelector(Action<IEnumerable<SearchColumn>,int> columnsAddedHandler, IEnumerable<SearchColumn> columns, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) mousePosition, int activeColumnIndex); 
### Parameters
Parameter | Description  
---|---  
columnsAddedHandler | Select handler invoked when columns are selected.  
columns | A set of existing columns. This set can help populate the column selector.  
mousePosition | Mouse position when the window needs to be opened.  
activeColumnIndex | Any active column index that we pass back to the select handler.  
### Description
Opens an auxiliary column selector window to allow the user to search for a column to be added.
In example, the selected column could be added to an existing search property table.
* * *
