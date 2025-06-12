* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-touches.html

#  [Input](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.html).touches
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
touches; 
### Description
Returns list of objects representing status of all touches during last frame. (Read Only) (Allocates temporary variables).
**Note** : This API is part of the legacy Input Manager. The recommended best practice is that you don't use this API in new projects. For new projects, use the Input System package. To learn more about input, refer to [Input](https://docs.unity3d.com/6000.0/Documentation/Manual/Input.html).  
  
Each entry represents a status of a finger touching the screen.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Prints number of fingers touching the screen
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        var fingerCount = 0;
        foreach (Touch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Touch.html) touch in Input.touches[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-touches.html))
        {
            if (touch.phase != TouchPhase.Ended[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchPhase.Ended.html) && touch.phase != TouchPhase.Canceled[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchPhase.Canceled.html))
            {
                fingerCount++;
            }
        }
        if (fingerCount > 0)
        {
            print("User has " + fingerCount + " finger(s) touching the screen");
        }
    }
}

```

* * *
