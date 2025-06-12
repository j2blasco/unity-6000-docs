* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumnEventArgs.html

# SearchColumnEventArgs
struct in UnityEditor.Search
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
### Description
Search column event arguments are used by [SearchColumn.getter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumn-getter.html), [SearchColumn.drawer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumn-drawer.html) and [SearchColumn.setter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumn-setter.html) delegates.
### Properties
Property | Description  
---|---  
[column](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumnEventArgs-column.html) | Search column being handled by the current event.  
[context](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumnEventArgs-context.html) | Search context being used for the current event.  
[focused](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumnEventArgs-focused.html) | Indicates if the search column cell is currently focused.  
[item](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumnEventArgs-item.html) | Search item currently being used for the event.  
[multiple](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumnEventArgs-multiple.html) | Indicates if multiple search results are currently selected when processing the current event.  
[rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumnEventArgs-rect.html) | UnityEngine.Rect used to indicate the drawing boudaries of the SearchColumn.drawer event.  
[selected](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumnEventArgs-selected.html) | Indicates if the search result is currently selected.  
[value](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumnEventArgs-value.html) | Value obtained from SearchColumn.getter before calling SearchColumn.drawer.  
* * *
