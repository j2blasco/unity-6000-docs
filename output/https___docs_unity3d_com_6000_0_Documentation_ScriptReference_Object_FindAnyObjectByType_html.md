* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindAnyObjectByType.html

#  [Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html).FindAnyObjectByType
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Object.html "Go to Object Component in the Manual")
## Declaration
public static T FindAnyObjectByType(); 
## Declaration
public static T FindAnyObjectByType([FindObjectsInactive](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FindObjectsInactive.html) findObjectsInactive); 
## Declaration
public static Object FindAnyObjectByType(Type type); 
## Declaration
public static Object FindAnyObjectByType(Type type, [FindObjectsInactive](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FindObjectsInactive.html) findObjectsInactive); 
### Parameters
Parameter | Description  
---|---  
type | The type of object to find.  
findObjectsInactive | Whether to include components attached to inactive GameObjects. If you don't specify this parameter, this function doesn't include inactive objects in the results.  
### Returns
**T** Returns an arbitrary active loaded object that matches the specified type. If no object matches the specified type, returns null. 
### Description
Retrieves any active loaded object of Type `type`.
`Object.FindAnyObjectByType` doesn't return Assets (for example meshes, textures, or prefabs), or inactive objects. It also doesn't return objects that have [HideFlags.DontSave](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideFlags.DontSave.html) set.  
  
**Note** : The object that this function returns isn't guaranteed to be the same between calls, but it is always of the specified type. This function is faster than [Object.FindFirstObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindFirstObjectByType.html) if you don't need a specific object instance.  
  
See Also: [Object.FindFirstObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindFirstObjectByType.html), [Object.FindObjectsByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindObjectsByType.html).
```
using UnityEngine;
using System.Collections;  
  
// Search for any object of Types TextMesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextMesh.html) and CanvasRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanvasRenderer.html),
// if found print the names, else print a message
// that says that it was not found.
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        TextMesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextMesh.html) texture = (TextMesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextMesh.html))FindAnyObjectByType(typeof(TextMesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextMesh.html)));
        if (texture)
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("TextMesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextMesh.html) object found: " + texture.name);
        else
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("No TextMesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextMesh.html) object could be found");  
  
        CanvasRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanvasRenderer.html) canvas = FindAnyObjectByType<CanvasRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanvasRenderer.html)>();
        if (canvas)
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("CanvasRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanvasRenderer.html) object found: " + canvas.name);
        else
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("No CanvasRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanvasRenderer.html) object could be found");
    }
}

```

* * *
