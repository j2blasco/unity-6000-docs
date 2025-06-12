* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.FindAllInstancesOfPrefab.html

#  [PrefabUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.html).FindAllInstancesOfPrefab
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
public static GameObject[] FindAllInstancesOfPrefab([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) prefabRoot); 
## Declaration
public static GameObject[] FindAllInstancesOfPrefab([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) prefabRoot, [SceneManagement.Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) scene); 
### Parameters
Parameter | Description  
---|---  
prefabRoot | The root GameObject of a Prefab asset.  
scene | The scene to search for Prefab instances. The scene you specify must be valid and loaded.  
### Returns
**GameObject[]** The root GameObjects for all instances of the Prefab asset with root `prefabRoot`. 
### Description
Retrieves the root GameObjects for all instances of the Prefab asset with root `prefabRoot` found in all currently loaded scenes. If `prefabRoot` is not a valid Prefab asset root GameObject, an `ArgumentException` is thrown.
FindAllInstancesOfPrefab will not return nested Prefab instances.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using UnityEngine.SceneManagement;
using NUnit.Framework;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) prefabAssetRoot;
    private void Start()
    {
        var expectedInstance = (GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html))PrefabUtility.InstantiatePrefab[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.InstantiatePrefab.html)(prefabAssetRoot);
        var instances = PrefabUtility.FindAllInstancesOfPrefab[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.FindAllInstancesOfPrefab.html)(prefabAssetRoot);
        Assert.AreEqual[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.AreEqual.html)(1, instances.Length);
        Assert.AreEqual[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.AreEqual.html)(expectedInstance, instances[0]);
    }
}

```

* * *
### Description
Returns the root GameObjects for all instances of the Prefab asset with root `prefabRoot` found in `scene`. If `prefabRoot` is not a valid Prefab asset root GameObject, or `scene` is not valid and loaded, `ArgumentException` is thrown.
FindAllInstancesOfPrefab will not return nested Prefab instances.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using UnityEngine.SceneManagement;
using NUnit.Framework;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) prefabAssetRoot;
    private void Start()
    {
        var expectedInstance = (GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html))PrefabUtility.InstantiatePrefab[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.InstantiatePrefab.html)(prefabAssetRoot);
        var instances = PrefabUtility.FindAllInstancesOfPrefab[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.FindAllInstancesOfPrefab.html)(prefabAssetRoot, SceneManager.GetActiveScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.GetActiveScene.html)());
        Assert.AreEqual[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.AreEqual.html)(1, instances.Length);
        Assert.AreEqual[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.AreEqual.html)(expectedInstance, instances[0]);
    }
}

```

* * *
