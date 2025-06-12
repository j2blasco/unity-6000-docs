* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-useGravity.html

#  [Rigidbody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html).useGravity
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
useGravity; 
### Description
Controls whether gravity affects this rigidbody.
If set to false the rigidbody will behave as in outer space.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) coll;  
  
    void Start()
    {
        coll = GetComponent<Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html)>();
        coll.isTrigger = true;
    }  
  
    // Disables gravity on all rigidbodies entering this collider.
    void OnTriggerEnter(Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) other)
    {
        if (other.attachedRigidbody)
            other.attachedRigidbody.useGravity = false;
    }
}

```

* * *
