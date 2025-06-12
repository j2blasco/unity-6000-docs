* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.CreateEditor.html

#  [Editor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html).CreateEditor
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
public static [Editor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) CreateEditor([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) targetObject, Type editorType = null); 
## Declaration
public static [Editor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) CreateEditor(Object[] targetObjects, Type editorType = null); 
### Parameters
Parameter | Description  
---|---  
objects | All objects must be of the same type.  
### Description
Make a custom editor for `targetObject` or `targetObjects`.
By default, an appropriate editor with a matching CustomEditor attribute is created. If an editorType is specified, an editor of that type is created instead. Use this if you have created multiple custom editors, and each editor shows different properties of the object. Returns NULL if `objects` are of different types or if no approprate editor was found. Editors created using this function have to be destroyed explicitly, using either [Object.Destroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Destroy.html) or [Object.DestroyImmediate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DestroyImmediate.html).  
  
Consider a script WaypointPathEditor for editing the Transforms of a wayPoint array.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using System.Collections;  
  

[CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)(typeof(WaypointPath))]
public class WaypointPathEditor : Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
{
    Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) currentTransformEditor;
    Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) selectedTransform;
    string[] optionsList;
    int index = 0;
    WaypointPath myWayPath;  
  
    void GetWaypoints()
    {
        myWayPath = target as WaypointPath;  
  
        if (myWayPath.wayPointArray != null)
        {
            optionsList = new string[myWayPath.wayPointArray.Length];  
  
            for (int i = 0; i < optionsList.Length; i++)
            {
                Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) wayPoint = myWayPath.wayPointArray[i];  
  
                if (wayPoint != null)
                    optionsList[i] = wayPoint.name;
                else
                    optionsList[i] = $"Empty waypoint {(i + 1)}";
            }
        }
    }  
  
    public override void OnInspectorGUI()
    {
        GetWaypoints ();
        DrawDefaultInspector ();
        EditorGUILayout.Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Space.html) ();
        EditorGUI.BeginChangeCheck[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.BeginChangeCheck.html) ();  
  
        if (optionsList != null)
            index = EditorGUILayout.Popup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Popup.html) ("Select Waypoint", index, optionsList);  
  
        if (EditorGUI.EndChangeCheck[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.EndChangeCheck.html)())
        {
            Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) tmpEditor = null;  
  
            if (index < myWayPath.wayPointArray.Length)
            {
                selectedTransform = myWayPath.wayPointArray[index];  
  
                //Creates an Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) for selected Component[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html) from a Popup
                tmpEditor = Editor.CreateEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.CreateEditor.html)(selectedTransform);
            } else {
                selectedTransform = null;
            }  
  
            // If there isn't a Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) currently selected then destroy the existing editor
            if (currentTransformEditor != null)
            {
                DestroyImmediate (currentTransformEditor);
            }  
  
            currentTransformEditor = tmpEditor;
        }  
  
        // Shows the created Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) beneath CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)
        if (currentTransformEditor != null && selectedTransform != null)
        {
            currentTransformEditor.OnInspectorGUI ();
        }
    }
}

```

The script attached to a waypath GameObject:
```
using UnityEngine;
using System.Collections;  
  
// Note: this is not an editor script.
public class WaypointPath : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html)[] wayPointArray;
}

```

* * *
