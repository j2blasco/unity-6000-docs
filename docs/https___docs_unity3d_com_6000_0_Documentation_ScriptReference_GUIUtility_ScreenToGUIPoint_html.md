* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.ScreenToGUIPoint.html

#  [GUIUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.html).ScreenToGUIPoint
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
public static [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) ScreenToGUIPoint([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) screenPoint); 
### Description
Convert a point from screen space to GUI position.
Used for reconverting values calculated from [GUIToScreenPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.GUIToScreenPoint.html)  
  
**Note:** In Unity the screen space **y** coordinate varies from zero at the top edge of the window to a maximum at the bottom edge of the window. This is different from what you might expect.  
  
Additional resources: [GUIUtility.GUIToScreenPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.GUIToScreenPoint.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Check the difference between the mouse position (Screen[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen.html)) and
    // the converted GUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html) positions because of the group.  
  
    void OnGUI()
    {
        Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) screenPos = Event.current.mousePosition;
        GUI.BeginGroup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.BeginGroup.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 10, 100, 100));
        Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) convertedGUIPos = GUIUtility.ScreenToGUIPoint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.ScreenToGUIPoint.html)(screenPos);
        GUI.EndGroup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.EndGroup.html)();
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Screen[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen.html): " + screenPos + " GUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html): " + convertedGUIPos);
    }
}

```

* * *
