* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.RefreshFlags.html

# RefreshFlags
enumeration
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
Refresh flags are used to indicate why search view needs to be refreshed or updated.
### Properties
Property | Description  
---|---  
[None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.RefreshFlags.None.html) | No particular refresh reason were specified.  
[Default](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.RefreshFlags.Default.html) | Normal refresh.  
[StructureChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.RefreshFlags.StructureChanged.html) | The structure of the current selection data has changed (i.e. the selected scene object got a new component).  
[DisplayModeChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.RefreshFlags.DisplayModeChanged.html) | The display mode or item size has changed.  
[ItemsChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.RefreshFlags.ItemsChanged.html) | The search item list has been updated.  
[GroupChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.RefreshFlags.GroupChanged.html) | The current item group has changed. In example, the user selected a new search tab.  
[QueryStarted](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.RefreshFlags.QueryStarted.html) | A search query is about to be executed.  
[QueryCompleted](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.RefreshFlags.QueryCompleted.html) | A search query has completed.  
* * *
