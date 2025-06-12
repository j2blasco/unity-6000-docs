* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene-buildIndex.html

#  [Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html).buildIndex
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
buildIndex; 
### Description
Return the index of the Scene in the Build Settings.
[Scene.buildIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene-buildIndex.html) varies from zero to the number of [Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html)s in the `Build Settings` minus one. This is because indexes start at zero, so the first [Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) is at position zero in the [buildIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene-buildIndex.html). For example, five [Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html)s in the `Build Settings` have an index from zero to four.  
  
Unity ignores any numbers in a `Scene` name. For example, if you add a `Scene` called `scene15` to a list of five [Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html)s in the `Build Settings`, Unity gives it a [buildIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene-buildIndex.html) of 5.  
  
A `Scene` that is not added to the `Scenes in Build` window returns a [buildIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene-buildIndex.html) one more than the highest in the list. For example, if you don’t add a `Scene` to a `Scenes in Build` window that already has 6 Scenes in it, then [Scene.buildIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene-buildIndex.html) returns 6 as its index .  
  
If the `Scene` is loaded through an `AssetBundle`, [Scene.buildIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene-buildIndex.html) returns -1.
```
using UnityEngine;
using UnityEngine.SceneManagement;  
  
// Show the buildIndex for the current script.
//
// The Build Settings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingAccelerationStructure.Settings.html) window shows 5 added Scenes.  These have buildIndex values from
// 0 to 4. Each Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) has a version of this script applied.
//
// In the Project, create 5 Scenes called scene1, scene2, scene3, scene4 and scene5.
// In each Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) add an empty GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) and attach this script to it.
//
// Each Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) randomly switches to a different Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) when the button is clicked.  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) scene;  
  
    void Start()
    {
        scene = SceneManager.GetActiveScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.GetActiveScene.html)();
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Active Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) name is: " + scene.name + "\nActive Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) index: " + scene.buildIndex);
    }  
  
    void OnGUI()
    {
        GUI.skin.button.fontSize = 20;  
  
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 80, 180, 60), "Change from scene " + scene.buildIndex))
        {
            int nextSceneIndex = Random.Range[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.Range.html)(0, 4);
            SceneManager.LoadScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.LoadScene.html)(nextSceneIndex, LoadSceneMode.Single[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.LoadSceneMode.Single.html));
        }
    }
}

```

* * *
