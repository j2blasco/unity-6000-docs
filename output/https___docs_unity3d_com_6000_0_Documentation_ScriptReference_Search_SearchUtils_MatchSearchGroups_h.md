* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.MatchSearchGroups.html

#  [SearchUtils](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.html).MatchSearchGroups
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
public static bool MatchSearchGroups([Search.SearchContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) context, string content, bool ignoreCase); 
### Parameters
Parameter | Description  
---|---  
context | Search context containing the searchQuery that search tries to match.  
content | String content that is tokenized and used to match the search query.  
ignoreCase | Perform matching while ignoring letter casing.  
### Returns
**bool** If a match has occurred. 
### Description
Helper function to match a string against the SearchContext. This will try to match the search query against each token of content (similar to the AddComponent menu workflow).
```
private static IEnumerable<SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html)> SearchLogs(SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) context, SearchProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html) provider)
{
    lock (s_Logs)
    {
        if (!s_Initialized)
        {
            s_Initialized = true;
            Application.logMessageReceived[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-logMessageReceived.html) -= HandleLog;
            Application.logMessageReceived[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-logMessageReceived.html) += HandleLog;
        }
        for (int logIndex = 0; logIndex < s_Logs.Count; ++logIndex)
            yield return SearchLogEntry(context, provider, s_Logs[logIndex]);
    }
}

```

* * *
