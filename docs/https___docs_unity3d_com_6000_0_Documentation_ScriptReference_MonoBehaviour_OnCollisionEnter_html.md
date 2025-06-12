* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnCollisionEnter.html

#  [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html).OnCollisionEnter(Collision)
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
other | The [Collision](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision.html) data associated with this collision.  
### Description
OnCollisionEnter is called when this collider/rigidbody has begun touching another rigidbody/collider.
In contrast to [OnTriggerEnter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnTriggerEnter.html), [OnCollisionEnter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnCollisionEnter.html) is passed the [Collision](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision.html) class and not a [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html). The [Collision](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision.html) class contains information about contact points, impact velocity etc. If you don't use collisionInfo in the function, leave out the collisionInfo parameter as this avoids unneccessary calculations. **Note:** Collision events are only sent if one of the colliders also has a non-kinematic rigidbody attached. Collision events will be sent to disabled MonoBehaviours, to allow enabling Behaviours in response to collisions.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) audioSource;  
  
    void Start()
    {
        audioSource = GetComponent<AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html)>();
    }  
  
    void OnCollisionEnter(Collision[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision.html) collision)
    {
        foreach (ContactPoint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPoint.html) contact in collision.contacts)
        {
            Debug.DrawRay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.DrawRay.html)(contact.point, contact.normal, Color.white[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-white.html));
        }  
  
        if (collision.relativeVelocity.magnitude > 2)
            audioSource.Play();
    }
}

```

OnCollisionEnter can be a co-routine, simply use the yield statement in the function.
* * *
