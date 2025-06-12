* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.GUIToScreenPoint.html

#  [GUIUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.html).GUIToScreenPoint
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
public static [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) GUIToScreenPoint([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) guiPoint); 
### Description
Convert a point from GUI position to screen space.
**Note:** In Unity the screen space **y** coordinate varies from zero at the top edge of the window to a maximum at the bottom edge of the window. This is different from what you might expect.  
  
Additional resources: [GUIUtility.ScreenToGUIPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.ScreenToGUIPoint.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Converts a GUICoordinate (affected by a group) to a Screen[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen.html) coordinate.  
  
    void OnGUI()
    {
        Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) gPos = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(10, 10);
        GUI.BeginGroup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.BeginGroup.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 10, 100, 100));
        Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) convertedGUIPos = GUIUtility.GUIToScreenPoint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.GUIToScreenPoint.html)(gPos);
        GUI.EndGroup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.EndGroup.html)();
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("GUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html): " + gPos + " Screen[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen.html): " + convertedGUIPos);
    }
}

```

* * *
