* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.GUIPointToScreenPixelCoordinate.html

#  [HandleUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.html).GUIPointToScreenPixelCoordinate
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
public static [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) GUIPointToScreenPixelCoordinate([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) guiPoint); 
### Description
Converts a 2D GUI position to screen pixel coordinates.
The bottom-left of the screen or window is at (0, 0). The top-right of the screen or window is at ([Screen.width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-width.html), [Screen.height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-height.html)).  
  
Additional resources: [Input.mousePosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-mousePosition.html) and [Camera.ScreenPointToRay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.ScreenPointToRay.html).
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public static Ray[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ray.html) GUIPointToWorldRay(Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) guiPos, Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) camera)
    {
        Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) screenPixelPos = HandleUtility.GUIPointToScreenPixelCoordinate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.GUIPointToScreenPixelCoordinate.html)(guiPos);
        return Camera.main.ScreenPointToRay(screenPixelPos);
    }
}

```

* * *
