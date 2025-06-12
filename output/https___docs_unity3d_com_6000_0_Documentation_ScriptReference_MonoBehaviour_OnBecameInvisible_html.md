* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnBecameInvisible.html

#  [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html).OnBecameInvisible()
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MonoBehaviour.html "Go to MonoBehaviour Component in the Manual")
### Description
OnBecameInvisible is called when the renderer is no longer visible by any camera.
This message is sent to all scripts attached to the renderer. [OnBecameVisible](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnBecameVisible.html) and [OnBecameInvisible](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnBecameInvisible.html) is useful to avoid computations that are only necessary when the object is visible.
```
// Disables the behaviour when it is invisible  
  
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnBecameInvisible()
    {
        enabled = false;
    }
}

```

OnBecameInvisible can be a co-routine, simply use the yield statement in the function. When running in the editor, Scene view cameras will also cause this function to be called.
* * *
