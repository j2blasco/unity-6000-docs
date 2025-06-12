* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimeInitializeLoadType.BeforeSceneLoad.html

#  [RuntimeInitializeLoadType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimeInitializeLoadType.html).BeforeSceneLoad
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
Callback invoked when the first scene's objects are loaded into memory but **before** Awake has been called.
For more info on ordering see [RuntimeInitializeOnLoadMethodAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimeInitializeOnLoadMethodAttribute.html).
```
// Demonstration of the RuntimeInitializeLoadType.BeforeSceneLoad[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimeInitializeLoadType.BeforeSceneLoad.html) attribute to find inactive objects before Awake has been 
// called for the first scene being loaded. Then from these inactive objects we find which ones will be active after Awake is called later.
using UnityEngine;  
  
class MyClass
{
    [RuntimeInitializeOnLoadMethod(RuntimeInitializeLoadType.BeforeSceneLoad[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimeInitializeLoadType.BeforeSceneLoad.html))]
    private static void FirstSceneLoading()
    {
        var components = UnityEngine.Object.FindObjectsByType(typeof(MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)), FindObjectsInactive.Include[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FindObjectsInactive.Include.html), FindObjectsSortMode.None[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FindObjectsSortMode.None.html));
        var willBeActiveAfterSceneLoad = 0;
        foreach (var c in components)
        {
            if (WillBeActiveAfterSceneLoad(((Component[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html))c).gameObject))
                willBeActiveAfterSceneLoad++;
        }
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("BeforeSceneLoad. Will be Active after Awake, count: " + willBeActiveAfterSceneLoad);
    }  
  
    static bool WillBeActiveAfterSceneLoad(GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) gameObject)
    {
        Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) current = gameObject.transform;
        while (current != null)
        {
            if (!current.gameObject.activeSelf)
                return false;  
  
            current = current.parent;
        }  
  
        return true;
    }
}
```

* * *
