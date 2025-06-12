* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider-attachedArticulationBody.html

#  [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html).attachedArticulationBody
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
[ArticulationBody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.html) attachedArticulationBody; 
### Description
The articulation body the collider is attached to.
Returns null if the collider is attached to no articulation body.  
  
Colliders are automatically connected to the articulation body attached to the same game object or attached to any parent game object.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Lift the articulation body attached to the collider.
        GetComponent<Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html)>().attachedArticulationBody.AddForce(Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html));
    }
}

```

* * *
