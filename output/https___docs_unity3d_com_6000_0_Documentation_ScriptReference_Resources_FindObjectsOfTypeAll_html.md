* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.FindObjectsOfTypeAll.html

#  [Resources](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.html).FindObjectsOfTypeAll
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
public static T[] FindObjectsOfTypeAll(); 
### Description
Returns a list of all objects of Type `T`.
This function can return any type of Unity object that is loaded, including game objects, prefabs, materials, meshes, textures, etc. It will also list internal objects, therefore be careful with the way you handle the returned objects.  
  
Contrary to Object.FindObjectsOfType this function will also list disabled objects.
```
using System.Collections.Generic;
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    List<GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)> GetAllObjectsOnlyInScene()
    {
        List<GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)> objectsInScene = new List<GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)>();  
  
        foreach (GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) go in Resources.FindObjectsOfTypeAll[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.FindObjectsOfTypeAll.html)(typeof(GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html))) as GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)[])
        {
            if (!EditorUtility.IsPersistent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.IsPersistent.html)(go.transform.root.gameObject) && !(go.hideFlags == HideFlags.NotEditable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideFlags.NotEditable.html) || go.hideFlags == HideFlags.HideAndDontSave[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideFlags.HideAndDontSave.html)))
                objectsInScene.Add(go);
        }  
  
        return objectsInScene;
    }
}

```

This will return all GameObjects in the scene, in List<GameObject> format.
```
using System.Collections.Generic;
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    List<GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)> GetNonSceneObjects()
    {
        List<GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)> objectsInScene = new List<GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)>();  
  
        foreach (GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) go in Resources.FindObjectsOfTypeAll[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.FindObjectsOfTypeAll.html)(typeof(GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html))) as GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)[])
        {
            if (EditorUtility.IsPersistent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.IsPersistent.html)(go.transform.root.gameObject) && !(go.hideFlags == HideFlags.NotEditable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideFlags.NotEditable.html) || go.hideFlags == HideFlags.HideAndDontSave[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideFlags.HideAndDontSave.html)))
                objectsInScene.Add(go);
        }  
  
        return objectsInScene;
    }
}

```

This will return all GameObjects that are also Prefabs in the Resources folder.
* * *
## Declaration
public static Object[] FindObjectsOfTypeAll(Type type); 
### Description
Returns a list of all objects of Type `type`.
This function using non-generic types can return any type of Unity object that is loaded, including game objects, prefabs, materials, meshes, textures, etc. It will also list internal stuff, therefore be careful the way you handle the returned objects. Contrary to [Object.FindObjectsOfType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindObjectsOfType.html) this function will also list disabled objects.  
  
Note: that this function is very slow and is not recommended to be used every frame.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using System.Collections.Generic;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    List<UnityEngine.Object> GetSceneObjectsNonGeneric()
    {
        List<UnityEngine.Object> objectsInScene = new List<UnityEngine.Object>();  
  
        foreach (UnityEngine.Object go in Resources.FindObjectsOfTypeAll[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.FindObjectsOfTypeAll.html)(typeof(UnityEngine.Object)) as UnityEngine.Object[])
        {
            GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) cGO = go as GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html);
            if (cGO != null && !EditorUtility.IsPersistent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.IsPersistent.html)(cGO.transform.root.gameObject) && !(go.hideFlags == HideFlags.NotEditable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideFlags.NotEditable.html) || go.hideFlags == HideFlags.HideAndDontSave[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideFlags.HideAndDontSave.html)))
                objectsInScene.Add(go);
        }  
  
        return objectsInScene;
    }
}

```

Find all gameObjects in scene using non-generic methods.
* * *
