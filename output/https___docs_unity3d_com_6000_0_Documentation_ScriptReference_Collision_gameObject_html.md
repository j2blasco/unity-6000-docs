* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision-gameObject.html

#  [Collision](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision.html).gameObject
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
[GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) gameObject; 
### Description
The [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) whose collider you are colliding with. (Read Only).
This is the GameObject that is colliding with your GameObject. Access this to check properties of the colliding GameObject, for example, the GameObject’s name and tag.
```
using UnityEngine;  
  
public class CollisionGameObjectExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    //Detect collisions between the GameObjects with Colliders attached
    void OnCollisionEnter(Collision[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision.html) collision)
    {
        //Check for a match with the specified name on any GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) that collides with your GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
        if (collision.gameObject.name == "MyGameObjectName")
        {
            //If the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)'s name matches the one you suggest, output this message in the console
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Do something here");
        }  
  
        //Check for a match with the specific tag on any GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) that collides with your GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
        if (collision.gameObject.tag == "MyGameObjectTag")
        {
            //If the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) has the same tag as specified, output this message in the console
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Do something else here");
        }
    }
}

```

* * *
