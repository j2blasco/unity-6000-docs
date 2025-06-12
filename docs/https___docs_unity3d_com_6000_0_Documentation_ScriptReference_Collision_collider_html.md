* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision-collider.html

#  [Collision](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision.html).collider
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
[Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) collider; 
### Description
The [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) we hit (Read Only).
Fetch the Collider of the GameObject your GameObject hits. To find all colliders that were hit in detail you have to iterate the contact points ([contacts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision-contacts.html) property).
```
//In this example, the name of the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) that collides with your GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) is output to the console. Then this checks the name of the Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) and if it matches with the one you specify, it outputs another message.  
  
//Create a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) and make sure it has a Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) component. Attach this script to it.
//Create a second GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) with a Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) and place it on top of the other GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) to output that there was a collision. You can add movement to the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) to test more.  
  
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    //If your GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) starts to collide with another GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) with a Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html)
    void OnCollisionEnter(Collision[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision.html) collision)
    {
        //Output the Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html)'s GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)'s name
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(collision.collider.name);
    }  
  
    //If your GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) keeps colliding with another GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) with a Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html), do something
    void OnCollisionStay(Collision[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision.html) collision)
    {
        //Check to see if the Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html)'s name is "Chest"
        if (collision.collider.name == "Chest")
        {
            //Output the message
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Chest is here!");
        }
    }
}

```

* * *
