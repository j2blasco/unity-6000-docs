* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DontDestroyOnLoad.html

#  [Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html).DontDestroyOnLoad
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
public static void DontDestroyOnLoad([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) target); 
### Parameters
Parameter | Description  
---|---  
target | An Object not destroyed on [Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) change.  
### Description
Do not destroy the target Object when loading a new [Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html).
The load of a new [Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) destroys all current [Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) objects. Call [Object.DontDestroyOnLoad](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DontDestroyOnLoad.html) to preserve an Object during scene loading. If the target Object is a component or [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html), Unity also preserves all of the [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html)’s children. [Object.DontDestroyOnLoad](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DontDestroyOnLoad.html) only works for root GameObjects or components on root GameObjects. [Object.DontDestroyOnLoad](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DontDestroyOnLoad.html) does not return a value.  
  
The following example script uses [Object.DontDestroyOnLoad](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DontDestroyOnLoad.html). The example has `scene1` which starts playing background music from an [AudioSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html). The music continues when `scene2` loads. Switch between scenes using a button.  
  
To implement this example, create two new [Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html)s, named `scene1` and `scene2`. Open `scene1` and add the `SceneSwap.cs` script to an empty [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) and name it `Menu`. Next, add `DontDestroy.cs` to a new [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) and name it `BackgroundMusic`. Add an [AudioSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) to `BackgroundMusic` - `Add Component > Audio > Audio Source` - and import an [AudioClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) into your Project. Assign the [AudioClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) to the [AudioSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html)’s [AudioClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) field. Create a tag, call it `music`, and add it to `BackgroundMusic`. Switch to `scene2`. Again add `SceneSwap.cs` to a new [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) and name it `Menu`. Save the Project. Return to `scene1` and run the Project from the `Editor`.  
  
`SceneSwap.cs` script:
```
using UnityEngine;
using UnityEngine.SceneManagement;  
  
// Object.DontDestroyOnLoad[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DontDestroyOnLoad.html) example.
//
// Two scenes call each other. This happens when OnGUI button is clicked.
// scene1 will load scene2; scene2 will load scene1. Both scenes have
// the Menu[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Menu.html) GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) with the SceneSwap.cs script attached.
//
// AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) plays an AudioClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) as the game runs. This is on the
// BackgroundMusic GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) which has a music tag.  The audio
// starts in AudioSource.playOnAwake[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource-playOnAwake.html). The DontDestroy.cs script
// is attached to BackgroundMusic.  
  
public class SceneSwap : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private void OnGUI()
    {
        int xCenter = (Screen.width[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-width.html) / 2);
        int yCenter = (Screen.height[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-height.html) / 2);
        int width = 400;
        int height = 120;  
  
        GUIStyle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) fontSize = new GUIStyle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html)(GUI.skin.GetStyle("button"));
        fontSize.fontSize = 32;  
  
        Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) scene = SceneManager.GetActiveScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.GetActiveScene.html)();  
  
        if (scene.name == "scene1")
        {
            // Show a button to allow scene2 to be switched to.
            if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(xCenter - width / 2, yCenter - height / 2, width, height), "Load second scene", fontSize))
            {
                SceneManager.LoadScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.LoadScene.html)("scene2");
            }
        }
        else
        {
            // Show a button to allow scene1 to be returned to.
            if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(xCenter - width / 2, yCenter - height / 2, width, height), "Return to first scene", fontSize))
            {
                SceneManager.LoadScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.LoadScene.html)("scene1");
            }
        }
    }
}

```

`DontDestroy.cs` script:
```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;  
  
// Object.DontDestroyOnLoad[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DontDestroyOnLoad.html) example.
//
// This script example manages the playing audio. The GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) with the
// "music" tag is the BackgroundMusic GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html). The AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) has the
// audio attached to the AudioClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html).  
  
public class DontDestroy : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Awake()
    {
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)[] objs = GameObject.FindGameObjectsWithTag[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.FindGameObjectsWithTag.html)("music");  
  
        if (objs.Length > 1)
        {
            Destroy(this.gameObject);
        }  
  
        DontDestroyOnLoad(this.gameObject);
    }
}

```

* * *
