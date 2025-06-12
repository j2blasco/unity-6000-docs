* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.BoundsField.html

#  [EditorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.html).BoundsField
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
public static [Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) BoundsField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) value); 
## Declaration
public static [Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) BoundsField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, [Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) value); 
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to use for the field.  
label | Optional label to display above the field.  
value | The value to edit.  
### Returns
**Bounds** The value entered by the user. 
### Description
Makes Center and Extents field for entering a [Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html).
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorGUIBoundsField.png)   
_Bounds field in an Editor Window._  
  
See also [Extending the editor](https://docs.unity3d.com/6000.0/Documentation/Manual/ExtendingTheEditor.html).
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  

// Simple script that shows radius of bounds of selected MeshFilter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html)  
  
class EditorGUILayoutBoundsField : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    float radius = 0;
    Bounds[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) bounds;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Show Radius of mesh bounds")]
    static void Init()
    {
        var window = GetWindow<EditorGUILayoutBoundsField>();
        window.Show();
    }  
  
    void OnGUI()
    {
        GUILayout.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Label.html)("Select a mesh in the Hierarchy[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Hierarchy.Hierarchy.html) view and click 'Capture Bounds[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html)'");
        EditorGUILayout.BeginHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.BeginHorizontal.html)();
        bounds = EditorGUILayout.BoundsField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.BoundsField.html)("Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) bounds:", bounds);  
  
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Capture Bounds[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html)") && Selection.activeTransform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeTransform.html))
        {
            MeshFilter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html) meshFilter = Selection.activeTransform.GetComponentInChildren<MeshFilter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html)>();
            if (meshFilter)
            {
                bounds = meshFilter.sharedMesh.bounds;
            }
        }
        EditorGUILayout.EndHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.EndHorizontal.html)();  
  
        EditorGUILayout.LabelField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.LabelField.html)("Radius:", bounds.size.magnitude.ToString());
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Close"))
        {
            this.Close();
        }
    }
}

```

* * *
