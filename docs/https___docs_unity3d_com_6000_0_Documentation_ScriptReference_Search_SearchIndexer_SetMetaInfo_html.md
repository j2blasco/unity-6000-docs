* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.SetMetaInfo.html

#  [SearchIndexer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.html).SetMetaInfo
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
public void SetMetaInfo(string documentId, string metadata); 
### Parameters
Parameter | Description  
---|---  
documentId | Id of a document.  
metadata | Metadata to bind to that document.  
### Description
Set arbiraty metadata on a specific document.
```
using System.IO;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Search;
using UnityEngine;

/// <summary>
/// Use GetMetaInfo to store some additional data about a specific document within the index db
/// that you can retrieve later if needed.
/// </summary>
static class Example_SearchIndexer_GetMetaInfo
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/SearchIndexer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.html)/GetMetaInfo")]
    public static void Run()
    {
        var si = new SearchIndexer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.html)();
        si.Start();
        var newDocumentId = System.Guid.NewGuid().ToString("N");
        var di = si.AddDocument(newDocumentId);
        si.SetMetaInfo(newDocumentId, "Please save this data for later");
        si.Finish((bytes) =>
        {
            File.WriteAllBytes[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.File.WriteAllBytes.html)("Temp/index.db", bytes);
            EditorApplication.delayCall[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-delayCall.html) += ReloadIndex;
            // Dispose of the SearchIndexer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.html) when you are done with it.
            si.Dispose();
        }, null);
    }

    private static void ReloadIndex()
    {
        var si = new SearchIndexer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.html)();
        si.LoadBytes(File.ReadAllBytes[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.File.ReadAllBytes.html)("Temp/index.db"), (success) =>
        {
            Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(success);
            Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(si.GetMetaInfo(si.GetDocument(0).id) == "Please save this data for later");
            // Dispose of the SearchIndexer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.html) when you are done with it.
            si.Dispose();
        });
    }
}

```

* * *
