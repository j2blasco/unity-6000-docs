* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItemOptions.html

# SearchItemOptions
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
Indicates how the search item description needs to be formatted when presented to the user.
```
private static SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html) SearchLogEntry(SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) context, SearchProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html) provider, LogEntry logEntry)
{
    if (!SearchUtils.MatchSearchGroups[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.MatchSearchGroups.html)(context, logEntry.msgLowerCased, true))
        return null;

    var logItem = provider.CreateItem(context, logEntry.id, ~logEntry.lineNumber, logEntry.msg, null, null, logEntry);
    logItem.options = SearchItemOptions.Ellipsis[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItemOptions.Ellipsis.html) | SearchItemOptions.RightToLeft[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItemOptions.RightToLeft.html) | SearchItemOptions.Highlight[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItemOptions.Highlight.html);
    return logItem;
}

```

### Properties
Property | Description  
---|---  
[None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItemOptions.None.html) | Uses default description.  
[Ellipsis](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItemOptions.Ellipsis.html) | If the description is longer than the width of the search view, truncates the description and adds an ellipsis.  
[RightToLeft](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItemOptions.RightToLeft.html) | If the description is longer than the search view, keeps the last characters.  
[Highlight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItemOptions.Highlight.html) | Highlights parts of the description that match the Search Query.  
[FuzzyHighlight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItemOptions.FuzzyHighlight.html) | Highlights parts of the description that match the Fuzzy Search Query.  
[Compacted](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItemOptions.Compacted.html) | Uses Label instead of description for shorter display.  
[AlwaysRefresh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItemOptions.AlwaysRefresh.html) | Indicates that the item will always be refreshed.  
[FullDescription](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItemOptions.FullDescription.html) | The item description that is displayed in full mode. This is usually the case when the description is displayed in the Preview Inspector as opposed to the Result View.  
[CustomAction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItemOptions.CustomAction.html) | Indicates that the item is used as a built-in or custom user action that should always be displayed on top of result views.  
* * *
