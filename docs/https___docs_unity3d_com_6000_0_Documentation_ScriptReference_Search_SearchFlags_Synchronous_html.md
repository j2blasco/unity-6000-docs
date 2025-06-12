* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.Synchronous.html

#  [SearchFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.html).Synchronous
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
Search items are fetched synchronously. This can take a long time for some [SearchProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html) (like asset). Use at your own risk.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Search;
using UnityEngine;

public class SearchFlags_Synchronous
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/SearchFlags[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.html)/Synchronous")]
    static void Run()
    {
        using (var searchContext = SearchService.CreateContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.CreateContext.html)("menu", "Create"))
        {
            // ***IMPORTANT***: Synchronous search can take a long time to resolve depending on the provider (especially assets).
            // Unity suggests using SearchService.Request[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.Request.html).

            // Initiate the query and get the results.
            var results = SearchService.GetItems[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.GetItems.html)(searchContext, SearchFlags.Synchronous[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.Synchronous.html));

            foreach (var searchItem in results)
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(searchItem.GetDescription(searchContext));
        }
    }
}

```

* * *
