* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchMonitor.GetView.html

#  [SearchMonitor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchMonitor.html).GetView
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
public static [Search.SearchMonitorView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchMonitorView.html) GetView(bool delayedSync); 
### Parameters
Parameter | Description  
---|---  
delayedSync | Boolean indicating if the sync between views should only happen when the view is disposed, or for every operation. Default is false.  
### Returns
**SearchMonitorView** A [SearchMonitorView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchMonitorView.html). 
### Description
Returns a [SearchMonitorView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchMonitorView.html) to access Search's main [PropertyDatabases](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.html).
Multiple nested calls to [GetView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchMonitor.GetView.html) are supported. If those calls are on the same thread, it will return the same instance to avoid opening and closing new views. If the calls are on different threads, new views will be opened. Here is an example of a custom Scene [SearchProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html) using [GetView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchMonitor.GetView.html) to cache data in Search's main [PropertyDatabases](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.html) to increase search speed:
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.Collections.Generic;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Search;
using UnityEngine;

static class CustomSceneProvider
{
    const string k_ProviderId = "customSceneProvider";

    static QueryEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html)<GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)> s_QueryEngine;

    [SearchItemProvider]
    public static SearchProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html) CreateSearchProvider()
    {
        return new SearchProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html)(k_ProviderId, "Custom Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html)")
        {
            filterId = "csp:",
            isExplicitProvider = true,
            fetchItems = (context, items, provider) => FetchItems(context, provider),
            onEnable = OnEnable
        };
    }

    static void OnEnable()
    {
        s_QueryEngine = new QueryEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html)<GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)>(true);
        s_QueryEngine.SetSearchDataCallback(go => new []{ go.name });
        s_QueryEngine.AddFilter("p", OnPropertyFilter, s => s, StringComparison.OrdinalIgnoreCase);

        // Setup all the SearchValue[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchValue.html) handlers.
        SearchValue.SetupEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchValue.SetupEngine.html)(s_QueryEngine);
    }

    static IEnumerable<SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html)> FetchItems(SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) context, SearchProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html) provider)
    {
        // Parse the search query.
        var query = s_QueryEngine.ParseQuery(context.searchQuery);
        if (query == null)
            yield break;

        // If there are any errors, report them.
        if (!query.valid)
        {
            foreach (var queryError in query.errors)
            {
                context.AddSearchQueryError(new SearchQueryError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchQueryError.html)(queryError, context, provider));
            }
            yield break;
        }

        // Open a view on Search's main PropertyDatabases for the duration of the search. By opening
        // a view here, it reduces the time spent opening new views for each game object we filter in OnPropertyFilter.
        using (SearchMonitor.GetView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchMonitor.GetView.html)())
        {
            var filteredObjects = query.Apply(SearchUtils.FetchGameObjects[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.FetchGameObjects.html)());
            foreach (var filteredObject in filteredObjects)
            {
                var instanceId = filteredObject.GetHashCode();
                yield return provider.CreateItem(context, instanceId.ToString(), ~instanceId, filteredObject.name, null, null, null);
            }
        }
    }

    static SearchValue[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchValue.html) OnPropertyFilter(GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) go, string propertyName)
    {
        if (!go)
            return SearchValue.invalid[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchValue-invalid.html);
        if (string.IsNullOrEmpty(propertyName))
            return SearchValue.invalid[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchValue-invalid.html);

        // Opening a view here will only return the existing instance of the view if it's already open.
        using (var view = SearchMonitor.GetView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchMonitor.GetView.html)())
        {
            var documentKey = GetDocumentKey(go);
            var propertyPath = GetPropertyPath(go, propertyName);
            var recordKey = PropertyDatabase.CreateRecordKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.CreateRecordKey.html)(documentKey, PropertyDatabase.CreatePropertyHash[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.CreatePropertyHash.html)(propertyPath));
            if (view.TryLoadProperty(recordKey, out object data) && data is SearchValue[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchValue.html) sv)
                return sv;

            foreach (var c in EnumerateSubObjects(go))
            {
                var property = FindPropertyValue(c, propertyName);
                if (property.valid)
                {
                    view.StoreProperty(recordKey, property);
                    return property;
                }
            }

            view.StoreProperty(recordKey, SearchValue.invalid[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchValue-invalid.html));
        }

        return SearchValue.invalid[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchValue-invalid.html);
    }

    static IEnumerable<UnityEngine.Object> EnumerateSubObjects(GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) go)
    {
        yield return go;

        var gocs = go.GetComponents<Component[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html)>();
        for (int componentIndex = 0; componentIndex < gocs.Length; ++componentIndex)
        {
            var c = gocs[componentIndex];
            if (!c || (c.hideFlags & HideFlags.HideInInspector[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideFlags.HideInInspector.html)) == HideFlags.HideInInspector[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideFlags.HideInInspector.html))
                continue;

            yield return c;
        }
    }

    static SearchValue[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchValue.html) FindPropertyValue(UnityEngine.Object obj, string propertyName)
    {
        var property = FindProperty(obj, propertyName, out var so);
        if (property == null)
            return SearchValue.invalid[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchValue-invalid.html);

        var v = SearchValue.ConvertPropertyValue(property);
        so?.Dispose();
        return v;
    }

    static SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) FindProperty(UnityEngine.Object obj, string propertyPath, out SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html) so)
    {
        if (!obj)
        {
            so = null;
            return null;
        }

        so = new SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)(obj);
        var property = so.FindProperty(propertyPath);
        if (property != null)
            return property;

        property = so.FindProperty($"m_{propertyPath}");
        if (property != null)
        {
            return property;
        }

        property = so.GetIterator();
        var next = property.NextVisible(true);
        while (next)
        {
            if (property.name.EndsWith(propertyPath, StringComparison.OrdinalIgnoreCase) ||
                (property.name.Contains(" ") && property.name.Replace(" ", "").EndsWith(propertyPath, StringComparison.OrdinalIgnoreCase)))
            {
                return property;
            }
            next = property.NextVisible(property.hasChildren);
        }

        so?.Dispose();
        so = null;
        return null;
    }

    static ulong GetDocumentKey(GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) go)
    {
        if (!go)
            return ulong.MaxValue;

        if (!go.scene.IsValid() || string.IsNullOrEmpty(go.scene.path))
            return ulong.MaxValue;

        // We return the scene path's hash code as the document key. This is the same key
        // that the SearchMonitor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchMonitor.html) uses to invalidate assets that have been modified.
        return AssetDatabase.AssetPathToGUID[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.AssetPathToGUID.html)(go.scene.path).GetHashCode64();
    }

    static string GetPropertyPath(GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) go, string propertyName)
    {
        var hierarchyPath = SearchUtils.GetHierarchyPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.GetHierarchyPath.html)(go);
        return $"{hierarchyPath}/{propertyName}";
    }

    static ulong GetHashCode64(this string strText)
    {
        if (string.IsNullOrEmpty(strText))
            return 0;
        var s1 = (ulong)strText.Substring(0, strText.Length / 2).GetHashCode();
        var s2 = (ulong)strText.Substring(strText.Length / 2).GetHashCode();
        return s1 << 32 | s2;
    }
}

```

See [SearchMonitorView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchMonitorView.html) for more details.
* * *
