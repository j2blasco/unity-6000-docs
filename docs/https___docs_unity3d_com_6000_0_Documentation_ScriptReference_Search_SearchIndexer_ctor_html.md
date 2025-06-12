* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer-ctor.html

# SearchIndexer Constructor
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
public SearchIndexer(); 
## Declaration
public SearchIndexer(string name); 
### Parameters
Parameter | Description  
---|---  
name | Name of the indexer.  
### Description
Creates a new default SearchIndexer.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Search;
using UnityEngine;

static class Example_SearchIndexer
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/SearchIndexer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.html)/Class")]
    public static void Run()
    {
        // Create a search indexer
        using var searchIndexer = new SearchIndexer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.html)("SearchIndexerExample");

        // Indicate that searchIndexer is about to index documents
        searchIndexer.Start();

        // Add some documents
        var unityDocumentIndex = searchIndexer.AddDocument("Unity Technologies");

        // Index some words
        var baseScore = 42;
        searchIndexer.AddWord("unity", baseScore, unityDocumentIndex);
        searchIndexer.AddWord("is", baseScore, unityDocumentIndex);
        searchIndexer.AddWord("awesome", baseScore, unityDocumentIndex);

        // Indicate that searchIndexer is finished indexing documents and is ready to search.
        searchIndexer.Finish();

        // Wait for the indexation to finish.
        while (!searchIndexer.IsReady())
            ;

        // Search the index
        foreach (var result in searchIndexer.Search("uni"))
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Found document [{result.index}] {result.id} ({result.score})");
    }
}

```

* * *
