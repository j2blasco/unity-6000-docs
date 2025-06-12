* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.ScaleAroundPivot.html

#  [GUIUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.html).ScaleAroundPivot
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
public static void ScaleAroundPivot([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) scale, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) pivotPoint); 
### Description
Helper function to scale the GUI around a point.
Modifies [GUI.matrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-matrix.html) to scale all GUI elements around a `pivotPoint`.  
  
Additional resources: [GUI.matrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-matrix.html), [RotateAroundPivot](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.RotateAroundPivot.html).
```
using UnityEngine;
using System.Collections;  
  
// Scale[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Scale.html) a button by 1.5 times each time is pressed.  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) scale = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(1, 1);
    private Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) pivotPoint;  
  
    void OnGUI()
    {
        pivotPoint = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(Screen.width[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-width.html) / 2, Screen.height[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-height.html) / 2);
        GUIUtility.ScaleAroundPivot[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.ScaleAroundPivot.html)(scale, pivotPoint);  
  
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(Screen.width[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-width.html) / 2 - 25, Screen.height[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-height.html) / 2 - 25, 50, 50), "Big!"))
        {
            scale += new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(0.5F, 0.5F);
        }
    }
}

```

* * *
