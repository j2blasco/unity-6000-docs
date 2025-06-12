* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager-sceneUnloaded.html

#  [SceneManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.html).sceneUnloaded
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
### Parameters
Parameter | Description  
---|---  
value | Use a subscription of either a UnityAction<[Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html)> or a method that takes a [Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) type argument.  
### Description
Add a delegate to this to get notifications when a Scene has unloaded.
Rather than being called directly this script code shows use of a delegate. This means the [sceneUnloaded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager-sceneUnloaded.html) value is added into a list of delegates.  
  
In the script example below a method call is shown. Specifically a function called OnSceneUnloaded is added to sceneUnloaded. SceneUnloaded is called when the Scene it is associated with is closed. At this point SceneUnloaded should be removed from the [sceneUnloaded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager-sceneUnloaded.html) list.
```
using UnityEngine;
using UnityEngine.SceneManagement;  
  
public class SceneLoaded1 : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public void Start()
    {
        SceneManager.sceneUnloaded[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager-sceneUnloaded.html) += OnSceneUnloaded;
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Start: SceneLoaded1");
    }  
  
    private void OnSceneUnloaded(Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) current)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("OnSceneUnloaded: " + current);
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (Input.GetKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKey.html)("space"))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Quitting Scene1");
            ChangeScene();
        }
    }  
  
    void ChangeScene()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Changing to Scene2");  
  
        SceneManager.LoadScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.LoadScene.html)("Scene2");
    }  
  
    void OnDestroy()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("OnDestroy");
    }
}

```

`SceneLoaded2` simply announces that this is the active Scene.
```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;  
  
public class SceneLoaded2 : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public void Start()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("SceneLoaded2");
    }
}

```

* * *
