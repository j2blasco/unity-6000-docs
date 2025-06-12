* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager-sceneLoaded.html

#  [SceneManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.html).sceneLoaded
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
value | A method with the signature MyMethod([Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html), [LoadSceneMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.LoadSceneMode.html)).  
### Description
Assign a custom callback to this event to get notifications when a Scene has loaded.
Create a custom callback method to receive the notification and assign it to the `SceneManager.sceneLoaded` event. The callback must have the required signature, taking a [Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) and a [LoadSceneMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.LoadSceneMode.html) as input parameters.  
  
The code example below defines a custom calllback method called `OnSceneLoaded` with the required signature. It assigns `OnSceneLoaded` to `SceneManager.sceneLoaded` in the `OnEnable` callback and unassigns it in the `OnDisable` callback.  
  
The code example and comment annotations demonstrate the execution order of the callbacks. Unity raises the `SceneManager.sceneLoaded` event and invokes the associated callback after `OnEnable` but before `Start`.  
  
Additional resources: [Details of disabling domain and scene reload](https://docs.unity3d.com/6000.0/Documentation/Manual/configurable-enter-play-mode-details.html)
```
using UnityEngine;
using UnityEngine.SceneManagement;  
  
public class ExampleCode : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // called first
    void Awake()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Awake");
    }  
  
    // called second
    void OnEnable()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("OnEnable called");
        SceneManager.sceneLoaded[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager-sceneLoaded.html) += OnSceneLoaded;
    }  
  
    // called third
    void OnSceneLoaded(Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) scene, LoadSceneMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.LoadSceneMode.html) mode)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("OnSceneLoaded: " + scene.name);
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(mode);
    }  
  
    // called fourth
    void Start()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Start");
    }  
  
    // called when the game is terminated
    void OnDisable()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("OnDisable");
        SceneManager.sceneLoaded[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager-sceneLoaded.html) -= OnSceneLoaded;
    }
}

```

* * *
