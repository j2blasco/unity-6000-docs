* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.GetDocument.html

#  [SearchIndexer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.html).GetDocument
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
public [Search.SearchDocument](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchDocument.html) GetDocument(int index); 
### Parameters
Parameter | Description  
---|---  
index | Valid index of the document to access.  
### Returns
**SearchDocument** Indexed search document. 
### Description
Returns a search document by its index.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Search;
using UnityEngine;

static class Example_SearchIndexer_GetDocument
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/SearchIndexer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.html)/GetDocument")]
    public static void Run()
    {
        var si = new SearchIndexer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.html)();
        si.Start();
        si.AddDocument("document 1");
        si.AddDocument("document 2");
        si.AddDocument("document 3");
        si.Finish(() =>
        {
            // Enumerate all documents
            for (int di = 0; di < si.documentCount; ++di)
            {
                var doc = si.GetDocument(di);
                Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(doc.id.StartsWith("document"));
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(doc.id);
            }

            // Dispose of the SearchIndexer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.html) when you are done with it.
            si.Dispose();
        });
    }
}

```

* * *
