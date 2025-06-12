* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.FetchGameObjects.html

#  [SearchUtils](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.html).FetchGameObjects
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
public static GameObject[] FetchGameObjects([SceneManagement.Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) scene); 
## Declaration
public static IEnumerable<GameObject> FetchGameObjects(); 
### Parameters
Parameter | Description  
---|---  
scene | Scene to get objects from.  
### Returns
**GameObject[]** The array of game objects in the scene. 
### Description
Utility function to fetch all the game objects in a particular scene.
Use `SearchUtils.FetchGameObjects` to create a custom [SearchProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html) that is able to access current scene objects.
```
static void OnEnable()
{
    s_GameObjects = SearchUtils.FetchGameObjects[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.FetchGameObjects.html)().ToArray();
    s_QueryEngine = new QueryEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html)<GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)>();

    // Id supports all operators
    s_QueryEngine.AddFilter("id", go => go.GetInstanceID());
    // Name supports only :, = and !=
    s_QueryEngine.AddFilter("n", go => go.name, new[] {":", "=", "!="});

    // Add distance filtering. Does not support :.
    s_QueryEngine.AddFilter("dist", DistanceHandler, DistanceParamHandler, new[] {"=", "!=", "<", ">", "<=", ">="});
}

```

```
static IEnumerator SearchItems(SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) context, SearchProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html) provider)
{
    var query = s_QueryEngine.ParseQuery(context.searchQuery);
    if (!query.valid)
        yield break;

    var filteredObjects = query.Apply(s_GameObjects);
    foreach (var filteredObject in filteredObjects)
    {
        yield return provider.CreateItem(filteredObject.GetInstanceID().ToString(), null, null, null, filteredObject.GetInstanceID());
    }
}

```

* * *
