* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnMouseExit.html

#  [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html).OnMouseExit()
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MonoBehaviour.html "Go to MonoBehaviour Component in the Manual")
### Description
Called when the mouse is not any longer over the [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html).
A call to OnMouseExit follows the corresponding calls to [OnMouseEnter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnMouseEnter.html) and [OnMouseOver](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnMouseOver.html).  
  
**Note:** This function is not called on objects that belong to Ignore Raycast layer.  
  
This function is called on Colliders and 2D Colliders marked as trigger when the following properties are set to true:   
  
- For 3D physics: [Physics.queriesHitTriggers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics-queriesHitTriggers.html)  
  
- For 2D physics - [Physics2D.queriesHitTriggers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D-queriesHitTriggers.html)   
  
You can use OnMouseExit as a co-routine if you add a yield statement somewhere in the function. This event is sent to all scripts attached to the [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html).
```
//Attach this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) to have it output messages when your mouse hovers over it.
using UnityEngine;  
  
public class OnMouseOverExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnMouseOver()
    {
        //If your mouse hovers over the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) with the script attached, output this message
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Mouse is over GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).");
    }  
  
    void OnMouseExit()
    {
        //The mouse is no longer hovering over the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) so output this message each frame
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Mouse is no longer on GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).");
    }
}

```

* * *
