* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider-onEnable.html

#  [SearchProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html).onEnable
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
[Unity.Android.Gradle.Manifest.Action](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) onEnable; 
### Description
Called when the SearchWindow is opened. Allows the search provider to perform some caching.
```
using System.Collections.Generic;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Search;
using UnityEngine;

static class LightsSearchProvider
{
    [SearchItemProvider]
    internal static SearchProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html) CreateProvider()
    {
        return new SearchProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html)("example_lights", "Lights")
        {
            filterId = "z:",
            priority = 99999, // Put example provider at a low priority
            showDetailsOptions = ShowDetailsOptions.Inspector[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ShowDetailsOptions.Inspector.html),
            fetchItems = (context, items, provider) => FetchItems(context, provider),
            toObject = (item, type) => item.data as Light[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html),
            onEnable = () => { /*Cache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html) some data in here*/ },
            onDisable = () => { /*Clear the cache*/ },

            // This provider can be used in the scene view contextually.
            isEnabledForContextualSearch = () => IsFocusedWindowTypeName("SceneView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.html)")
        };
    }

    static IEnumerable<SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html)> FetchItems(SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) context, SearchProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html) provider)
    {
        if (context.empty)
            yield break;

        var sceneProvider = SearchService.GetProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.GetProvider.html)("scene");
        using (var sceneQuery = SearchService.CreateContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.CreateContext.html)(sceneProvider, $"t:light {context.searchQuery}"))
        using (var results = SearchService.Request[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.Request.html)(sceneQuery))
        {
            var lightIcon = EditorGUIUtility.FindTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.FindTexture.html)("Lighting");
            foreach (var r in results)
            {
                if (r == null)
                {
                    // ***IMPORTANT***: Make sure to yield so you do not block the main thread waiting for results.
                    yield return null;
                }
                else
                {
                    yield return provider.CreateItem(context, r.id,
                        r.GetLabel(sceneQuery, true), r.GetDescription(sceneQuery, true),
                        lightIcon, r.ToObject<GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)>().GetComponent<Light[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html)>());
                }
            }
        }
    }

    static bool IsFocusedWindowTypeName(string focusWindowName)
    {
        return EditorWindow.focusedWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow-focusedWindow.html) != null && EditorWindow.focusedWindow.GetType().ToString().EndsWith("." + focusWindowName);
    }

    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/SearchProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html)/Show lights")]
    public static void ShowLights()
    {
        // Search for directional lights (lights with "directional" in their name)
        SearchService.ShowWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.ShowWindow.html)(SearchService.CreateContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.CreateContext.html)("z:directional"));
    }
}

```

* * *
