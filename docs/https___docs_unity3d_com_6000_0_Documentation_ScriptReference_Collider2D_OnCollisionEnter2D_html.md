* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.OnCollisionEnter2D.html

#  [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html).OnCollisionEnter2D(Collision2D)
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
Sent when an incoming collider makes contact with this object's collider (2D physics only).
Further information about the collision is reported in the Collision 2D parameter passed during the call.  
  
Notes: Collision events will be sent to disabled MonoBehaviours, to allow enabling Behaviours in response to collisions.  
  
Additional resources: [Collision2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision2D.html) class, [OnCollisionExit2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.OnCollisionExit2D.html), [OnCollisionStay2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.OnCollisionStay2D.html).
```
using UnityEngine; 
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html) 
{ 
    void OnCollisionEnter2D(Collision2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision2D.html) collision) 
    { 
        if (collision.gameObject.CompareTag("Enemy")) 
        { 
            collision.gameObject.SendMessage("ApplyDamage", 10); 
        } 
    } 
}
```

* * *
