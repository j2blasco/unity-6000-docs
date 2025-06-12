* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.OnTriggerStay2D.html

#  [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html).OnTriggerStay2D(Collider2D)
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
other | The other Collider2D involved in this collision.  
### Description
Sent each frame where another object is within a trigger collider attached to this object (2D physics only).
Further information about the other collider is reported in the Collider2D parameter passed during the call.  
  
Notes: Trigger events will be sent to disabled MonoBehaviours, to allow enabling Behaviours in response to collisions.  
  
Additional resources: [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) class, [OnTriggerEnter2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.OnTriggerEnter2D.html), [OnTriggerExit2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.OnTriggerExit2D.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    bool characterInQuicksand = false;  
  
    void OnTriggerStay2D(Collider2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) collider)
    {
        collider.attachedRigidbody.AddForce(-0.1f * collider.attachedRigidbody.velocity);
    }
}

```

* * *
