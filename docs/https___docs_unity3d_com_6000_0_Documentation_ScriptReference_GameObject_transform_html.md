* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject-transform.html

#  [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).transform
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
[Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) transform; 
### Description
The Transform attached to the GameObject (Read Only).
Every GameObject has a [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) component attached to it on creation, which cannot be removed.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        gameObject.transform.Translate(1, 1, 1);
    }
}

```

* * *
