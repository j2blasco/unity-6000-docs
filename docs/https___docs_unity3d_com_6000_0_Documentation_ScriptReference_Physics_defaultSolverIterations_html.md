* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics-defaultSolverIterations.html

#  [Physics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.html).defaultSolverIterations
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
defaultSolverIterations; 
### Description
The defaultSolverIterations determines how accurately Rigidbody joints and collision contacts are resolved. (default 6). Must be positive.
If you are having trouble with connected Rigidbodies oscillating and behaving erratically setting a higher solver iteration count may improve their stability (but is slower).  
  
This value is usually changed in `Edit->Project Settings->Physics` inspector instead of from scripts.  
  
**Note:** Changing the defaultSolverIterations does not affect already created Rigidbodies. To change an existing Rigidbody please use [Rigidbody.solverIterations](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-solverIterations.html).  
  
Additional resources: [Physics.defaultSolverVelocityIterations](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics-defaultSolverVelocityIterations.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Physics.defaultSolverIterations[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics-defaultSolverIterations.html) = 10;
    }
}

```

* * *
