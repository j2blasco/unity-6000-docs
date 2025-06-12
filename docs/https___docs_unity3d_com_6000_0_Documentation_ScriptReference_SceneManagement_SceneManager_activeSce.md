* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager-activeSceneChanged.html

#  [SceneManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.html).activeSceneChanged
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
value | Use a subscription of either a UnityAction<[Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html), [Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html)> or a method that takes two [Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) types arguments.  
### Description
Subscribe to this event to get notified when the active Scene has changed.
This script added to [activeSceneChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager-activeSceneChanged.html) takes two hidden arguments. These are the replaced Scene and the next Scene. The arguments are not visible.  
  
In the Editor this event is sent only in Play mode (not in Edit mode). If the event is needed for Edit mode then use [EditorSceneManager.activeSceneChangedInEditMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager-activeSceneChangedInEditMode.html).
```
// SceneManager.activeSceneChanged[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager-activeSceneChanged.html)
//
// This example configures Scene1 to wait for 1.5 seconds before switching to Scene2.
// Scene1 is the replaced Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html); Scene2 is the new loaded Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html).  
  
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;  
  
public class ScriptExample1 : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public delegate void Change();
    public static event Change TimeChanged;  
  
    public void Start()
    {
        SceneManager.activeSceneChanged[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager-activeSceneChanged.html) += ChangedActiveScene;  
  
        // wait 1.5 seconds before change to Scene2
        StartCoroutine(TimeChangedScene());
    }  
  
    IEnumerator TimeChangedScene()
    {
        print(Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html) + " seconds");
        yield return new WaitForSeconds[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForSeconds.html)(1.5f);
        print(Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html) + " seconds");  
  
        // call the event
        TimeChanged();
    }  
  
    private void ChangedActiveScene(Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) current, Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) next)
    {
        string currentName = current.name;  
  
        if (currentName == null)
        {
            // Scene1 has been removed
            currentName = "Replaced";
        }  
  
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Scenes: " + currentName + ", " + next.name);
    }  
  
    void OnEnable()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("OnEnable");
        ScriptExample1.TimeChanged += ChangeScene;
    }  
  
    void ChangeScene()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Changing to Scene2");
        SceneManager.LoadScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.LoadScene.html)("Scene2");  
  
        Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) scene = SceneManager.GetSceneByName[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.GetSceneByName.html)("Scene2");
        SceneManager.SetActiveScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.SetActiveScene.html)(scene);
    }  
  
    void OnDisable()
    {
        ScriptExample1.TimeChanged -= ChangeScene;
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("OnDisable happened for Scene1");
    }
}

```

`ScriptExample2` simply announces that this is the active Scene.
```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;  
  
public class ScriptExample2 : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Script2 starting");
    }
}

```

* * *
