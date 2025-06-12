* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics-defaultSolverVelocityIterations.html

#  [Physics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.html).defaultSolverVelocityIterations
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
defaultSolverVelocityIterations; 
### Description
The defaultSolverVelocityIterations affects how accurately the Rigidbody joints and collision contacts are resolved. (default 1). Must be positive.
Increasing this value will result in higher accuracy of the resulting exit velocity after a Rigidbody bounce. If you are experiencing issues with jointed Rigidbodies or Ragdolls moving too much after collisions you can try to increase this value.  
  
This value is usually changed in `Edit->Project Settings->Physics` inspector instead of from scripts.  
  
**Note:** Changing the defaultSolverVelocityIterations does not affect already created Rigidbodies. To change an existing Rigidbody please use [Rigidbody.solverVelocityIterations](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-solverVelocityIterations.html).  
  
Additional resources: [Physics.defaultSolverIterations](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics-defaultSolverIterations.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Physics.defaultSolverVelocityIterations[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics-defaultSolverVelocityIterations.html) = 10;
    }
}

```

* * *
