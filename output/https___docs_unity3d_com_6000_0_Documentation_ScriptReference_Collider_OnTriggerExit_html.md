* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.OnTriggerExit.html

#  [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html).OnTriggerExit(Collider)
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
OnTriggerExit is called when the [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) `other` has stopped touching the trigger.
This message is sent to the trigger and the Collider that touches the trigger.  
  
**Notes:** Trigger events are only sent if one of the Colliders also has a Rigidbody attached. Trigger events will be sent to disabled MonoBehaviours, to allow enabling Behaviours in response to collisions. [OnTriggerExit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.OnTriggerExit.html) occurs on the FixedUpdate after the Colliders have stopped touching. The Colliders involved are not guaranteed to be at the point of initial separation. Deactivating or destroying a Collider while it is inside a trigger volume will not register an on exit event.  
  
Additional resources: [Collider.OnTriggerEnter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.OnTriggerEnter.html) which contains a useful example.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnTriggerExit(Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) other)
    {
        // Destroy everything that leaves the trigger
        Destroy(other.gameObject);
    }
}

```

* * *
