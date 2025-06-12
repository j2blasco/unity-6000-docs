* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.IsChildOf.html

#  [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html).IsChildOf
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Transform.html "Go to Transform Component in the Manual")
## Declaration
public bool IsChildOf([Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) parent); 
### Description
Is this transform a child of `parent`?
Returns a boolean value that indicates whether the transform is a child of a given transform. true if this transform is a child, deep child (child of a child) or identical to this transform, otherwise false.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnTriggerEnter(Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) col)
    {
        // Ignore trigger events if between this collider and colliders in children
        // Eg. when you have a complex character with multiple triggers colliders.
        if (col.transform.IsChildOf(transform))
        {
            return;
        }  
  
        print("Do something here");
    }
}

```

* * *
