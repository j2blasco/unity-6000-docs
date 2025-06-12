* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawSolidArc.html

#  [Handles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.html).DrawSolidArc
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
public static void DrawSolidArc([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) center, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) normal, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) from, float angle, float radius); 
### Parameters
Parameter | Description  
---|---  
center | The center of the circle.  
normal | The normal of the circle.  
from | The direction of the point on the circumference, relative to the center, where the sector begins.  
angle | The angle of the sector, in degrees.  
radius | The radius of the circle  
  
**Note:** Use HandleUtility.GetHandleSize where you might want to have constant screen-sized handles.  
### Description
Draw a circular sector (pie piece) in 3D space.
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/DrawSolidArc.png)   
_Solid Arc in the Scene View._
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
static class ArcExample
{
    static Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) m_Angle = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(1.5f, .66f, 0f);  
  
    // Create an arc at 0, 0, 0 in the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) view and a slider that changes thes angle of the arc.
    [InitializeOnLoadMethod]
    static void Init() => SceneView.duringSceneGui[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView-duringSceneGui.html) += view =>
    {
        Handles.DrawLine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawLine.html)(new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(1.5f, 0f, 0f), new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(1.5f, 1f, 0f));
        var handleSize = HandleUtility.GetHandleSize[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.GetHandleSize.html)(m_Angle) * .1f;
        m_Angle = Handles.Slider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.Slider.html)(m_Angle, Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html), handleSize, Handles.DotHandleCap[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DotHandleCap.html), EditorSnapSettings.move.x);
        m_Angle.y = Mathf.Clamp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Clamp.html)(m_Angle.y, 0f, 1f);
        Handles.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.Label.html)(m_Angle + Vector3.right[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-right.html) * handleSize * 2f, $"Angle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Angle.html) {m_Angle.y * 360f}");  
  
        Handles.DrawSolidArc[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawSolidArc.html)(Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html), Vector3.forward[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-forward.html), Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html), m_Angle.y * -360f, 1f);
    };
}

```

* * *
