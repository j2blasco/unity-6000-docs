* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPoint-normal.html

#  [ContactPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPoint.html).normal
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
[Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) normal; 
### Description
Normal of the contact point.
The following example will draw a line to represent every normal from a collision. Each line will be drawn in the Scene view.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnCollisionEnter(Collision[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision.html) other)
    {
        // Print how many points are colliding with this transform
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Points colliding: " + other.contacts.Length);  
  
        // Print the normal of the first point in the collision.
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Normal of the first point: " + other.contacts[0].normal);  
  
        // Draw a different colored ray for every normal in the collision
        foreach (var item in other.contacts)
        {
            Debug.DrawRay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.DrawRay.html)(item.point, item.normal * 100, Random.ColorHSV[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.ColorHSV.html)(0f, 1f, 1f, 1f, 0.5f, 1f), 10f);
        }
    }
}

```

* * *
