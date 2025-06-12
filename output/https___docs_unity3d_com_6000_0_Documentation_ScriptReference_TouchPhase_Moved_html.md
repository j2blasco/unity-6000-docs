* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchPhase.Moved.html

#  [TouchPhase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchPhase.html).Moved
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
### Description
A finger moved on the screen.
```
//Attach this script to an empty GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
//Create some UI Text by going to Create>UI>Text.
//Drag this GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) into the Text field of your GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)’s Inspector window.  
  
using UnityEngine;
using System.Collections;
using UnityEngine.UI;  
  
public class TouchPhaseExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) startPos;
    public Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) direction;  
  
    public Text m_Text;
    string message;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        //Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html) the Text on the screen depending on current TouchPhase[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchPhase.html), and the current direction vector
        m_Text.text = "Touch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Touch.html) : " + message + "in direction" + direction;  
  
        // Track a single touch as a direction control.
        if (Input.touchCount[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-touchCount.html) > 0)
        {
            Touch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Touch.html) touch = Input.GetTouch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetTouch.html)(0);  
  
            // Handle finger movements based on TouchPhase[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchPhase.html)
            switch (touch.phase)
            {
                //When a touch has first been detected, change the message and record the starting position
                case TouchPhase.Began[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchPhase.Began.html):
                    // Record initial touch position.
                    startPos = touch.position;
                    message = "Begun ";
                    break;  
  
                //Determine if the touch is a moving touch
                case TouchPhase.Moved[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchPhase.Moved.html):
                    // Determine direction by comparing the current touch position with the initial one
                    direction = touch.position - startPos;
                    message = "Moving ";
                    break;  
  
                case TouchPhase.Ended[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchPhase.Ended.html):
                    // Report that the touch has ended when it ends
                    message = "Ending ";
                    break;
            }
        }
    }
}

```

* * *
