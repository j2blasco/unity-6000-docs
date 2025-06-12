* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchAction.html

# SearchAction
class in UnityEditor.Search
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
Defines an action that can be applied on a SearchItem of a specific search provider type.
```
using System.Collections.Generic;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Search;
using UnityEngine;
using UnityEngine.Rendering;

public class Example_SearchAction
{
    [SearchActionsProvider]
    internal static IEnumerable<SearchAction[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchAction.html)> ActionHandlers()
    {
        return new[]
        {
            new SearchAction[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchAction.html)("asset", "print_dependencies", new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Print Dependencies[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Dependencies.html)", null, "Print all dependencies of an asset."))
            {
                // If this action is the default, double-clicking on an item to execute this action will not close the Search window.
                closeWindowAfterExecution = false,

                // Handler for a single item.
                handler = (item) =>
                {
                    var asset = item.ToObject();
                    if (!asset)
                        return;
                    var path = AssetDatabase.GetAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAssetPath.html)(asset);
                    if (string.IsNullOrEmpty(path))
                        return;

                    var dependencyPaths = AssetDatabase.GetDependencies[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetDependencies.html)(path);
                    foreach (var dependencyPath in dependencyPaths)
                    {
                        var o = AssetDatabase.LoadAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAssetAtPath.html)<UnityEngine.Object>(dependencyPath);
                        if (o != null)
                            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(dependencyPath, o);
                    }
                }
            },

            new SearchAction[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchAction.html)("scene", "toggle_cast_shadows", new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Toggle.html) Cast Shadows", null, "Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Toggle.html) Cast Shadows on a Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html)"))
            {
                // Only enable this action if any of the selected items are actually a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) with a MeshRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshRenderer.html).
                enabled = items =>
                {
                    foreach (var searchItem in items)
                    {
                        var go = searchItem.ToObject<GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)>();
                        if (!go)
                            continue;
                        var mesh = go.GetComponent<MeshRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshRenderer.html)>();
                        if (mesh)
                            return true;
                    }
                    return false;
                },
                // Handler for multiple items: (used when multi selection is used in the Search Window).
                execute = (items) =>
                {
                    foreach (var searchItem in items)
                    {
                        var go = searchItem.ToObject<GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)>();
                        if (!go)
                            continue;
                        var mesh = go.GetComponent<MeshRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshRenderer.html)>();
                        if (!mesh)
                            continue;
                        mesh.shadowCastingMode = mesh.shadowCastingMode == ShadowCastingMode.Off[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowCastingMode.Off.html) ? ShadowCastingMode.On[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowCastingMode.On.html) : ShadowCastingMode.Off[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowCastingMode.Off.html);
                    }
                }
            },
        };
    }
}

```

### Properties
Property | Description  
---|---  
[closeWindowAfterExecution](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchAction-closeWindowAfterExecution.html) | Indicates if the search view should be closed after the action execution.  
[content](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchAction-content.html) | GUI content of the search action used when displayed with an icon.  
[displayName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchAction-displayName.html) | Display name for the search action.  
[enabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchAction-enabled.html) | Callback used to check if the action is enabled based on the current context.  
[execute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchAction-execute.html) | Executes an action on a set of items.  
[handler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchAction-handler.html) | This handler is used for actions that do not support multi-selection.  
[id](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchAction-id.html) | Action unique identifier.  
### Constructors
Constructor | Description  
---|---  
[SearchAction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchAction-ctor.html) | Default constructor to build a search action.  
* * *
