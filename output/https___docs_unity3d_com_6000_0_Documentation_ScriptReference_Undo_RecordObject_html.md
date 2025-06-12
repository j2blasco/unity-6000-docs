* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.RecordObject.html

#  [Undo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.html).RecordObject
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
public static void RecordObject([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) objectToUndo, string name); 
### Parameters
Parameter | Description  
---|---  
objectToUndo | The reference to the object that you will be modifying.  
name | The title of the action to appear in the undo history (i.e. visible in the undo menu).  
### Description
Records any changes done on the object after the RecordObject function.
Almost all property changes can be recorded with this function. The transform parent, AddComponent, object destruction can not be recorded with this function, for that you should use the dedicated functions.  
  
Internally this creates a temporary copy of the object's state. At the end of the frame Unity diffs the state and detects what has changed. The changed properties are recorded on the undo stack. If nothing has changed (Binary exact comparison is used for all properties), no undo operations are stored on the stack.  
  
**Important:** To correctly handle instances where _objectToUndo_ is an instance of a Prefab, [PrefabUtility.RecordPrefabInstancePropertyModifications](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.RecordPrefabInstancePropertyModifications.html) must be called after RecordObject.  
  
This is an example of an editor script which allows you to change an effect radius variable. The Undo state is recorded, allowing you to revert the change using the undo system.
```
//Name this script "EffectRadiusEditor"
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
[CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)(typeof(EffectRadius))]
public class EffectRadiusEditor : Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
{
    public void OnSceneGUI()
    {
        EffectRadius t = (target as EffectRadius);  
  
        // The Begin and EndChangeChecks check for changes in the GUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html) state. This is not required for
        // Undo.RecordObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.RecordObject.html). Undo.RecordObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.RecordObject.html) only registers changes to the target
        // after the call to Undo.RecordObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.RecordObject.html).
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
Place this script on a GameObject to see the area of effect handle, and change the value using the gizmo in the Scene view.
```
//Name this script "EffectRadius"
using UnityEngine;
using System.Collections;  
  
public class EffectRadius : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public float areaOfEffect = 1;
}

```

Additional resources: [Undo.RecordObjects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.RecordObjects.html).
* * *
