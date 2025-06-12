* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.CylinderHandleCap.html

#  [Handles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.html).CylinderHandleCap
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
public static void CylinderHandleCap(int controlID, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation, float size, [EventType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.html) eventType); 
### Parameters
Parameter | Description  
---|---  
controlID | The control ID for the handle.  
position | The position of the handle in the space of [Handles.matrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-matrix.html).  
rotation | The rotation of the handle in the space of [Handles.matrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-matrix.html).  
size | The size of the handle in the space of [Handles.matrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-matrix.html). Use [HandleUtility.GetHandleSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.GetHandleSize.html) if you want a constant screen-space size.  
eventType | Event type for the handle to act upon. By design it handles [EventType.Layout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.Layout.html) and [EventType.Repaint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.Repaint.html) events.  
### Description
Draw a cylinder handle. Pass this into handle functions.
On [EventType.Layout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.Layout.html) event, calculates handle distance to mouse and calls [HandleUtility.AddControl](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.AddControl.html) accordingly.  
  
On [EventType.Repaint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.Repaint.html) event, draws the handle shape.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/CylinderCap.png) _Cylinder Handle Cap in the Scene View._  
  
Add the following script to your Assets folder as CylinderExample.cs and add the CylinderExample component to an object in a Scene.
```
using UnityEngine;  
  
public class CylinderExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html) {}

```

Add the following script to Assets/Editor as CylinderExampleEditor.cs and select the object with the CylinderExample component.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
[CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)(typeof(CylinderExample))]
public class CylinderExampleEditor : Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
{
    float size = 1f;  
  
    protected virtual void OnSceneGUI()
    {
        if (Event.current.type == EventType.Repaint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.Repaint.html))
        {
            Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) transform = ((CylinderExample)target).transform;
            Handles.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-color.html) = Handles.xAxisColor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-xAxisColor.html);
            Handles.CylinderHandleCap[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.CylinderHandleCap.html)(
                0,
                transform.position + new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(3f, 0f, 0f),
                transform.rotation * Quaternion.LookRotation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.LookRotation.html)(Vector3.right[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-right.html)),
                size,
                EventType.Repaint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.Repaint.html)
            );
            Handles.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-color.html) = Handles.yAxisColor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-yAxisColor.html);
            Handles.CylinderHandleCap[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.CylinderHandleCap.html)(
                0,
                transform.position + new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0f, 3f, 0f),
                transform.rotation * Quaternion.LookRotation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.LookRotation.html)(Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html)),
                size,
                EventType.Repaint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.Repaint.html)
            );
            Handles.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-color.html) = Handles.zAxisColor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-zAxisColor.html);
            Handles.CylinderHandleCap[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.CylinderHandleCap.html)(
                0,
                transform.position + new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0f, 0f, 3f),
                transform.rotation * Quaternion.LookRotation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.LookRotation.html)(Vector3.forward[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-forward.html)),
                size,
                EventType.Repaint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.Repaint.html)
            );
        }
    }
}

```

* * *
