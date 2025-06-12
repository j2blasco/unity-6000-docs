* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision-rigidbody.html

#  [Collision](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision.html).rigidbody
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
[Rigidbody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) rigidbody; 
### Description
The [Rigidbody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) we hit (Read Only). This is `null` if the object we hit is a collider with no rigidbody attached.
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Make all rigidbodies we touch fly upwards
    void OnCollisionStay(Collision[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision.html) collision)
    {
        // Check if the collider we hit has a rigidbody
        // Then apply the force
        if (collision.rigidbody)
        {
            collision.rigidbody.AddForce(Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html) * 15);
        }
    }
}

```

* * *
