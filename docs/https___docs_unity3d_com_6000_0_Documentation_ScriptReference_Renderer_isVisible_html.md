* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-isVisible.html

#  [Renderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html).isVisible
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
isVisible; 
### Description
Is this renderer visible in any camera? (Read Only)
Note that the object is considered visible when it needs to be rendered in the Scene. For example, it might not actually be visible by any camera but still need to be rendered for shadows. When running in the editor, the Scene view cameras will also cause this value to be true.  
  
Additional resources: [OnBecameVisible](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.OnBecameVisible.html), [OnBecameInvisible](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.OnBecameInvisible.html).
```
//Attach this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) with a Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) component attached
//If the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) is visible to the camera, the message is output to the console  
  
using UnityEngine;  
  
public class IsVisible : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) m_Renderer;
    // Use this for initialization
    void Start()
    {
        m_Renderer = GetComponent<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)>();
    }  
  
    // Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html) is called once per frame
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (m_Renderer.isVisible)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Object is visible");
        }
        else Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Object is no longer visible");
    }
}

```

* * *
