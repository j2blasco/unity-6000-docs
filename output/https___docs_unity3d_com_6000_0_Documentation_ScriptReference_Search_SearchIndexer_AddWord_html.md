* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.AddWord.html

#  [SearchIndexer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.html).AddWord
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
public void AddWord(string word, int score, int documentIndex); 
## Declaration
public void AddWord(string word, int size, int score, int documentIndex); 
## Declaration
public void AddWord(string word, int minVariations, int maxVariations, int score, int documentIndex); 
### Parameters
Parameter | Description  
---|---  
word | Word to add to the index.  
score | Relevance score of the word.  
documentIndex | Document where the indexed word was found.  
size | Number of variations to compute.  
minVariations | Minimum number of variations to compute. Cannot be higher than the length of the word.  
maxVariations | Maximum number of variations to compute. Cannot be higher than the length of the word.  
### Description
Adds a new word coming from a document to the index. The word is added with multiple variations allowing partial search.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Search;
using UnityEngine;

static class Example_SearchIndexer_AddWord
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/SearchIndexer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.html)/AddWord")]
    public static void Run()
    {
        // Create a search indexer
        var searchIndexer = new SearchIndexer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.html)("SearchIndexerAddWordExample");

        // Indicate that Search is about to index documents.
        searchIndexer.Start();

        // Add a document
        var di = searchIndexer.AddDocument("My/File[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.File.html)/Path");

        // Index some words
        var baseScore = 42;

        // This will index all variation of the word awesome, i.e. aw, awe, awes, aweso, awesom and awesome
        searchIndexer.AddWord("awesome", baseScore, di);

        // This will index an exact match for "unity", so no variation.
        searchIndexer.AddWord("unity", "unity".Length[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Length.html), baseScore, di);

        // This will only index variations for the word from character indexes 3 to 6, e.g. thi, this, thisi and thisis
        searchIndexer.AddWord("thisisitasuperlongword", 3, 6, baseScore, di);

        // Indicate that searchIndexer is finished indexing a document and is ready to search.
        searchIndexer.Finish(() =>
        {
            // Search the index
            foreach (var result in searchIndexer.Search("unity awes this"))
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Found document [{result.index}] {result.id} ({result.score})");

            // Dispose of the SearchIndexer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.html) when you are done with it.
            searchIndexer.Dispose();
        });
    }
}

```

* * *
