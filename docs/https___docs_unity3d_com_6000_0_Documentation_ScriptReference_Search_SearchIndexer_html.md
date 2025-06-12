* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.html

# SearchIndexer
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
Base class for a document Indexer which provides methods for retrieving a document given a specific pattern in roughly log(n). This allows you to search a large index more quickly.
This class contains resources that must be disposed when it is no longer needed. See [Dispose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.Dispose.html).
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
### Properties
Property | Description  
---|---  
[documentCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer-documentCount.html) | Returns the number of documents in the index.  
[keywordCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer-keywordCount.html) | Returns the number keywords in the index.  
[minQueryLength](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer-minQueryLength.html) | Minimal length of a query. By default it is 1 character.  
[minWordIndexationLength](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer-minWordIndexationLength.html) | Minimal indexed word size. Default is 2.  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer-name.html) | Name of the index. Generally this name is set by a user from SearchDatabase.Settings.  
[resolveDocumentHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer-resolveDocumentHandler.html) | Handler used to resolve a document ID to some other data string.  
[skipEntryHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer-skipEntryHandler.html) | Handler used to skip entries.  
[timestamp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer-timestamp.html) | Indicates when the search index was last modified.  
### Constructors
Constructor | Description  
---|---  
[SearchIndexer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer-ctor.html) | Creates a new default SearchIndexer.  
### Public Methods
Method | Description  
---|---  
[AddDocument](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.AddDocument.html) | Adds a new document to be indexed.  
[AddExactWord](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.AddExactWord.html) | Adds a new word coming from a document to the index. The word is added with multiple variations allowing partial search.  
[AddNumber](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.AddNumber.html) | Adds a key-number value pair to the index. The key won't be added with variations.  
[AddProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.AddProperty.html) | Adds a property value to the index. A property is specified with a key and a string value. The value will be stored with multiple variations.  
[AddWord](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.AddWord.html) | Adds a new word coming from a document to the index. The word is added with multiple variations allowing partial search.  
[Dispose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.Dispose.html) | Dispose of the SearchIndexer.  
[Finish](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.Finish.html) | Finalizes the current index, sorting and compiling of all the indexes.  
[GetDocument](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.GetDocument.html) | Returns a search document by its index.  
[GetMetaInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.GetMetaInfo.html) | Get metadata of a specific document.  
[IndexDocument](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.IndexDocument.html) | Function to override in a concrete SearchIndexer to index the content of a document.  
[IsReady](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.IsReady.html) | Indicates if the index is fully built, up to date, and ready for search.  
[LoadBytes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.LoadBytes.html) | Loads the index asynchronously (in another thread) from a binary buffer.  
[Merge](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.Merge.html) | Merge a search index content into the current index.  
[Read](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.Read.html) | Reads a stream and populates the index from it.  
[SaveBytes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.SaveBytes.html) | Get the bytes representation of this index. See SearchIndexer.Write.  
[Search](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.Search.html) | Runs a search query in the index.  
[SetMetaInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.SetMetaInfo.html) | Set arbiraty metadata on a specific document.  
[SkipEntry](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.SkipEntry.html) | Called when the index is built to see if a specified document needs to be indexed. See SearchIndexer.skipEntryHandler.  
[Start](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.Start.html) | Starts indexing entries.  
[Write](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.Write.html) | Writes a binary representation of the index on a stream.  
* * *
