* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawWireArc.html

#  [Handles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.html).DrawWireArc
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
public static void DrawWireArc([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) center, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) normal, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) from, float angle, float radius, float thickness = 0.0f); 
### Parameters
Parameter | Description  
---|---  
center | The center of the circle in world space.  
normal | The normal of the circle in world space.  
from | The direction of the point on the circle circumference, relative to the center, where the arc begins.  
angle | The angle of the arc, in degrees.  
radius | The radius of the circle in world space units.  
thickness | Line thickness in UI points (zero thickness draws single-pixel line).  
### Description
Draws a circular arc in 3D space.
The [Handles.color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-color.html) and [Handles.matrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-matrix.html) properties colorize and additionally transform the arc position. Unity ignores `DrawWireArc` (that is, nothing happens) when the current GUI event type is not [Repaint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.Repaint.html).  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/DrawWireArc.png)  
_Wire Arc in the Scene View._
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using System.Collections;  
  
//this class should exist somewhere in your project
public class WireArcExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public float shieldArea;
}  
  
// Create a 180 degrees wire arc with a ScaleValueHandle attached to the disc
// that lets you modify the "shieldArea" value in the WireArcExample
[CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)(typeof(WireArcExample))]
public class DrawWireArc : Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
{
    void OnSceneGUI()
    {
        Handles.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-color.html) = Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html);
        WireArcExample myObj = (WireArcExample)target;
        Handles.DrawWireArc[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawWireArc.html)(myObj.transform.position, myObj.transform.up, -myObj.transform.right, 180, myObj.shieldArea);
        myObj.shieldArea = (float)Handles.ScaleValueHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.ScaleValueHandle.html)(myObj.shieldArea, myObj.transform.position + myObj.transform.forward * myObj.shieldArea, myObj.transform.rotation, 1, Handles.ConeHandleCap[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.ConeHandleCap.html), 1);
    }
}

```

You can use [HandleUtility.GetHandleSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.GetHandleSize.html) to calculate a suitable size for a manipulator handle.  
  
Arc line `thickness` can be optionally set. Zero thickness draws a one-pixel line. Larger thickness values express line thickness in UI points. For example, a thickness of 1.0 could be two pixels wide on screen if the display zoom is 200% (see [EditorGUIUtility.pixelsPerPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility-pixelsPerPoint.html)).  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/HandlesDrawWireArcThickness.png)  
_Arcs of varying thickness._
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
}  
  
// Display[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display.html) arcs of various angles and thickness in the scene view
[CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)(typeof(ExampleScript))]
public class ExampleEditor : Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
{
    public void OnSceneGUI()
    {
        var t = target as ExampleScript;
        var tr = t.transform;
        var position = tr.position;
        Handles.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-color.html) = Color.yellow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-yellow.html);
        for (int i = 0; i < 10; ++i)
        {
            var center = position;
            var start = Vector3.left[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-left.html);
            var normal = Vector3.forward[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-forward.html);
            var radius = 3 - i * 0.3f;
            var angle = 40 + 30 * i;
            Handles.DrawWireArc[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawWireArc.html)(center, normal, start, angle, radius, i);
        }
    }
}

```

Additional resources: [Handles.lineThickness](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-lineThickness.html), [Handles.DrawLine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawLine.html), [Handles.DrawSolidArc](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawSolidArc.html), [Handles.DrawWireDisc](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawWireDisc.html).
* * *
