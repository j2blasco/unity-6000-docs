* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObjectUtility.DuplicateGameObject.html

#  [GameObjectUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObjectUtility.html).DuplicateGameObject
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
public static [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) DuplicateGameObject([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) gameObject); 
### Parameters
Parameter | Description  
---|---  
gameObject | The GameObject to be duplicated.  
### Returns
**GameObject** The duplicated GameObject. 
### Description
Duplicates a single GameObject and returns the new GameObject.
Duplicates a GameObject within a Scene. The duplicated GameObject will be on the same level in the hierarchy as the original GameObject, and they will share the same parent. If there are any children or components that belong to the original GameObject, the duplicate will have them as well.  
  
For duplicating more than one GameObject use [DuplicateGameObjects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObjectUtility.DuplicateGameObjects.html). For duplicating Assets use [CopyAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObjectUtility.CopyAsset.html).
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public static class DuplicateGameObjectExample
{
    // Create context menu
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/DuplicateGameObject")]
    public static void DuplicateTest()
    {
        // The original GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) gameObject = new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)();  
  
        // The duplicated GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) duplicatedGameObject = GameObjectUtility.DuplicateGameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObjectUtility.DuplicateGameObject.html)(gameObject);  
  
        // Display[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display.html) the names of the original and duplicated GameObjects in the console
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("The original GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html): " + gameObject.name);
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("The duplicated GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html): " + duplicatedGameObject.name);
    }
}

```

Any errors and warnings from the duplication operation are reported in the log and the console.
* * *
