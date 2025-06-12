* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.OnCollisionEnter.html

#  [Rigidbody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html).OnCollisionEnter(Collision)
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
### Description
OnCollisionEnter is called when this collider/rigidbody has begun touching another rigidbody/collider.
In contrast to OnTriggerEnter, OnCollisionEnter is passed the [Collision](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision.html) class and not a Collider. The [Collision](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision.html) class contains information about contact points, impact velocity etc. If you don't use collisionInfo in the function, leave out the collisionInfo parameter as this avoids unneccessary calculations. Notes: Collision events are only sent if one of the colliders also has a non-kinematic rigidbody attached. Collision events will be sent to disabled MonoBehaviours, to allow enabling Behaviours in response to collisions.
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
        // Debug[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.html)-draw all contact points and normals
        foreach (ContactPoint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPoint.html) contact in collision.contacts)
        {
            Debug.DrawRay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.DrawRay.html)(contact.point, contact.normal, Color.white[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-white.html));
        }  
  
        // Play a sound if the colliding objects had a big impact.
        if (collision.relativeVelocity.magnitude > 2)
            audioSource.Play();
    }
}

```

Another example:
```
// A grenade
// instantiates a explosion Prefab when hitting a surface
// then destroys itself
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) explosionPrefab;
    void OnCollisionEnter(Collision[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision.html) collision)
    {
        ContactPoint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPoint.html) contact = collision.contacts[0];  
  
        // Rotate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Rotate.html) the object so that the y-axis faces along the normal of the surface
        Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rot = Quaternion.FromToRotation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.FromToRotation.html)(Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html), contact.normal);
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) pos = contact.point;
        Instantiate(explosionPrefab, pos, rot);
        Destroy(gameObject);
    }
}

```

* * *
