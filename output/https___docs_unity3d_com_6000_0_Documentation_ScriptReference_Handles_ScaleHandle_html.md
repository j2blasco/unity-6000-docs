* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.ScaleHandle.html

#  [Handles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.html).ScaleHandle
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
public static [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) ScaleHandle([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) scale, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation, float size); 
### Parameters
Parameter | Description  
---|---  
scale | Scale to modify.  
position | The position of the handle.  
rotation | The rotation of the handle.  
size | Allows you to scale the size of the handle on-screen.  
### Returns
**Vector3** The new value modified by the user's interaction with the handle. If the user has not moved the handle, it will return the same value as you passed into the function. 
### Description
Make a Scene view scale handle.
This will behave like the built-in scale tool  
  
**Note:** Use [HandleUtility.GetHandleSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.GetHandleSize.html) where you might want to have constant screen-sized handles.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/ScaleHandle.png)  
_Scale handle that will appear whenever you select the GameObject._
```
// Name this script "ScaleAtPointEditor"
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
[CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)(typeof(ScaleAtPoint))]
[CanEditMultipleObjects[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanEditMultipleObjects.html)]
public class ScaleAtPointEditor : Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
{
    public void OnSceneGUI()
    {
        ScaleAtPoint t = (target as ScaleAtPoint);  
  
        EditorGUI.BeginChangeCheck[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.BeginChangeCheck.html)();
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) scale = Handles.ScaleHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.ScaleHandle.html)(t.scale, Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html), Quaternion.identity[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion-identity.html), 1);
        if (EditorGUI.EndChangeCheck[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.EndChangeCheck.html)())
        {
            Undo.RecordObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.RecordObject.html)(target, "Scaled ScaleAt Point");
            t.scale = scale;
            t.Update();
        }
    }
}

```

And the script Attached to this GameObject:
```
// Name this script "ScaleAtPoint"
using UnityEngine;
[ExecuteInEditMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ExecuteInEditMode.html)]
public class ScaleAtPoint : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) scale = Vector3.one[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-one.html);
    public void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        transform.localScale = scale;
    }
}

```

* * *
