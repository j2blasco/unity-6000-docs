* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.ArcHandle.html

# ArcHandle
class in UnityEditor.IMGUI.Controls
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
A class for a compound handle to edit an angle and a radius in the Scene view.
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/ArcHandle.png) _ArcHandle in the Scene View._  
  
This class allows you to display control handles for editing the angle and radius of an arc. The arc originates at [Vector3.forward](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-forward.html) multiplied by the [radius](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.ArcHandle-radius.html) and rotates around [Vector3.up](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html). The handle rendered by this class's [DrawHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.ArcHandle.DrawHandle.html) method is affected by global state in the [Handles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.html) class, such as [Handles.matrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-matrix.html) and [Handles.color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-color.html).  
  
The following component defines an object with an angle and force property.
```
using UnityEngine;  
  
public class ProjectileExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public float elevationAngle { get { return m_ElevationAngle; } set { m_ElevationAngle = value; } }
    [SerializeField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeField.html)]
    float m_ElevationAngle = 45f;  
  
    public float impulse { get { return m_Impulse; } set { m_Impulse = value; } }
    [SerializeField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeField.html)]
    float m_Impulse = 20f;  
  
    public Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) facingDirection
    {
        get
        {
            Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) result = transform.forward;
            result.y = 0f;
            return result.sqrMagnitude == 0f ? Vector3.forward[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-forward.html) : result.normalized;
        }
    }  
  
    protected virtual void Start()
    {
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) ball = GameObject.CreatePrimitive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.CreatePrimitive.html)(PrimitiveType.Sphere[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Sphere.html));  
  
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) direction = facingDirection;
        direction = Quaternion.AngleAxis[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.AngleAxis.html)(elevationAngle, Vector3.Cross[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Cross.html)(direction, Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html))) * direction;
        ball.AddComponent<Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)>().AddForce(direction  * impulse, ForceMode.Impulse[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode.Impulse.html));
    }
}

```

The following Custom Editor example allows you to edit the elevation angle and force properties for this component in the Scene view, where the force is represented by the radius of the handle.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.IMGUI.Controls;
using UnityEngine;  
  
[CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)(typeof(ProjectileExample))]
public class ProjectileExampleEditor : Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
{
    ArcHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.ArcHandle.html) m_ArcHandle = new ArcHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.ArcHandle.html)();  
  
    protected virtual void OnEnable()
    {
        // arc handle has no radius handle by default
        m_ArcHandle.SetColorWithRadiusHandle(Color.white[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-white.html), 0.1f);
    }  
  
    // the OnSceneGUI callback uses the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) view camera for drawing handles by default
    protected virtual void OnSceneGUI()
    {
        ProjectileExample projectileExample = (ProjectileExample)target;  
  
        // copy the target object's data to the handle
        m_ArcHandle.angle = projectileExample.elevationAngle;
        m_ArcHandle.radius = projectileExample.impulse;  
  
        // set the handle matrix so that angle extends upward from target's facing direction along ground
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) handleDirection = projectileExample.facingDirection;
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) handleNormal = Vector3.Cross[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Cross.html)(handleDirection, Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html));
        Matrix4x4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) handleMatrix = Matrix4x4.TRS[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.TRS.html)(
            projectileExample.transform.position,
            Quaternion.LookRotation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.LookRotation.html)(handleDirection, handleNormal),
            Vector3.one[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-one.html)
        );  
  
        using (new Handles.DrawingScope[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawingScope.html)(handleMatrix))
        {
            // draw the handle
            EditorGUI.BeginChangeCheck[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.BeginChangeCheck.html)();
            m_ArcHandle.DrawHandle();
            if (EditorGUI.EndChangeCheck[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.EndChangeCheck.html)())
            {
                // record the target object before setting new values so changes can be undone/redone
                Undo.RecordObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.RecordObject.html)(projectileExample, "Change Projectile Properties");  
  
                // copy the handle's updated data back to the target object
                projectileExample.elevationAngle = m_ArcHandle.angle;
                projectileExample.impulse = m_ArcHandle.radius;
            }
        }
    }
}

```

Additional resources: [Editor.OnSceneGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.OnSceneGUI.html), [Handles.SetCamera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.SetCamera.html).
### Properties
Property | Description  
---|---  
[angle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.ArcHandle-angle.html) | Returns or specifies the angle of the arc for the handle.  
[angleHandleColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.ArcHandle-angleHandleColor.html) | Returns or specifies the color of the angle control handle.  
[angleHandleDrawFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.ArcHandle-angleHandleDrawFunction.html) | The CapFunction to use when displaying the angle control handle.  
[angleHandleSizeFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.ArcHandle-angleHandleSizeFunction.html) | The SizeFunction to specify how large the angle control handle should be.  
[fillColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.ArcHandle-fillColor.html) | Returns or specifies the color of the arc shape.  
[radius](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.ArcHandle-radius.html) | Returns or specifies the radius of the arc for the handle.  
[radiusHandleColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.ArcHandle-radiusHandleColor.html) | Returns or specifies the color of the radius control handle.  
[radiusHandleDrawFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.ArcHandle-radiusHandleDrawFunction.html) | The CapFunction to use when displaying the radius control handle.  
[radiusHandleSizeFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.ArcHandle-radiusHandleSizeFunction.html) | The SizeFunction to specify how large the angle control handle should be.  
[wireframeColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.ArcHandle-wireframeColor.html) | Returns or specifies the color of the curved line along the outside of the arc.  
### Constructors
Constructor | Description  
---|---  
[ArcHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.ArcHandle-ctor.html) | Creates a new instance of the ArcHandle class.  
### Public Methods
Method | Description  
---|---  
[DrawHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.ArcHandle.DrawHandle.html) | A function to display this instance in the current handle camera using its current configuration.  
[SetColorWithoutRadiusHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.ArcHandle.SetColorWithoutRadiusHandle.html) | Sets angleHandleColor, wireframeColor, and fillColor to the same value, where fillColor will have the specified alpha value. radiusHandleColor will be set to Color.clear and the radius handle will be disabled.  
[SetColorWithRadiusHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.ArcHandle.SetColorWithRadiusHandle.html) | Sets angleHandleColor, radiusHandleColor, wireframeColor, and fillColor to the same value, where fillColor will have the specified alpha value.  
### Static Methods
Method | Description  
---|---  
[DefaultAngleHandleDrawFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.ArcHandle.DefaultAngleHandleDrawFunction.html) | A CapFunction that draws a line terminated with Handles.CylinderHandleCap.  
[DefaultAngleHandleSizeFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.ArcHandle.DefaultAngleHandleSizeFunction.html) | A SizeFunction that returns a fixed screen-space size.  
[DefaultRadiusHandleSizeFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.ArcHandle.DefaultRadiusHandleSizeFunction.html) | A SizeFunction that returns a fixed screen-space size.  
* * *
