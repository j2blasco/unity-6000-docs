* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-attachedRigidbody.html

#  [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html).attachedRigidbody
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
The [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) attached to the [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html).
[Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) are automatically attached to a [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) on the same [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) as the [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) or if none is present then on a [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) on the nearest parent [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html). The property will be null if no [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) is attached. In this case, the [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) is attached to a hidden body known as the ground body that lives at the world origin as is set to be [RigidbodyType2D.Static](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyType2D.Static.html). No reference to this hidden body is available however.  
  
Additional resources: [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html), [RigidbodyType2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyType2D.html).
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) force = Vector2.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2-up.html);  
  
    void Start()
    {
        // Apply a force to the rigidbody attached to the collider.
        GetComponent<Collider2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html)>().attachedRigidbody.AddForce(force);
    }
}

```

* * *
