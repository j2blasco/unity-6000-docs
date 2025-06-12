* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision-articulationBody.html

#  [Collision](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision.html).articulationBody
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
[ArticulationBody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.html) articulationBody; 
### Description
The [ArticulationBody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.html) of the collider that your GameObject collides with (Read Only).
This returns the [ArticulationBody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.html) of the collider that your GameObject collides with. If the collider doesn't have an articulation body attached, this returns `null`.
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Make all articulation bodies that your GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) hits fly upwards
    void OnCollisionStay(Collision[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision.html) collision)
    {
        // Check if the collider your GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) hits has an articulation body
        // Then apply the force
        if (collision.articulationBody)
        {
            collision.articulationBody.AddForce(Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html) * 15);
        }
    }
}

```

* * *
