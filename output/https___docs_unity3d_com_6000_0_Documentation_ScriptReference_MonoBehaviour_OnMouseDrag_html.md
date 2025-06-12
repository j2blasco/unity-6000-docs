* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnMouseDrag.html

#  [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html).OnMouseDrag()
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
OnMouseDrag is called when the user has clicked on a [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) and is still holding down the mouse.
OnMouseDrag is called every frame while the mouse is down.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) rend;  
  
    void Start()
    {
        rend = GetComponent<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)>();
    }  
  
    void OnMouseDrag()
    {
        rend.material.color -= Color.white[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-white.html) * Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html);
    }
}

```

**Note:** This function is not called on objects that belong to Ignore Raycast layer.  
  
This function is called on Colliders and 2D Colliders marked as trigger when the following properties are set to true:   
  
- For 3D physics: [Physics.queriesHitTriggers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics-queriesHitTriggers.html)  
  
- For 2D physics: [Physics2D.queriesHitTriggers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D-queriesHitTriggers.html)   
  
OnMouseDrag can be a co-routine, simply use the yield statement in the function. This event is sent to all scripts attached to the [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html).
* * *
