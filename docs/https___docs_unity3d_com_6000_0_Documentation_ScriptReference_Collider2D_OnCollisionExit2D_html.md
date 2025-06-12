* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.OnCollisionExit2D.html

#  [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html).OnCollisionExit2D(Collision2D)
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
other | The Collision2D data associated with this collision.  
### Description
Sent when a collider on another object stops touching this object's collider (2D physics only).
Further information about the objects involved is reported in the Collision2D parameter passed during the call.  
  
Notes: Collision events will be sent to disabled MonoBehaviours, to allow enabling Behaviours in response to collisions.  
  
Additional resources: [Collision2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision2D.html) class, [OnCollisionEnter2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.OnCollisionEnter2D.html), [OnCollisionStay2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.OnCollisionStay2D.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    int bumpCount;
    void OnCollisionExit2D(Collision2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision2D.html) collision)
    {
        if (collision.gameObject.tag == "DodgemCar")
        {
            bumpCount++;
        }
    }
}

```

* * *
