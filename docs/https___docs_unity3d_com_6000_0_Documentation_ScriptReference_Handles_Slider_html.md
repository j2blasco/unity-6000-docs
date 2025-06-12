* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.Slider.html

#  [Handles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.html).Slider
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
public static [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) Slider([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) direction); 
## Declaration
public static [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) Slider([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) direction, float size, [Handles.CapFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.CapFunction.html) capFunction, float snap); 
### Parameters
Parameter | Description  
---|---  
position | The position of the current point in the space of [Handles.matrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-matrix.html).  
direction | The direction axis of the slider in the space of [Handles.matrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-matrix.html).  
size | The size of the handle in the space of [Handles.matrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-matrix.html). Use [HandleUtility.GetHandleSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.GetHandleSize.html) if you want a constant screen-space size.  
snap | The snap increment. See [Handles.SnapValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.SnapValue.html).  
capFunction | The function to call for doing the actual drawing. By default it is [Handles.ArrowHandleCap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.ArrowHandleCap.html), but any function that has the same signature can be used.  
### Returns
**Vector3** The new value modified by the user's interaction with the handle. If the user has not moved the handle, it will return the position value passed into the function. 
### Description
Make a 3D slider that moves along one axis.
This method will draw a 3D-draggable handle on the screen. The handle is constrained to sliding along a direction vector in 3D space.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/SliderHandle.png)  
_Slider handle in the Scene View._  
  
Add the following script to your Assets folder as SliderExample.cs and add the SliderExample component to an object in a Scene.
```
using UnityEngine;  
  
[ExecuteInEditMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ExecuteInEditMode.html)]
public class SliderExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
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
Add the following script to Assets/Editor as SliderExampleEditor.cs and select the object with the SliderExample component.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
[CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)(typeof(SliderExample)), CanEditMultipleObjects[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanEditMultipleObjects.html)]
public class SliderExampleEditor : Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
{
    protected virtual void OnSceneGUI()
    {
        SliderExample example = (SliderExample)target;  
  
        float size = HandleUtility.GetHandleSize[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.GetHandleSize.html)(example.targetPosition) * 0.5f;
        float snap = 0.1f;  
  
        EditorGUI.BeginChangeCheck[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.BeginChangeCheck.html)();
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) newTargetPosition = Handles.Slider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.Slider.html)(example.targetPosition, Vector3.right[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-right.html), size, Handles.ConeHandleCap[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.ConeHandleCap.html), snap);
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
