* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-tag.html

#  [Component](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html).tag
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
tag; 
### Description
The tag of this game object.
A tag can be used to identify a game object. Tags must be declared in the [Tags and Layers manager](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TagManager.html) before using them.  
  
**Note:** You should not set a tag from the [Awake()](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.Awake.html) or [OnValidate()](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnValidate.html) method. This is because the order in which components become awake is not deterministic, and therefore can result in unexpected behaviour such as the tag being overwritten when it is awoken. If you try this, Unity will generate a warning reading "SendMessage cannot be called during Awake, CheckConsistency, or OnValidate".
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Prints the tag that this transform has
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) Tag is: " + gameObject.tag);
    }
}

```

* * *
