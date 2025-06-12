* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.SearchEngineScope.html

# SearchEngineScope
enumeration
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
An enumeration that contains the available search engine scopes.
A search engine scope identifies where a search comes from. This is useful when implementing a single entry point for the base engine functions:
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.Collections.Generic;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.SearchService;

class BaseEngine : ISearchEngineBase[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.ISearchEngineBase.html)
{
    public virtual void BeginSession(ISearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.ISearchContext.html) context)
    {
        if (context.engineScope == ObjectSelectorSearch.EngineScope[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.ObjectSelectorSearch.EngineScope.html) || context.engineScope == ProjectSearch.EngineScope[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.ProjectSearch.EngineScope.html))
        {
            // Cache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html) Assets.
        }
        if (context.engineScope == ObjectSelectorSearch.EngineScope[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.ObjectSelectorSearch.EngineScope.html) || context.engineScope == SceneSearch.EngineScope[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.SceneSearch.EngineScope.html))
        {
            // Cache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html) Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) objects.
        }
    }

    public virtual void EndSession(ISearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.ISearchContext.html) context)
    {
        // Flush any cached data.
    }

    public virtual void BeginSearch(ISearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.ISearchContext.html) context, string query)
    {
    }

    public virtual void EndSearch(ISearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.ISearchContext.html) context)
    {
    }

    public string name => "My Engine Service[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Service.html)";
}

[SceneSearchEngine]
class SampleSceneFilterEngine : BaseEngine, ISceneSearchEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.ISceneSearchEngine.html)
{
    public bool Filter(ISearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.ISearchContext.html) context, string query, HierarchyProperty objectToFilter)
    {
        // Use cached Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) objects.
        // ...
        return true;
    }
}

[ProjectSearchEngine]
class SampleProjectSearchEngine : BaseEngine, IProjectSearchEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.IProjectSearchEngine.html)
{
    public IEnumerable<string> Search(ISearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.ISearchContext.html) context, string query, Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html)<IEnumerable<string>> asyncItemsReceived)
    {
        // Use cached Assets.
        // ...
        return new List<string>();
    }
}

[ObjectSelectorEngine]
class SampleObjectSelectorEngine : BaseEngine, IObjectSelectorEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.IObjectSelectorEngine.html)
{
    public bool SelectObject(ISearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.ISearchContext.html) context, Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html)<UnityEngine.Object, bool> onObjectSelectorClosed, Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html)<UnityEngine.Object> onObjectSelectedUpdated)
    {
        // Use cached Assets and Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) objects.
        return true;
    }

    public void SetSearchFilter(ISearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.ISearchContext.html) context, string searchFilter)
    {}
}

```

### Properties
Property | Description  
---|---  
[Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.SearchEngineScope.Scene.html) | Identifies a search for Scene engines.  
[Project](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.SearchEngineScope.Project.html) | Identifies a search for Project engines.  
[ObjectSelector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.SearchEngineScope.ObjectSelector.html) | Identifies a search for ObjectSelector engines.  
* * *
