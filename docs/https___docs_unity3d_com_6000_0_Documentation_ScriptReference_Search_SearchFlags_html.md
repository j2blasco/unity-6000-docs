* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.html

# SearchFlags
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
Search options used to fetch items. Mostly with [SearchContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) to specify how a search should be handled.
```
using System.Collections;
using System.Collections.Generic;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Search;
using UnityEngine;

public class SearchFlags_NoIndexing
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/SearchFlags[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.html)/NoIndexing")]
    public static void RequestAll()
    {
        // Find all assets matching the word Search without using any indexed data (will rely on the Find Files provider).
        SearchService.Request[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.Request.html)("p: Search", (SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) context, IList<SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html)> items) =>
        {
            foreach (var item in items)
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(item);
        }, SearchFlags.NoIndexing[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.NoIndexing.html));
    }
}

```

### Properties
Property | Description  
---|---  
[None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.None.html) | No specific search options. Result will be unsorted.  
[Synchronous](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.Synchronous.html) | Search items are fetched synchronously. This can take a long time for some SearchProvider (like asset). Use at your own risk.  
[Sorted](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.Sorted.html) | Fetched items are sorted by the search service.  
[FirstBatchAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.FirstBatchAsync.html) | Sends the first items asynchronously.  
[WantsMore](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.WantsMore.html) | Sets the search to search for all results. This might take longer than unusual if SearchProvider are using multiple sources of items (files on disk, AssetDatabase...)  
[Debug](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.Debug.html) | Adds debugging information to SearchItem while looking for results.  
[NoIndexing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.NoIndexing.html) | Prevents the search from using indexing. Asset Provider will use its builtin Find in Files provider.  
[Expression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.Expression.html) | Indicates that the search query will be evaluated as a search expression.  
[QueryString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.QueryString.html) | Evaluate the search text as a pure query string (do not evaluate the text as a search expression).  
[Packages](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.Packages.html) | The Object Picker window will include any results from packages.  
[Default](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.Default.html) | Default Search Flag (SearchFlags.Sorted).  
[AllProvidersAvailable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.AllProvidersAvailable.html) | All SearchProviders are available in the SearchWindow dropdown menu.  
[UseSessionSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.UseSessionSettings.html) | Persist the SearchContext state in between sessions using the SearchViewState.sessionName as its data key.  
[ShowErrorsWithResults](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.ShowErrorsWithResults.html) | Always show query errors even when there are results available. This flag is only usable with internal API.  
[ReuseExistingWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.ReuseExistingWindow.html) | Indicates that the search view will find any existing window instances that are already opened before creating a new one. This flag is only usable with internal API.  
[Multiselect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.Multiselect.html) | Indicates that the search view will allow multi-selection. This flag is only usable with internal API.  
[Dockable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.Dockable.html) | Indicates that the search view is dockable. This flag is only usable with internal API.  
[FocusContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.FocusContext.html) | Indicates that the search view will focus on the first contextual search provider available when it opens. This flag is only usable with internal API.  
[HidePanels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.HidePanels.html) | Indicates that the search view will hide its side panels when it opens. This flag is only usable with internal API.  
[GeneralSearchWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.GeneralSearchWindow.html) | This is a general purpose search window that has access to all Providers in the SearchService.  
[OpenDefault](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.OpenDefault.html) | Opens a search view with default options. This flag is only usable with internal API.  
[OpenGlobal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.OpenGlobal.html) | Opens a search view for a global search. This flag is only usable with internal API.  
[OpenContextual](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.OpenContextual.html) | Opens a search view with default contextual options. This flag is only usable with internal API.  
[OpenPicker](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.OpenPicker.html) | Opens a search view as an object picker. This flag is only usable with internal API.  
* * *
