* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.CreateContext.html

#  [SearchService](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.html).CreateContext
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
public static [Search.SearchContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) CreateContext(string searchText); 
## Declaration
public static [Search.SearchContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) CreateContext(string searchText, [Search.SearchFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.html) flags); 
## Declaration
public static [Search.SearchContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) CreateContext([Search.SearchProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html) provider, string searchText); 
## Declaration
public static [Search.SearchContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) CreateContext(string providerId, string searchText, [Search.SearchFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.html) flags); 
## Declaration
public static [Search.SearchContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) CreateContext(IEnumerable<string> providerIds, string searchText, [Search.SearchFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.html) flags); 
## Declaration
public static [Search.SearchContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) CreateContext(IEnumerable<SearchProvider> providers, string searchText, [Search.SearchFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.html) flags); 
### Parameters
Parameter | Description  
---|---  
searchText | Search Query.  
provider | Search provider (This search provider does not need to be active or registered).  
providerId | Unique search provider ID string (i.e. asset, scene, find, etc.)  
providerIds | List of search provider IDs.  
providers | List of search providers.  
flags | Options defining how the query is performed.  
### Returns
**SearchContext** Returns a new SearchContext. 
### Description
Creates context from a list of search provider IDs.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Search;
using UnityEngine;

static class Example_SearchService_CreateContext
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/SearchService[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.html)/CreateContext")]
    public static void Run()
    {
        using var searchContext = SearchService.CreateContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.CreateContext.html)("scene", "camera");
        using var results = SearchService.Request[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.Request.html)(searchContext, SearchFlags.Synchronous[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.Synchronous.html));
        {
            foreach (var label in results.Select(r => r.GetLabel(searchContext)))
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(label);
        }
    }
}


```

* * *
