* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindObjectsOfType.html

**Method group is Obsolete**   

#  [Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html).FindObjectsOfType
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
**Obsolete** Object.FindObjectsOfType has been deprecated. Use Object.FindObjectsByType instead which lets you decide whether you need the results sorted or not. FindObjectsOfType sorts the results by InstanceID, but if you do not need this using FindObjectSortMode.None is considerably faster.
## Declaration
public static Object[] FindObjectsOfType(Type type); 
**Obsolete** Object.FindObjectsOfType has been deprecated. Use Object.FindObjectsByType instead which lets you decide whether you need the results sorted or not. FindObjectsOfType sorts the results by InstanceID but if you do not need this using FindObjectSortMode.None is considerably faster.
## Declaration
public static Object[] FindObjectsOfType(Type type, bool includeInactive); 
**Obsolete** Object.FindObjectsOfType has been deprecated. Use Object.FindObjectsByType instead which lets you decide whether you need the results sorted or not. FindObjectsOfType sorts the results by InstanceID but if you do not need this using FindObjectSortMode.None is considerably faster.
## Declaration
public static T[] FindObjectsOfType(bool includeInactive); 
**Obsolete** Object.FindObjectsOfType has been deprecated. Use Object.FindObjectsByType instead which lets you decide whether you need the results sorted or not. FindObjectsOfType sorts the results by InstanceID but if you do not need this using FindObjectSortMode.None is considerably faster.
## Declaration
public static T[] FindObjectsOfType(); 
### Parameters
Parameter | Description  
---|---  
type | The type of object to find.  
includeInactive | If true, components attached to inactive GameObjects are also included.  
### Returns
**Object[]** The array of objects found matching the type specified. 
### Description
Gets a list of all loaded objects of Type `type`.
This does not return assets (such as meshes, textures or prefabs), or objects with [HideFlags.DontSave](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideFlags.DontSave.html) set. Objects attached to inactive GameObjects are only included if `inactiveObjects` is set to true. Use [Resources.FindObjectsOfTypeAll](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.FindObjectsOfTypeAll.html) to avoid these limitations.  
  
In Editor, this searches the Scene view by default. If you want to find an object in the Prefab stage, see the [StageUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.StageUtility.html) APIs.  
  
**Note** : This function is very slow. It is not recommended to use this function every frame. In most cases you can use the singleton pattern instead.  
  
**Obsolete** : This function is obsolete, use [Object.FindObjectsByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindObjectsByType.html) instead. This replacement allows you to specify whether to sort the resulting array. FindObjectsOfType() always sorts by InstanceID, so calling FindObjectsByType(FindObjectsSortMode.InstanceID) produces identical results. If you specify not to sort the array, the function runs significantly faster, however, the order of the results can change between calls.
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
            var foundCanvasObjects = FindObjectsOfType<CanvasRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanvasRenderer.html)>();
            var foundTextMeshObjects = FindObjectsOfType(typeof(TextMesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextMesh.html)));
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(foundCanvasObjects + " : " + foundCanvasObjects.Length);
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(foundTextMeshObjects + " : " + foundTextMeshObjects.Length);
        }
    }
}

```

Additional resources: [Object.FindObjectsByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindObjectsByType.html).
* * *
