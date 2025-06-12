* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.RadiusHandle.html

#  [Handles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.html).RadiusHandle
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
public static float RadiusHandle([Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, float radius, bool handlesOnly); 
## Declaration
public static float RadiusHandle([Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, float radius); 
### Parameters
Parameter | Description  
---|---  
rotation | The orientation of the handle in 3D space.  
position | The center of the handle in 3D space.  
radius | Radius to modify.  
handlesOnly | Whether to omit the circular outline of the radius and only draw the point handles.  
### Returns
**float** The new value modified by the user's interaction with the handle. If the user has not moved the handle, it will return the same value as you passed into the function.  
  
**Note:** Use HandleUtility.GetHandleSize where you might want to have constant screen-sized handles. 
### Description
Make a Scene view radius handle.
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/RadiusHandle.png)   
_RadiusHandle on the Scene View._
```
// Name this script "EffectRadiusEditor"
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
[CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)(typeof(EffectRadius))]
public class EffectRadiusEditor : Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
{
    public void OnSceneGUI()
    {
        EffectRadius t = (target as EffectRadius);  
  
        EditorGUI.BeginChangeCheck[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.BeginChangeCheck.html)();
        float areaOfEffect = Handles.RadiusHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.RadiusHandle.html)(Quaternion.identity[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion-identity.html), t.transform.position, t.areaOfEffect);
        if (EditorGUI.EndChangeCheck[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.EndChangeCheck.html)())
        {
            Undo.RecordObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.RecordObject.html)(target, "Changed Area Of Effect");
            t.areaOfEffect = areaOfEffect;
        }
    }
}

```

And the Script attached to this GameObject:
```
// Name this script "EffectRadius"
using UnityEngine;
using System.Collections;  
  
public class EffectRadius : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public float areaOfEffect = 1;
}

```

* * *
