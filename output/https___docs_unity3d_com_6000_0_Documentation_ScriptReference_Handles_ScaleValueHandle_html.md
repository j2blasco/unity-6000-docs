* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.ScaleValueHandle.html

#  [Handles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.html).ScaleValueHandle
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
public static float ScaleValueHandle(float value, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation, float size, [Handles.CapFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.CapFunction.html) capFunction, float snap); 
### Parameters
Parameter | Description  
---|---  
value | The value the user can modify.  
position | The position of the handle in the space of [Handles.matrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-matrix.html).  
rotation | The rotation of the handle in the space of [Handles.matrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-matrix.html).  
size | The size of the handle in the space of [Handles.matrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-matrix.html). Use [HandleUtility.GetHandleSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.GetHandleSize.html) if you want a constant screen-space size.  
snap | The snap increment. See [Handles.SnapValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.SnapValue.html).  
capFunction | The function to call for doing the actual drawing.  
### Returns
**float** The new value modified by the user's interaction with the handle. If the user has not moved the handle, it will return the same value as you passed into the function. 
### Description
Make a 3D handle that scales a single float.
This method will draw a 3D-draggable handle on the screen. The handle does not move and will scale a single float up and down.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/ScaleValueHandle.png)  
_Scale Value handle in the Scene view with an arrow cap as the handle._  
  
Add the following script to your Assets folder as LightColorLerp.cs and add the LightColorLerp component to an object in a Scene.
```
using UnityEngine;  
  
[ExecuteInEditMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ExecuteInEditMode.html), RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(Light[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html)))]
public class LightColorLerp : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [SerializeField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeField.html)]
    private Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) m_Color1 = Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html);
    [SerializeField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeField.html)]
    private Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) m_Color2 = Color.green[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-green.html);  
  
    public float amount { get { return m_Amount; } set { m_Amount = Mathf.Clamp01[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Clamp01.html)(value); } }
    [SerializeField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeField.html), Range(0f, 1f)]
    private float m_Amount = 1f;  
  
    private Light[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html) m_Light;  
  
    protected virtual void OnEnable()
    {
        m_Light = GetComponent<Light[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html)>();
    }  
  
    public virtual void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        m_Light.color = Color.Lerp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.Lerp.html)(m_Color1, m_Color2, m_Amount);
    }
}

```

Add the following script to Assets/Editor as LightColorLerpEditor.cs and select the object with the LightColorLerp component.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
[CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)(typeof(LightColorLerp)), CanEditMultipleObjects[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanEditMultipleObjects.html)]
public class LightColorLerpEditor : Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
{
    protected virtual void OnSceneGUI()
    {
        LightColorLerp colorLerp = (LightColorLerp)target;  
  
        float size = HandleUtility.GetHandleSize[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.GetHandleSize.html)(colorLerp.transform.position) * 5f;
        float snap = 0.1f;  
  
        EditorGUI.BeginChangeCheck[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.BeginChangeCheck.html)();
        float newAmount = Handles.ScaleValueHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.ScaleValueHandle.html)(colorLerp.amount, colorLerp.transform.position, Quaternion.identity[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion-identity.html), size, Handles.ArrowHandleCap[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.ArrowHandleCap.html), snap);
        if (EditorGUI.EndChangeCheck[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.EndChangeCheck.html)())
        {
            Undo.RecordObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.RecordObject.html)(colorLerp, "Change Light[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html) Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) Interpolation");
            colorLerp.amount = newAmount;
            colorLerp.Update();
        }
    }
}

```

* * *
