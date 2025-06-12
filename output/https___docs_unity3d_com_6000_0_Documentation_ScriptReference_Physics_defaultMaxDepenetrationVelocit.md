* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics-defaultMaxDepenetrationVelocity.html

#  [Physics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.html).defaultMaxDepenetrationVelocity
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
defaultMaxDepenetrationVelocity; 
### Description
The maximum default velocity needed to move a Rigidbody's collider out of another collider's surface penetration. Must be positive.
This value is usually changed in `Edit->Project Settings->Physics->Settings->Game Object` inspector instead of from scripts.  
  
**Note:** Very large values can introduce instability during collision detection; too small values might cause the collider depenetration to fail.  
  
You can also set a maximum depenetration velocity for individual Rigidbodies via [Rigidbody.maxDepenetrationVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-maxDepenetrationVelocity.html). 
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // By default defaultMaxDepenetrationVelocity has a value of 10.0f
        Physics.defaultMaxDepenetrationVelocity[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics-defaultMaxDepenetrationVelocity.html) = 5.0f;
    }
}

```

* * *
