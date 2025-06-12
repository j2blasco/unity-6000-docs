* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider-isTrigger.html

#  [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html).isTrigger
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
isTrigger; 
### Description
Specify if this collider is configured as a trigger.
A trigger doesn't register a collision with an incoming [Rigidbody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html). Instead, it sends [OnTriggerEnter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.OnTriggerEnter.html), [OnTriggerExit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.OnTriggerExit.html) and [OnTriggerStay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.OnTriggerStay.html) message when a rigidbody enters or exits the trigger volume.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) m_ObjectCollider;  
  
    void Start()
    {
        //Fetch the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)'s Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) (make sure they have a Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) component)
        m_ObjectCollider = GetComponent<Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html)>();
        //Here the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)'s Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) is not a trigger
        m_ObjectCollider.isTrigger = false;
        //Output whether the Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) is a trigger type Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) or not
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Trigger On : " + m_ObjectCollider.isTrigger);
    }  
  
    void OnMouseDown()
    {
        //GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)'s Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) is now a trigger Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) when the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) is clicked. It now acts as a trigger
        m_ObjectCollider.isTrigger = true;
        //Output to console the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)’s trigger state
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Trigger On : " + m_ObjectCollider.isTrigger);
    }
}

```

* * *
