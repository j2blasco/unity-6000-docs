* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.Request.html

#  [SearchService](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.html).Request
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
public static [Search.ISearchList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchList.html) Request(string searchText, [Search.SearchFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.html) options); 
## Declaration
public static [Search.ISearchList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchList.html) Request([Search.SearchContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) context, [Search.SearchFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.html) options); 
### Parameters
Parameter | Description  
---|---  
searchText | Search query to be executed.  
context | Search context used to track asynchronous requests. You need to dispose of the context yourself.  
options | Options defining how the query is performed.  
### Returns
**ISearchList** Asynchronous list of search items. 
### Description
Executes a search request that will fetch search results asynchronously.
The following example executes a query and print results over many frames using [EditorApplication.update](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-update.html).
```
[MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/SearchService[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.html)/Request[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Requests.Request.html) List")]
public static void RequestList()
{
    ISearchList[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchList.html) results = SearchService.Request[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.Request.html)("*.cs");

    // It is important to note that when you request some search results,
    // that you need to enumerate them asynchronously using the returned search list.
    AsyncResultEnumerator.Fetch(results, item => Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(item));
}

struct AsyncResultEnumerator
{
    private Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html)<SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html)> m_OnEnumerate;
    private IEnumerator<SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html)> m_Iterator;

    public static AsyncResultEnumerator Fetch(ISearchList[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchList.html) results, Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html)<SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html)> onEnumerate)
    {
        return new AsyncResultEnumerator(results, onEnumerate);
    }

    public AsyncResultEnumerator(ISearchList[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchList.html) results, Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html)<SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html)> onEnumerate)
    {
        m_OnEnumerate = onEnumerate;
        m_Iterator = results.GetEnumerator();
        EditorApplication.update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-update.html) += EnumerateResults;
    }

    private void EnumerateResults()
    {
        if (m_Iterator == null || !m_Iterator.MoveNext())
        {
            m_Iterator = null;
            EditorApplication.update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-update.html) -= EnumerateResults;
        }
        else if (m_Iterator.Current != null)
            m_OnEnumerate(m_Iterator.Current);
    }
}

```

If you are running a coroutine you can yield results like the following:
```
public static IEnumerable<SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html)> YieldResults()
{
    ISearchList[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchList.html) results = SearchService.Request[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.Request.html)("*.cs");
    foreach (var result in results)
        yield return result;
}

```

* * *
## Declaration
public static void Request(string searchText, Action<SearchContext,IList<SearchItem>> onSearchCompleted, [Search.SearchFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.html) options); 
## Declaration
public static void Request([Search.SearchContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) context, Action<SearchContext,IList<SearchItem>> onSearchCompleted, [Search.SearchFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.html) options); 
### Parameters
Parameter | Description  
---|---  
onSearchCompleted | Callback invoked when the search request is completed and all results are available.  
### Description
Executes a search request and calls back the specified function when all results are available.
```
[MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/SearchService[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.html)/Request[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Requests.Request.html) All")]
public static void RequestAll()
{
    SearchService.Request[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.Request.html)("t:texture", (SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) context, IList<SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html)> items) =>
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("All Textures");
        foreach (var item in items)
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(item);
    }, SearchFlags.Debug[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.Debug.html));
}

```

* * *
## Declaration
public static void Request(string searchText, Action<SearchContext,IEnumerable<SearchItem>> onIncomingItems, Action<SearchContext> onSearchCompleted, [Search.SearchFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.html) options); 
## Declaration
public static void Request([Search.SearchContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) context, Action<SearchContext,IEnumerable<SearchItem>> onIncomingItems, Action<SearchContext> onSearchCompleted, [Search.SearchFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.html) options); 
### Parameters
Parameter | Description  
---|---  
onIncomingItems | Callback invoked everytime a batch of results are found and available.  
onSearchCompleted | Callback invoked when the search request is completed.  
### Description
Executes a search request and callbacks for every batch of incoming results. It is possible to get duplicate items, so filter the final list if needed.
```
[MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/SearchService[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.html)/Request[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Requests.Request.html) Async")]
public static void RequestAsync()
{
    var batchCount = 0;
    var totalItemCount = 0;

    void OnIncomingResults(SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) context, IEnumerable<SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html)> items)
    {
        var batchItemCount = items.Count();
        totalItemCount += batchItemCount;
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"#{++batchCount} Incoming materials ({batchItemCount}): {string.Join("\n", items)}");
    }

    void OnSearchCompleted(SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) context)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Query <b>\"{context.searchText}\"</b> completed with a total of {totalItemCount}");
    }

    SearchService.Request[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.Request.html)("t:material", OnIncomingResults, OnSearchCompleted, SearchFlags.Debug[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.Debug.html));
}

```

* * *
