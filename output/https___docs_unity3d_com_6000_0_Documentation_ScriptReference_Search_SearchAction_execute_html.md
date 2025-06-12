* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchAction-execute.html

#  [SearchAction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchAction.html).execute
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
execute; 
### Description
Executes an action on a set of items.
```
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

```

* * *
