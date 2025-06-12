* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer-keywordCount.html

#  [SearchIndexer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.html).keywordCount
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
keywordCount; 
### Description
Returns the number keywords in the index.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Search;
using UnityEngine;

static class Example_SearchIndexer_keywordCount
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/SearchIndexer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.html)/keywordCount")]
    public static void Run()
    {
        var searchIndexer = new SearchIndexer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.html)();
        searchIndexer.Start();
        {
            var di = searchIndexer.AddDocument("unity");

            // Add some properties and save the filter keywords.
            searchIndexer.AddProperty("is", "awesome", di, saveKeyword: true);
            searchIndexer.AddProperty("search", "powerful", di, saveKeyword: true);
        }
        searchIndexer.Finish(() =>
        {
            OnIndexReady(searchIndexer);
            // Dispose the SearchIndexer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.html) when you are done with it.
            searchIndexer.Dispose();
        });
    }

    private static void OnIndexReady(SearchIndexer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.html) si)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Index contains {si.keywordCount} keywords");
    }
}

```

* * *
