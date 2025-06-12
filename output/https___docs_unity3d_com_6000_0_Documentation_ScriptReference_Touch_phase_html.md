* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Touch-phase.html

#  [Touch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Touch.html).phase
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
[TouchPhase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchPhase.html) phase; 
### Description
Describes the phase of the touch.
The touch `phase` refers to the action the finger has taken on the most recent frame update. Since a touch is tracked over its "lifetime" by the device, the start and end of a touch and movements in between can be reported on the frames they occur. The `phase` property can be used as the basis of a "switch' statement or as part of a more sophisticated state handling system.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) startPos;
    public Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) direction;
    public bool directionChosen;
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // Track a single touch as a direction control.
        if (Input.touchCount[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-touchCount.html) > 0)
        {
            Touch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Touch.html) touch = Input.GetTouch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetTouch.html)(0);  
  
            // Handle finger movements based on touch phase.
            switch (touch.phase)
            {
                // Record initial touch position.
                case TouchPhase.Began[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchPhase.Began.html):
                    startPos = touch.position;
                    directionChosen = false;
                    break;  
  
                // Determine direction by comparing the current touch position with the initial one.
                case TouchPhase.Moved[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchPhase.Moved.html):
                    direction = touch.position - startPos;
                    break;  
  
                // Report that a direction has been chosen when the finger is lifted.
                case TouchPhase.Ended[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchPhase.Ended.html):
                    directionChosen = true;
                    break;
            }
        }
        if (directionChosen)
        {
            // Something that uses the chosen direction...
        }
    }
}

```

* * *
