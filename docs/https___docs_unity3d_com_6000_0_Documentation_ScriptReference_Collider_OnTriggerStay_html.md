* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.OnTriggerStay.html

#  [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html).OnTriggerStay(Collider)
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
### Parameters
Parameter | Description  
---|---  
other | The other Collider involved in this collision.  
### Description
OnTriggerStay is called _almost_ all the frames for every [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) **other** that is touching the trigger. The function is on the physics timer so it won't necessarily run every frame.
This message is sent to the trigger and the collider that touches the trigger. Note that trigger events are only sent if one of the colliders also has a rigidbody attached. Trigger events will be sent to disabled MonoBehaviours, to allow enabling Behaviours in response to collisions.  
  
Additional resources: [Collider.OnTriggerEnter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.OnTriggerEnter.html) which contains a useful example.
```
using UnityEngine;
using System.Collections;
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Applies an upwards force to all rigidbodies that enter the trigger.
    void OnTriggerStay(Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) other)
    {
        if (other.attachedRigidbody)
            other.attachedRigidbody.AddForce(Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html) * 10);
    }
}

```

* * *
