* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.NoIndexing.html

#  [SearchFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.html).NoIndexing
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
Prevents the search from using indexing. Asset Provider will use its builtin Find in Files provider.
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
* * *
