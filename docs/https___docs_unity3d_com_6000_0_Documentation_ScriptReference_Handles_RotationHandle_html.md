* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.RotationHandle.html

#  [Handles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.html).RotationHandle
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
public static [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) RotationHandle([Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position); 
## Declaration
public static [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) RotationHandle([Handles.RotationHandleIds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.RotationHandleIds.html) ids, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position); 
### Parameters
Parameter | Description  
---|---  
rotation | The orientation of the handle in 3D space.  
position | The center of the handle in 3D space.  
ids | The control IDs of the handles. Use RotationHandleIds.default.  
### Returns
**Quaternion** The new rotation value modified by the user's interaction with the handle. If the user has not moved the handle, it will return the same value as you passed into the function. 
### Description
Make a Scene view rotation handle.
This will behave like the built-in rotation tool in Unity. If you have assigned something to Undo.SetSnapshotTarget, it will work fully with Undo. **Note:** Use [HandleUtility.GetHandleSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.GetHandleSize.html) where you might want to have constant screen-sized handles.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/RotationHandle.png)  
_Rotate the attached object from the Rotation Handle._
```
// Name this script "RotateAtPointEditor"
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
[CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)(typeof(RotateAtPoint))]
[CanEditMultipleObjects[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanEditMultipleObjects.html)]
public class RotateAtPointEditor : Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
{
    public void OnSceneGUI()
    {
        RotateAtPoint t = (target as RotateAtPoint);  
  
        EditorGUI.BeginChangeCheck[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.BeginChangeCheck.html)();
        Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rot = Handles.RotationHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.RotationHandle.html)(t.rot, Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html));
        if (EditorGUI.EndChangeCheck[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.EndChangeCheck.html)())
        {
            Undo.RecordObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.RecordObject.html)(target, "Rotated RotateAt Point");
            t.rot = rot;
            t.Update();
        }
    }
}

```

And the script attached to this GameObject:
```
// Name this script "RotateAtPoint"
using UnityEngine;  
  
[ExecuteInEditMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ExecuteInEditMode.html)]
public class RotateAtPoint : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rot = Quaternion.identity[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion-identity.html);
    public void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        transform.rotation = rot;
    }
}

```

* * *
