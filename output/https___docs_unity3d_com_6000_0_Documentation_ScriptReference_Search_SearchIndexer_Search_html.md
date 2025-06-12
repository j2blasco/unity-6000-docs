* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.Search.html

#  [SearchIndexer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.html).Search
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
public IEnumerable<SearchResult> Search([Search.SearchContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) context, [Search.SearchProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html) provider, int maxScore, int patternMatchLimit); 
## Declaration
public IEnumerable<SearchResult> Search(string query, [Search.SearchContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) context, [Search.SearchProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html) provider, int maxScore, int patternMatchLimit); 
## Declaration
public IEnumerable<SearchResult> Search(string query, int maxScore, int patternMatchLimit); 
### Parameters
Parameter | Description  
---|---  
query | Search query to look for. If if matches any of the indexed variations, a result is returned.  
context | The search context on which the query is applied.  
provider | The search provider that initiated the search.  
maxScore | Maximum match score of any matched Search Result. See [SearchResult.score](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchResult-score.html).  
patternMatchLimit | Maximum number of matched Search Results that can be returned. See [SearchResult](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchResult.html).  
### Returns
**IEnumerable <SearchResult>** Returns a collection of Search Results matching the query. 
### Description
Runs a search query in the index.
```
using System.Linq;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Search;
using UnityEngine;

static class Example_SearchIndexer_Search
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/SearchIndexer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.html)/Search")]
    public static void Run()
    {
        var si = new SearchIndexer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.html)();
        si.Start();

        // Index some documents and properties
        si.AddProperty("color", "red", si.AddDocument("RGB 55"));
        si.AddProperty("color", "reddish", si.AddDocument("RGB 45"));
        si.AddProperty("color", "yellow", si.AddDocument("RGB 66"));

        si.Finish(() =>
        {
            // Search document with property color=red*
            var results = si.Search("color:red").ToList();
            Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(results.Count == 2);
            if (results.Count > 0)
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(string.Join(", ", results.Select(r => $"{r.id} [{r.score}]")));
            // Dispose of the SearchIndexer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.html) when you are done with it.
            si.Dispose();
        });
    }
}


```

* * *
