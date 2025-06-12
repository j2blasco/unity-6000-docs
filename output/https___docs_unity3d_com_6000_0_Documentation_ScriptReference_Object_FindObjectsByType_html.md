* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindObjectsByType.html

#  [Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html).FindObjectsByType
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
public static Object[] FindObjectsByType(Type type, [FindObjectsSortMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FindObjectsSortMode.html) sortMode); 
## Declaration
public static Object[] FindObjectsByType(Type type, [FindObjectsInactive](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FindObjectsInactive.html) findObjectsInactive, [FindObjectsSortMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FindObjectsSortMode.html) sortMode); 
## Declaration
public static T[] FindObjectsByType([FindObjectsSortMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FindObjectsSortMode.html) sortMode); 
## Declaration
public static T[] FindObjectsByType([FindObjectsInactive](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FindObjectsInactive.html) findObjectsInactive, [FindObjectsSortMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FindObjectsSortMode.html) sortMode); 
### Parameters
Parameter | Description  
---|---  
type | The type of object to find.  
findObjectsInactive | Whether to include components attached to inactive GameObjects. If you don't specify this parameter, this function doesn't include inactive objects in the results.  
sortMode | Whether and how to sort the returned array. Not sorting the array makes this function run significantly faster.  
### Returns
**Object[]** The array of objects found matching the type specified. 
### Description
Retrieves a list of all loaded objects of Type `type`.
This doesn't return Assets (for example meshes, textures, or prefabs). It also doesn't return objects that have [HideFlags.DontSave](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideFlags.DontSave.html) set. Use [Resources.FindObjectsOfTypeAll](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.FindObjectsOfTypeAll.html) to avoid these limitations.  
  
In Editor, this searches the Scene view by default. If you want to find an object in the Prefab stage, see the [StageUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.StageUtility.html) APIs.
```
using UnityEngine;  
  
// Ten GameObjects are created and have TextMesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextMesh.html) and
// CanvasRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanvasRenderer.html) components added.
// When the game runs press the Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.html) key to display the
// number of TextMesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextMesh.html) and CanvasRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanvasRenderer.html) components.  
  
public class ScriptExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private const int count = 10;  
  
    void Start()
    {
        var gameObjects = new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)[count];
        var expectedTextMeshObjects = new TextMesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextMesh.html)[count];
        var expectedCanvasObjects = new CanvasRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanvasRenderer.html)[count];  
  
        for (var i = 0; i < count; ++i)
        {
            gameObjects[i] = new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)();
            expectedTextMeshObjects[i] = gameObjects[i].AddComponent<TextMesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextMesh.html)>();
            expectedCanvasObjects[i] = gameObjects[i].AddComponent<CanvasRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanvasRenderer.html)>();
        }
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (Input.GetKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyDown.html)(KeyCode.Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Space.html)))
        {
            var foundCanvasObjects = FindObjectsByType<CanvasRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanvasRenderer.html)>(FindObjectsSortMode.None[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FindObjectsSortMode.None.html));
            var foundTextMeshObjects = FindObjectsByType(typeof(TextMesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextMesh.html)), FindObjectsSortMode.None[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FindObjectsSortMode.None.html));
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(foundCanvasObjects + " : " + foundCanvasObjects.Length);
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(foundTextMeshObjects + " : " + foundTextMeshObjects.Length);
        }
    }
}

```

Additional resources: [Object.FindFirstObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindFirstObjectByType.html), [Object.FindAnyObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindAnyObjectByType.html).
* * *
