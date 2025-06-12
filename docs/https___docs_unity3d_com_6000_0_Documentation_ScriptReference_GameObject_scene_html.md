* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject-scene.html

#  [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).scene
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html "Go to GameObject Component in the Manual")
[SceneManagement.Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) scene; 
### Description
The Scene that contains the GameObject.
```
//Output the name of the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) this GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) belongs to  
  
using UnityEngine;
using UnityEngine.SceneManagement;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) scene = gameObject.scene;
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(gameObject.name + " is from the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html): " + scene.name);
    }
}

```

* * *
