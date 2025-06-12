* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.RotateAroundPivot.html

#  [GUIUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.html).RotateAroundPivot
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
public static void RotateAroundPivot(float angle, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) pivotPoint); 
### Description
Helper function to rotate the GUI around a point.
Modifies [GUI.matrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-matrix.html) to rotate all GUI elements `angle` degrees around `pivotPoint`.  
  
Additional resources: [GUI.matrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-matrix.html), [ScaleAroundPivot](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.ScaleAroundPivot.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Rotate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Rotate.html) a button 10 degrees clockwise when pressed.  
  
    float rotAngle = 0;
    Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) pivotPoint;  
  
    void OnGUI()
    {
        pivotPoint = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(Screen.width[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-width.html) / 2, Screen.height[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-height.html) / 2);
        GUIUtility.RotateAroundPivot[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.RotateAroundPivot.html)(rotAngle, pivotPoint);
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(Screen.width[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-width.html) / 2 - 25, Screen.height[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-height.html) / 2 - 25, 50, 50), "Rotate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Rotate.html)"))
        {
            rotAngle += 10;
        }
    }
}

```

* * *
