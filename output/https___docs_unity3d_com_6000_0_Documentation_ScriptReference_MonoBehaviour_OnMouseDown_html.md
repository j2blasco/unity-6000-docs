* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnMouseDown.html

#  [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html).OnMouseDown()
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
[OnMouseDown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnMouseDown.html) is called when the user presses the left mouse button while over the [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html).
This event is sent to all scripts of the GameObject with [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html). Scripts of the parent or child objects do not receive this event.
```
using UnityEngine;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnMouseDown()
    {
        // Destroy the gameObject after clicking on it
        Destroy(gameObject);
    }
}

```

Note: This function is not called on objects that belong to Ignore Raycast layer.  
  
This function is called on Colliders and 2D Colliders marked as trigger when the following properties are set to true:   
  
- For 3D physics: [Physics.queriesHitTriggers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics-queriesHitTriggers.html)  
  
- For 2D physics: [Physics2D.queriesHitTriggers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D-queriesHitTriggers.html)   
  
In addition, `OnMouseDown` can be a coroutine.
* * *
