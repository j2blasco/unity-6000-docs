* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.ProjectSearch.html

# ProjectSearch
class in UnityEditor.SearchService
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
Use this API to perform searches in the Project. Engines for this type of search implement the [IProjectSearchEngine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.IProjectSearchEngine.html) interface.
Registered Project search engines are called during searches in the Project browser. When the default object selector is used, they are also called for Asset searches.  
  
The following example creates a Project search engine:
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.Collections.Generic;
using System.Linq;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.SearchService;
using UnityEngine;
using Object = UnityEngine.Object;  
  
[ProjectSearchEngine]
class TestProjectSearchEngine : IProjectSearchEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.IProjectSearchEngine.html)
{
    public string name => "My Custom Engine";  
  
    public void BeginSession(ISearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.ISearchContext.html) context)
    {
    }  
  
    public void EndSession(ISearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.ISearchContext.html) context)
    {
    }  
  
    public void BeginSearch(ISearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.ISearchContext.html) context, string query)
    {
    }  
  
    public void EndSearch(ISearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.ISearchContext.html) context)
    {
    }  
  
    public IEnumerable<string> Search(ISearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.ISearchContext.html) context, string query, Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html)<IEnumerable<string>> asyncItemsReceived)
    {
        var allPaths = AssetDatabase.GetAllAssetPaths();
        var filteredPaths = allPaths.Where(path => !path.StartsWith("Library")).Where(path => path.IndexOf(query, StringComparison.InvariantCultureIgnoreCase) >= 0).ToList();
        return filteredPaths;
    }
}

```

Additional resources: [ProjectSearchEngineAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.ProjectSearchEngineAttribute.html), [IProjectSearchEngine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.IProjectSearchEngine.html).
### Static Properties
Property | Description  
---|---  
[EngineScope](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.ProjectSearch.EngineScope.html) | A enum that indicates the search scope for ProjectSearch engines. It is used by ProjectSearchContext.  
### Static Methods
Method | Description  
---|---  
[RegisterEngine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.ProjectSearch.RegisterEngine.html) | Registers a Project search engine dynamically.  
[UnregisterEngine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.ProjectSearch.UnregisterEngine.html) | Unregisters a dynamically registered engine.  
* * *
