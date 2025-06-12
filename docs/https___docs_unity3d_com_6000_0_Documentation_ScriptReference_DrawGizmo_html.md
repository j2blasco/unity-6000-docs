* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawGizmo.html

# DrawGizmo
class in UnityEditor
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
### Description
The DrawGizmo attribute allows you to supply a gizmo renderer for any [Component](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html).
The renderer function must be static, and take two parameters: the object for which the gizmo is being drawn, and a [GizmoType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GizmoType.html) parameter which indicates the context in which the gizmo is being drawn.  
  
The renderer function can be defined in any class, including editor scripts. This allows you to keep your gizmo-drawing code out of your component scripts so that it is not included in builds.  
  
Additional resources: [GizmoType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GizmoType.html). 
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class MyScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
}  
  
// The icon has to be stored in Assets/Gizmos[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.html)  
  
public class MyScriptGizmoDrawer
{
    [DrawGizmo[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawGizmo.html)(GizmoType.Selected[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GizmoType.Selected.html) | GizmoType.Active[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GizmoType.Active.html))]
    static void DrawGizmoForMyScript(MyScript scr, GizmoType[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GizmoType.html) gizmoType)
    {
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position = scr.transform.position;  
  
        if (Vector3.Distance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Distance.html)(position, Camera.current.transform.position) > 10f)
            Gizmos.DrawIcon[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawIcon.html)(position, "MyScript Gizmo.tiff");
    }
}

```

### Constructors
Constructor | Description  
---|---  
[DrawGizmo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawGizmo-ctor.html) | Defines when the gizmo should be invoked for drawing.  
* * *
