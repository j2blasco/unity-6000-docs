* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnMouseUp.html

#  [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html).OnMouseUp()
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
OnMouseUp is called when the user has released the mouse button.
Note that OnMouseUp is called even if the mouse is not over the same [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) as the mouse has been pressed down on. For button-like behavior see: [OnMouseUpAsButton](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnMouseUpAsButton.html).
```
// Register when mouse dragging has ended. OnMouseUp is called
// when the mouse button is released.  
  
using UnityEngine;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnMouseUp()
    {
        // If the user releases the mouse button while over the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) with this script attached, output this message
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Drag ended!");
    }
}

```

**Note:** This function is not called on objects that belong to Ignore Raycast layer.  
  
This function is called on Colliders and 2D Colliders marked as trigger when the following properties are set to true:   
  
- For 3D physics: [Physics.queriesHitTriggers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics-queriesHitTriggers.html)  
  
- For 2D physics: [Physics2D.queriesHitTriggers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D-queriesHitTriggers.html)   
  
[OnMouseUp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnMouseUp.html) can be a co-routine. Simply use the yield statement in the function. This event is sent to all scripts attached to the [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html).  
  
Additional resources: [OnMouseDown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnMouseDown.html), [OnMouseDrag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnMouseDrag.html).
* * *
