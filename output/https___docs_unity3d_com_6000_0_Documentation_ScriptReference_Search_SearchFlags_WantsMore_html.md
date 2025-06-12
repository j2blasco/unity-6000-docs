* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.WantsMore.html

#  [SearchFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.html).WantsMore
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
Sets the search to search for all results. This might take longer than unusual if [SearchProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html) are using multiple sources of items (files on disk, AssetDatabase...)
```
using System.Collections.Generic;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Search;
using UnityEngine;

static class Example_SearchService_GetItems
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/SearchService[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.html)/GetItems")]
    public static void Run()
    {
        // Create a container to hold found items.
        var results = new List<SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html)>();

        // Create the search context that will be used to execute the query.
        using (var searchContext = SearchService.CreateContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.CreateContext.html)("scene", "is:leaf"))
        {
            // Initiate the query and get the results.
            // Note: it is recommended to use SearchService.Request[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.Request.html) if you wish to fetch the items asynchronously.
            results = SearchService.GetItems[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.GetItems.html)(searchContext, SearchFlags.WantsMore[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.WantsMore.html) | SearchFlags.Synchronous[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.Synchronous.html));

            // Print results
            foreach (var searchItem in results)
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(searchItem.GetDescription(searchContext));
        }
    }
}

```

* * *
