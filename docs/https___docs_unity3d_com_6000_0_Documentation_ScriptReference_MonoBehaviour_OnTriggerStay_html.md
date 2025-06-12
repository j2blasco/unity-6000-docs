* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnTriggerStay.html

#  [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html).OnTriggerStay(Collider)
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MonoBehaviour.html "Go to MonoBehaviour Component in the Manual")
### Parameters
Parameter | Description  
---|---  
other | The other Collider involved in this collision.  
### Description
OnTriggerStay is called once per physics update for every [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) `other` that is touching the trigger.
**Note:** Trigger events are only sent if one of the colliders also has a rigidbody attached. Trigger events are sent to disabled MonoBehaviours to allow enabling Behaviours in response to collisions.  
  
This message is sent to the trigger and the collider that touches the trigger.
```
// Applies an upwards force to all rigidbodies that enter the trigger.  
  
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnTriggerStay(Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) other)
    {
        if (other.attachedRigidbody)
        {
            other.attachedRigidbody.AddForce(Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html) * 10);
        }
    }
}

```

OnTriggerStay can be a co-routine, simply use the yield statement in the function.
* * *
