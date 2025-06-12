* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D-attachedRigidbody.html

#  [Joint2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D.html).attachedRigidbody
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
[Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) attachedRigidbody; 
### Description
The [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) attached to the [Joint2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D.html).
[Joint2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D.html) are automatically attached to a [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) on the same [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) as the [Joint2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D.html).  
  
Additional resources: [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html).
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) force = Vector2.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2-up.html);  
  
    void Start()
    {
        // Apply a force to the rigidbody attached to the joint.
        GetComponent<Joint2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D.html)>().attachedRigidbody.AddForce(force);
    }
}

```

* * *
