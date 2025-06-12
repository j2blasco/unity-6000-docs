* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItemOptions.Ellipsis.html

#  [SearchItemOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItemOptions.html).Ellipsis
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
If the description is longer than the width of the search view, truncates the description and adds an ellipsis.
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
* * *
