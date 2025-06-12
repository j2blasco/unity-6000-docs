* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint-massScale.html

#  [Joint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint.html).massScale
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
massScale; 
### Description
The scale to apply to the inverse mass and inertia tensor of the body prior to solving the constraints.
Scale mass and the inertia tensor to make the joints solver converge faster, thus resulting in less stretch of the limbs of a typical ragdoll. Most useful in conjunction with [Joint.connectedMassScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint-connectedMassScale.html).  
  
For example, if you have two objects in a ragdoll of masses 1 and 10, the physics engine will typically resolve the joint by changing the velocity of the lighter body much more than the heavier one. Applying a mass scale of 10 to the first body makes solver change the velocity of both bodies by an equal amount. Applying mass scales such that the joint sees similar effective masses and inertias makes the solver converge faster, which can make individual joints seem less rubbery or separated, and sets of jointed bodies appear less twitchy  
  
Note that scaling mass and inertia is fundamentally nonphysical and momentum won't be conserved.  
  
The following script is useful to adjust the mass and inertia scaling in order to get the same corrective velocity out of the solver. Attach it to the ragdoll's root, or to a limb that is over-stretched during the gameplay and it will find all joints down in the transform hierarchy below itself and adjust the mass scale.
```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;  
  
public class NormalizeMass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private void Apply(Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) root)
    {
        var j = root.GetComponent<Joint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint.html)>();  
  
        // Apply the inertia scaling if possible
        if (j && j.connectedBody)
        {
            // Make sure that both of the connected bodies will be moved by the solver with equal speed
            j.massScale = j.connectedBody.mass / root.GetComponent<Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)>().mass;
            j.connectedMassScale = 1f;
        }  
  
        // Continue for all children...
        for (int childId = 0; childId < root.childCount; ++childId)
        {
            Apply(root.GetChild(childId));
        }
    }  
  
    public void Start()
    {
        Apply(this.transform);
    }
}

```

* * *
