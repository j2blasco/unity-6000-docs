* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.ScaleSlider.html

#  [Handles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.html).ScaleSlider
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
public static float ScaleSlider(float scale, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) direction, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation, float size, float snap); 
## Declaration
public static float ScaleSlider(int id, float scale, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) direction, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation, float size, float snap); 
### Parameters
Parameter | Description  
---|---  
scale | The value the user can modify.  
position | The position of the handle in the space of [Handles.matrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-matrix.html).  
direction | The direction of the handle in the space of [Handles.matrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-matrix.html).  
rotation | The rotation of the handle in the space of [Handles.matrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-matrix.html).  
size | The size of the handle in the space of [Handles.matrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-matrix.html). Use [HandleUtility.GetHandleSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.GetHandleSize.html) if you want a constant screen-space size.  
snap | The snap increment. See [Handles.SnapValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.SnapValue.html).  
id | The control ID of the handle.  
### Returns
**float** The new value modified by the user's interaction with the handle. If the user has not moved the handle, it will return the same value as you passed into the function. 
### Description
Make a directional scale slider.
This method will draw a 3D-draggable handle on the screen that looks like one axis on Unity's built-in scale tool. The handle will stretch and will scale a single float up and down.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/ScaleSliderHandle.png)  
_Scale slider handle in the Scene View._  
  
Add the following script to your Assets folder as ScaleSliderExample.cs and add the ScaleSliderExample component to an object in a Scene.
```
using UnityEngine;  
  
[ExecuteInEditMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ExecuteInEditMode.html)]
public class ScaleSliderExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public float scale { get { return m_Scale; } set { m_Scale = value; } }
    [SerializeField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeField.html)]
    private float m_Scale = 1f;  
  
    public virtual void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        transform.localScale = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(scale, 1f, 1f);
    }
}

```

Add the following script to Assets/Editor as ScaleSliderExampleEditor.cs and select the object with the ScaleSliderExample component.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
[CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)(typeof(ScaleSliderExample)), CanEditMultipleObjects[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanEditMultipleObjects.html)]
public class ScaleSliderExampleEditor : Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
{
    public void OnSceneGUI()
    {
        ScaleSliderExample example = (ScaleSliderExample)target;  
  
        float size = HandleUtility.GetHandleSize[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.GetHandleSize.html)(example.transform.position) * 1f;
        float snap = 0.5f;  
  
        EditorGUI.BeginChangeCheck[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.BeginChangeCheck.html)();
        float scale = Handles.ScaleSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.ScaleSlider.html)(example.scale, example.transform.position, example.transform.right, example.transform.rotation, size, snap);
        if (EditorGUI.EndChangeCheck[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.EndChangeCheck.html)())
        {
            Undo.RecordObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.RecordObject.html)(target, "Change Scale[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Scale.html) Value");
            example.scale = scale;
            example.Update();
        }
    }
}

```

* * *
