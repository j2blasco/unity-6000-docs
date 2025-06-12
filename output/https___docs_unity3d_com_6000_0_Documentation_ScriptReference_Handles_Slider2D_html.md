* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.Slider2D.html

#  [Handles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.html).Slider2D
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
public static [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) Slider2D(int id, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) handlePos, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) offset, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) handleDir, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) slideDir1, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) slideDir2, float handleSize, [Handles.CapFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.CapFunction.html) capFunction, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) snap, bool drawHelper = false); 
## Declaration
public static [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) Slider2D([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) handlePos, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) handleDir, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) slideDir1, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) slideDir2, float handleSize, [Handles.CapFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.CapFunction.html) capFunction, float snap, bool drawHelper = false); 
## Declaration
public static [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) Slider2D(int id, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) handlePos, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) handleDir, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) slideDir1, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) slideDir2, float handleSize, [Handles.CapFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.CapFunction.html) capFunction, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) snap, bool drawHelper = false); 
## Declaration
public static [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) Slider2D([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) handlePos, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) handleDir, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) slideDir1, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) slideDir2, float handleSize, [Handles.CapFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.CapFunction.html) capFunction, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) snap, bool drawHelper = false); 
### Parameters
Parameter | Description  
---|---  
id | (optional) override the default ControlID for this Slider2D instance.  
handlePos | The position of the current point in the space of [Handles.matrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-matrix.html).  
offset | (optional) renders the Slider2D at handlePos, but treats the Slider2D's origin as handlePos + offset. Useful for Slider2D instances that are placed/rendered relative to another object or handle.  
handleDir | The direction of the handle in the space of [Handles.matrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-matrix.html), only used for rendering of the handle.  
slideDir1 | The first axis of the slider's plane of movement in the space of [Handles.matrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-matrix.html).  
slideDir2 | The second axis of the slider's plane of movement in the space of [Handles.matrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-matrix.html).  
handleSize | The size of the handle in the space of [Handles.matrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-matrix.html). Use [HandleUtility.GetHandleSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.GetHandleSize.html) if you want a constant screen-space size.  
snap | (float or Vector2) The snap increment along both axes, either uniform or per-axis. See [Handles.SnapValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.SnapValue.html).  
drawHelper | (default: false) render a rectangle around the handle when dragging.  
capFunction | The function to call for doing the actual drawing.  
### Returns
**Vector3** The new value modified by the user's interaction with the handle. If the user has not moved the handle, it will return the position value passed into the function. 
### Description
Make a 3D slider that moves along a plane defined by two axes.
This method will draw a 3D-draggable handle on the screen. The handle is constrained to sliding along a plane in 3D space.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/SliderHandle2D.png)  
_2D slider handle in the Scene View._  
  
Add the following script to your Assets folder as Slider2DExample.cs and add the Slider2DExample component to an object in a Scene.
```
using UnityEngine;  
  
[ExecuteInEditMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ExecuteInEditMode.html)]
public class Slider2DExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) targetPosition { get { return m_TargetPosition; } set { m_TargetPosition = value; } }
    [SerializeField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeField.html)]
    private Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) m_TargetPosition = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(1f, 0f, 2f);  
  
    public virtual void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        transform.LookAt(m_TargetPosition);
    }
}

```

Add the following script to Assets/Editor as Slider2DExampleEditor.cs and select the object with the Slider2DExample component.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
[CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)(typeof(Slider2DExample)), CanEditMultipleObjects[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanEditMultipleObjects.html)]
public class Slider2DExampleEditor : Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
{
    protected virtual void OnSceneGUI()
    {
        Slider2DExample example = (Slider2DExample)target;  
  
        float size = HandleUtility.GetHandleSize[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.GetHandleSize.html)(example.targetPosition) * 0.5f;
        float snap = 0.1f;
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) handleDirection = Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html);  
  
        EditorGUI.BeginChangeCheck[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.BeginChangeCheck.html)();
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) newTargetPosition = Handles.Slider2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.Slider2D.html)(example.targetPosition, handleDirection, Vector3.right[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-right.html), Vector3.forward[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-forward.html), size, Handles.CircleHandleCap[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.CircleHandleCap.html), snap);
        if (EditorGUI.EndChangeCheck[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.EndChangeCheck.html)())
        {
            Undo.RecordObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.RecordObject.html)(example, "Change Look At Target[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.html) Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Position.html)");
            example.targetPosition = newTargetPosition;
            example.Update();
        }
    }
}

```

* * *
