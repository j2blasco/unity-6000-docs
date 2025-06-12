* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawGizmo-ctor.html

# DrawGizmo Constructor
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
public DrawGizmo([GizmoType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GizmoType.html) gizmo); 
### Parameters
Parameter | Description  
---|---  
gizmo | Flags to denote when the gizmo should be drawn.  
### Description
Defines when the gizmo should be invoked for drawing.
Additional resources: [GizmoType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GizmoType.html), [DrawGizmo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawGizmo.html).
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
// Draw an image above the light when the light is not selected
// The icon has to be stored in Assets/Gizmos[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.html)  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Draw an image above the light when the light is not selected
    [DrawGizmo[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawGizmo.html)(GizmoType.NotInSelectionHierarchy[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GizmoType.NotInSelectionHierarchy.html) | GizmoType.Pickable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GizmoType.Pickable.html))]
    static void drawGizmo1(Light[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html) light, GizmoType[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GizmoType.html) gizmoType)
    {
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position = light.transform.position;  
  
        Gizmos.DrawIcon[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawIcon.html)(position + Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html), "ninja.jpg");
    }  
  
    // Place a red sphere around a selected light.
    // Surround the sphere dark shaded when not selected.
    [DrawGizmo[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawGizmo.html)(GizmoType.Selected[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GizmoType.Selected.html) | GizmoType.NonSelected[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GizmoType.NonSelected.html))]
    static void drawGizmo2(Light[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html) light, GizmoType[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GizmoType.html) gizmoType)
    {
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position = light.transform.position;  
  
        if ((gizmoType & GizmoType.Selected[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GizmoType.Selected.html)) != 0)
        {
            Gizmos.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos-color.html) = Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html);
        }
        else
        {
            Gizmos.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos-color.html) = Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html) * 0.5f;
        }
        Gizmos.DrawSphere[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawSphere.html)(position , 1);
    }
}

```

* * *
## Declaration
public DrawGizmo([GizmoType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GizmoType.html) gizmo, Type drawnGizmoType); 
### Parameters
Parameter | Description  
---|---  
gizmo | Flags to denote when the gizmo should be drawn.  
drawnGizmoType | Type of object for which the gizmo should be drawn.  
### Description
Same as above. `drawnGizmoType` determines of what type the object we are drawing the gizmo of has to be.
If drawnGizmoType is null, the type will be determined from the first parameter of the draw gizmo method. If drawnGizmoType is not null, it must be the same type as, or a subtype of, the type of the first parameter.
* * *
