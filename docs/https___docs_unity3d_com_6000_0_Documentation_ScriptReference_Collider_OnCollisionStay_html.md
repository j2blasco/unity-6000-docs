* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.OnCollisionStay.html

#  [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html).OnCollisionStay(Collision)
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
other | The Collision data associated with this collision event.  
### Description
OnCollisionStay is called once per frame for every Collider or Rigidbody that touches another Collider or Rigidbody.
In contrast to OnTriggerStay, OnCollisionStay is passed the [Collision](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision.html) class and not a Collider. The [Collision](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision.html) class contains information about contact points, impact velocity etc. If you don't use collisionInfo in the function, leave out the collisionInfo parameter as this avoids unneccessary calculations. Notes: Collision events are only sent if one of the colliders also has a non-kinematic rigidbody attached. Collision events are sent to disabled MonoBehaviours, to allow enabling Behaviours in response to collisions. Collision stay events are not sent for sleeping Rigidbodies.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnCollisionStay(Collision[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision.html) collisionInfo)
    {
        // Debug[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.html)-draw all contact points and normals
        foreach (ContactPoint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPoint.html) contact in collisionInfo.contacts)
        {
            Debug.DrawRay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.DrawRay.html)(contact.point, contact.normal * 10, Color.white[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-white.html));
        }
    }
}

```

* * *
