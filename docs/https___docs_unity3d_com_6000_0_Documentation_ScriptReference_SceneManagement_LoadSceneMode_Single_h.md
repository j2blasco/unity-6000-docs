* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.LoadSceneMode.Single.html

#  [LoadSceneMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.LoadSceneMode.html).Single
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
Closes all current loaded Scenes and loads a Scene.
Additional resources: [SceneManager.LoadScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.LoadScene.html).
```
using UnityEngine;
using UnityEngine.SceneManagement;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnGUI()
    {
        //This displays a Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) on the screen at position (20,30), width 150 and height 50. The button’s text reads the last parameter. Press this for the SceneManager[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.html) to load the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html).
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(20, 30, 150, 30), "Other Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) Single"))
        {
            //The SceneManager[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.html) loads your new Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) as a single Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) (not overlapping). This is Single mode.
            SceneManager.LoadScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.LoadScene.html)("YourScene", LoadSceneMode.Single[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.LoadSceneMode.Single.html));
        }  
  
        //Whereas pressing this Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) loads the Additive Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html).
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(20, 60, 150, 30), "Other Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) Additive"))
        {
            //SceneManager[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.html) loads your new Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) as an extra Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) (overlapping the other). This is Additive mode.
            SceneManager.LoadScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.LoadScene.html)("YourScene", LoadSceneMode.Additive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.LoadSceneMode.Additive.html));
        }
    }
}

```

* * *
