* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.AddNumber.html

#  [SearchIndexer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.html).AddNumber
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
public void AddNumber(string key, double value, int score, int documentIndex); 
### Parameters
Parameter | Description  
---|---  
key | Key used to retrieve the value.  
value | Number value to store in the index.  
score | Relevance score of the word.  
documentIndex | Document where the indexed value was found.  
### Description
Adds a key-number value pair to the index. The key won't be added with variations.
```
using System.Linq;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Search;
using UnityEngine;

static class Example_SearchIndexer_AddNumber
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/SearchIndexer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.html)/AddNumber")]
    public static void Run()
    {
        var si = new SearchIndexer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.html)();
        si.Start();

        // Add some documents and index a power value that can be searched.
        si.AddNumber("power", 4.4, score: 0, si.AddDocument("Weak"));
        si.AddNumber("power", 6.42, score: 0, si.AddDocument("Healthy"));
        si.AddNumber("power", 9.9, score: 0, si.AddDocument("Strong"));

        si.Finish(() =>
        {
            SearchPowerLevels(si);
            // Dispose the SearchIndexer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.html) when you are done with it.
            si.Dispose();
        });
    }

    private static void SearchPowerLevels(SearchIndexer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.html) si)
    {
        SearchPowerLevel(si, "power<5", 1);
        SearchPowerLevel(si, "power>=6", 2);
    }

    static void SearchPowerLevel(SearchIndexer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.html) si, string powerQuery, int expectedCount)
    {
        var results = si.Search(powerQuery).ToList();
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(results.Count == expectedCount, "Invalid query");
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Document with {powerQuery}: {string.Join(", ", results.Select(r => r.id))}");
    }
}

```

* * *
