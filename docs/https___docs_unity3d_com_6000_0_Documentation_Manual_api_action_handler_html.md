* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/api-action-handler.html

  * [The Unity Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-editor.html)
  * [Unity Search](https://docs.unity3d.com/6000.0/Documentation/Manual/search-overview.html)
  * [Creating a custom Search Provider](https://docs.unity3d.com/6000.0/Documentation/Manual/api.html)
  * Registering an Action Handler


[](https://docs.unity3d.com/6000.0/Documentation/Manual/api-searching.html)
Performing a search
[](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
Working in Unity
# Registering an Action Handler
You can register actions for a Search Provider. Users can access registered actions via the **More Options** (**⋮**) icon in the search results.
> **Note:** Registering an action handler and registering a Search Provider are different processes. You can register new action handlers for existing Search Providers.
To register an action, you create a function tagged with the [`SearchActionsProvider`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchActionsProviderAttribute.html) attribute. This function must return an `IEnumerable<SearchAction>`.
The following example shows how to register actions for the Asset Search Provider.
```
[SearchActionsProvider]
internal static IEnumerable<SearchAction> ActionHandlers()
{
    return new[]
    {
        new SearchAction("asset", "select", Icons.@goto, "Select asset...")
        {
            handler = (item, context) =>
            {
                var asset = AssetDatabase.LoadAssetAtPath<Object>(item.id);
                if (asset != null)
                {
                    Selection.activeObject = asset;
                    EditorGUIUtility.PingObject(asset);
                    EditorWindow.FocusWindowIfItsOpen(
                        Utils.GetProjectBrowserWindowType());
                }
            }
        },
        new SearchAction("asset", "open", SearchIcon.open, "Open asset... (Alt+Enter)")
        {
            handler = (item, context) =>
            {
                var asset = AssetDatabase.LoadAssetAtPath<Object>(item.id);
                if (asset != null)
                    AssetDatabase.OpenAsset(asset);
            }
        },
        new SearchAction("asset", "reveal", SearchIcon.folder, "Show in Explorer")
        {
            handler = (item, context) =>
            {
                EditorUtility.RevealInFinder(item.id);
            }
        }
    };
}

```

## Search actions
The [`SearchAction`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchAction.html) class describes an action and provides a handler to execute the action on a specific `SearchItem`.
```
public class SearchAction
{
    public SearchAction(string providerType, string name,
                        Texture2D icon = null,
                        string tooltip = null);
    public ActionHandler handler;
    public EnabledHandler isEnabled;
}

```

The `providerType` is the unique ID of the provider that you register the action for.
The `ActionHandler` has the following signature:
```
// item: item that needs the action to be executed.
// context: search context of the SearchTool when the item is executed.
public delegate void ActionHandler(SearchItem item, SearchContext context);

```

You can set up an action with the `isEnabled` predicate, which determines whether an action is available for a specific item.
## Contextual search actions
To provide contextual (right-click) actions for specific types of items in search results, register an action named `context` for the Search Provider.
The following example is from the Asset Search Provider:
```
new SearchAction(type, "context", null, "Context")
{
    handler = (item, context) =>
    {
        var asset = AssetDatabase.LoadAssetAtPath<Object>(item.id);
        if (asset != null)
        {
            Selection.activeObject = asset;
            EditorUtility.DisplayPopupMenu(
                QuickSearchTool.ContextualActionPosition,
                "Assets/", null);
        }
    }
}

```

* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/api-searching.html)
Performing a search
[](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
Working in Unity
