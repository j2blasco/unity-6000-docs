* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.OnBecameInvisible.html

#  [Renderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html).OnBecameInvisible()
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
`OnBecameInvisible` is called when the object is no longer visible by any camera.
This message is sent to all scripts attached to the renderer. `OnBecameVisible` and `OnBecameInvisible` are useful to avoid computations that are only necessary when the object is visible.
```
using UnityEngine;  
  
public class BecomeVisible : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Disable this script when the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) moves out of the camera's view
    void OnBecameInvisible()
    {
        enabled = false;
    }  
  
    // Enable this script when the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) moves into the camera's view
    void OnBecameVisible()
    {
        enabled = true;
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Script is enabled");
    }
}

```

Note that object is considered visible when it needs to be rendered in the Scene. It might not be actually visible by any camera, but still need to be rendered for shadows for example. Also, when running in the editor, the Scene view cameras will also cause this function to be called.  
  
Additional resources: [OnBecameVisible](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.OnBecameVisible.html), [isVisible](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-isVisible.html).
* * *
