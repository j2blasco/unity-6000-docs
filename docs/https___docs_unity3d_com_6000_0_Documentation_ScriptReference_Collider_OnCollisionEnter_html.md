* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.OnCollisionEnter.html

#  [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html).OnCollisionEnter(Collision)
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
OnCollisionEnter is called when this collider/rigidbody has begun touching another rigidbody/collider.
In contrast to [OnTriggerEnter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.OnTriggerEnter.html), [OnCollisionEnter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.OnCollisionEnter.html) is passed the [Collision](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision.html) class and not a Collider. The [Collision](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision.html) class contains information, for example, about contact points and impact velocity. Notes: Collision events are only sent if one of the colliders also has a non-kinematic rigidbody attached. Collision events will be sent to disabled MonoBehaviours, to allow enabling Behaviours in response to collisions.
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
Another example:
```
// A grenade
// - instantiates an explosion Prefab when hitting a surface
// - then destroys itself  
  
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) explosionPrefab;  
  
    void OnCollisionEnter(Collision[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision.html) collision)
    {
        ContactPoint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPoint.html) contact = collision.contacts[0];
        Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation = Quaternion.FromToRotation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.FromToRotation.html)(Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html), contact.normal);
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position = contact.point;
        Instantiate(explosionPrefab, position, rotation);
        Destroy(gameObject);
    }
}

```

* * *
