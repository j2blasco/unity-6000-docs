* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Touch-position.html

#  [Touch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Touch.html).position
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
[Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) position; 
### Description
The position of the touch in screen space pixel coordinates.
Position returns the current position of a touch contact as it's dragged. If you need the original position of the touch see [Touch.rawPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Touch-rawPosition.html).  
  
The bottom-left of the screen or window is at (0, 0). The top-right of the screen or window is at (Screen.width, Screen.height).
```
// This script outputs the position of an active touch contact  
  
// Attach this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
// Create a Text GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) (GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)>UI>Text)
// Attach the Text to the Text field in the Inspector window of your GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)  
  
using UnityEngine;
using UnityEngine.UI;  
  
public class TouchPositionExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Text m_Text;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (Input.touchCount[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-touchCount.html) > 0)
        {
            Touch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Touch.html) touch = Input.GetTouch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetTouch.html)(0);  
  
            // Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html) the Text on the screen depending on current position of the touch each frame
            m_Text.text = "Touch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Touch.html) Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Position.html) : " + touch.position;
        }
        else
        {
            m_Text.text = "No touch contacts";
        }
    }
}

```

* * *
