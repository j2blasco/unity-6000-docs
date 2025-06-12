* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchQueryError.html

# SearchQueryError
class in UnityEditor.Search
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
Represents a query parsing error.
This class is only used in the context of [SearchProviders](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html), when performing a search. It allows a [SearchProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html) to report error during the parsing of the search query. Here is an example of a [SearchProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html) that uses a [QueryEngine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.html) and reports parsing errors:
```
public IEnumerable<T> Search(SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) context, SearchProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html) provider, IEnumerable<T> subset = null)
{
    var query = m_QueryEngine.ParseQuery(context.searchQuery, true);
    if (!query.valid)
    {
        if (reportError)
            context.AddSearchQueryErrors(query.errors.Select(e => new SearchQueryError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchQueryError.html)(e, context, provider)));
        return Enumerable.Empty<T>();
    }

    m_DoFuzzyMatch = query.HasToggle("fuzzy");
    IEnumerable<T> gameObjects = subset ?? m_Objects;
    return query.Apply(gameObjects, false);
}

```

In the previous example, the function "Search" would be called by the provider's [fetchItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.fetchItem.html).  
  
In the Search window, the errors are shown when there is no result available. ![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/Example_SearchQueryError.png).
### Properties
Property | Description  
---|---  
[context](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchQueryError-context.html) | The context in which this error was logged.  
[index](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchQueryError-index.html) | Index where the error occurred.  
[length](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchQueryError-length.html) | Length of the block that was being parsed.  
[provider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchQueryError-provider.html) | Which search provider logged this error.  
[reason](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchQueryError-reason.html) | The reason for the error.  
[type](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchQueryError-type.html) | The type of query error.  
### Constructors
Constructor | Description  
---|---  
[SearchQueryError](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchQueryError-ctor.html) | Creates a new SearchQueryError.  
* * *
