* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision-body.html

#  [Collision](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision.html).body
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
[Component](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html) body; 
### Description
The [Rigidbody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) or [ArticulationBody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.html) of the collider that your [Component](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html) collides with (Read Only).
This returns the [Rigidbody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) or [ArticulationBody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.html) of the collider that your [Component](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html) collides with. If the collider doesn't have a rigid or articulation body attached, this returns `null`.
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Print out which type of Component[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html) is attached to the collider we hit
    void OnCollisionStay(Collision[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision.html) collision)
    {
        // Check if the collider your GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) hits has a rigidbody
        if (collision.body as Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Has Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html).");
        }  
  
        // Check if the collider your GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) hits has an articulation body
        if (collision.body as ArticulationBody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.html))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Has ArticulationBody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.html).");
        }
    }
}

```

* * *
