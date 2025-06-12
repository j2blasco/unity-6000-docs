* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayoutUtility.GetLastRect.html

#  [GUILayoutUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayoutUtility.html).GetLastRect
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
## Declaration
public static [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) GetLastRect(); 
### Returns
**Rect** The last used rectangle. 
### Description
Get the rectangle last used by GUILayout for a control.
Note that this only works during the Repaint event.
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnGUI()
    {
        GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("My button");
        if (Event.current.type == EventType.Repaint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.Repaint.html) &&
            GUILayoutUtility.GetLastRect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayoutUtility.GetLastRect.html)().Contains(Event.current.mousePosition))
        {
            GUILayout.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Label.html)("Mouse over!");
        }
        else
        {
            GUILayout.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Label.html)("Mouse somewhere else");
        }
    }
}

```

* * *
