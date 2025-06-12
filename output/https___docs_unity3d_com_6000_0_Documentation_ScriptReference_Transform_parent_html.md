* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-parent.html

#  [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html).parent
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Transform.html "Go to Transform Component in the Manual")
[Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) parent; 
### Description
The parent of the transform.
Changing the parent will modify the parent-relative position, scale and rotation but keep the world space position, rotation and scale the same.  
  
Additional resources: [SetParent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.SetParent.html).
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) player;  
  
    //Invoked when a button is pressed.
    public void SetParent(GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) newParent)
    {
        //Makes the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) "newParent" the parent of the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) "player".
        player.transform.parent = newParent.transform;  
  
        //Display[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display.html) the parent's name in the console.
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Player's Parent: " + player.transform.parent.name);  
  
        // Check if the new parent has a parent GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).
        if (newParent.transform.parent != null)
        {
            //Display[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display.html) the name of the grand parent of the player.
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Player's Grand parent: " + player.transform.parent.parent.name);
        }
    }  
  
    public void DetachFromParent()
    {
        // Detaches the transform from its parent.
        transform.parent = null;
    }
}

```

* * *
