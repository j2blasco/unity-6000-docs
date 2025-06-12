* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-solverIterations.html

#  [Rigidbody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html).solverIterations
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html "Go to Rigidbody Component in the Manual")
solverIterations; 
### Description
The solverIterations determines how accurately Rigidbody joints and collision contacts are resolved. Overrides [Physics.defaultSolverIterations](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics-defaultSolverIterations.html). Must be positive.
If you are having trouble with connected Rigidbodies oscillating and behaving erratically setting a higher solver iteration count may improve their stability (but is slower).  
  
Additional resources: [Rigidbody.solverVelocityIterations](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-solverVelocityIterations.html).
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) rb = GetComponent<Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)>();
        rb.solverIterations = 30;
    }
}

```

* * *
