* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer-skipEntryHandler.html

#  [SearchIndexer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.html).skipEntryHandler
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
skipEntryHandler; 
### Description
Handler used to skip entries.
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Search;
using UnityEngine;

static class Example_SearchIndexer_skipEntryHandler
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/SearchIndexer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.html)/skipEntryHandler")]
    public static void Run()
    {
        using var searchIndexer = new SearchIndexer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.html)
        {
            // The skip entry handler can be used to prevent some documents from being indexed.
            skipEntryHandler = SkipDocumentThatStartsWithAnUnderscore
        };

        searchIndexer.Start();
        {
            var di = searchIndexer.AddDocument("A/Valid/File[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.File.html)/Path");
            Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(di >= 0);

            // This document should get discarded.
            di = searchIndexer.AddDocument("_Not/Valid/File[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.File.html)/Path");
            Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(di == -1);
        }
        searchIndexer.Finish(Array.Empty<string>());

        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"{searchIndexer.documentCount} document were indexed");
    }

    private static bool SkipDocumentThatStartsWithAnUnderscore(string documentId)
    {
        return documentId[0] == '_';
    }
}

```

* * *
