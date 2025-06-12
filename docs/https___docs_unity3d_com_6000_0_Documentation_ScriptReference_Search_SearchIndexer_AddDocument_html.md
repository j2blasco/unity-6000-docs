* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.AddDocument.html

#  [SearchIndexer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.html).AddDocument
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
public int AddDocument(string document, bool checkIfExists); 
## Declaration
public int AddDocument(string document, string name, string source, bool checkIfExists, [Search.SearchDocumentFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchDocumentFlags.html) flags); 
### Parameters
Parameter | Description  
---|---  
document | Unique document ID.  
name | Name of path of the document.  
source | Source of the document. In example, if the document is a nested object, the source should be the container asset path.  
checkIfExists | Pass true if this document has some chance of existing already.  
flags | Flags describing the nature of the document.  
### Returns
**int** The document index/handle used to add new index entries. 
### Description
Adds a new document to be indexed.
```
using System.Linq;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Search;
using UnityEngine;

static class Example_SearchIndexer_AddDocument
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/SearchIndexer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.html)/AddDocument")]
    public static void Run()
    {
        var si = new SearchIndexer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.html)();
        si.Start();

        // The most efficient way of adding a document is by not checking if the
        // document ID was already added if you are sure that all your document IDs are unique.
        var di = si.AddDocument("document1", checkIfExists: false);

        // You can set `checkIfExists=true` to check for existing document IDs, and the system
        // will return an index of any existing document IDs.
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(di == si.AddDocument("document1", checkIfExists: true));

        // Once you have added a new document, you need to use the returned handle to index words, numbers and properties.
        si.AddWord("unity", 0, di);
        si.AddProperty("is", "awesome", di);
        si.AddNumber("version", 3.0, score: 0, di);

        si.Finish(() =>
        {
            Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(si.Search("unity version>=3").Count() == 1, "No result were found");
            // Dispose of the SearchIndexer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.html) when you are done with it.
            si.Dispose();
        });
    }
}


```

* * *
