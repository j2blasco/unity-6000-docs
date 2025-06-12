* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision2D-contacts.html

#  [Collision2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision2D.html).contacts
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
contacts; 
### Description
The specific points of contact with the incoming Collider2D. You should avoid using this as it produces memory garbage. Use [GetContact](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision2D.GetContact.html) or [GetContacts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision2D.GetContacts.html) instead.
Additional resources: [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) class.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) explosion;  
  
    void OnCollisionEnter2D(Collision2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision2D.html) coll)
    {
        // If a missile hits this object
        if (coll.transform.tag == "Missile")
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("HIT!");  
  
            // Spawn an explosion at each point of contact
            foreach (ContactPoint2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPoint2D.html) missileHit in coll.contacts)
            {
                Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) hitPoint = missileHit.point;
                Instantiate(explosion, new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(hitPoint.x, hitPoint.y, 0), Quaternion.identity[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion-identity.html));
            }
        }
    }
}

```

* * *
