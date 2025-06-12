* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Vector3Field.html

#  [EditorGUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.html).Vector3Field
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
public static [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) Vector3Field(string label, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) value, params GUILayoutOption[] options); 
## Declaration
public static [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) Vector3Field([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) value, params GUILayoutOption[] options); 
### Parameters
Parameter | Description  
---|---  
label | Label to display above the field.  
value | The value to edit.  
options | An optional list of layout options that specify extra layout properties. Any values passed in here will override settings defined by the `style`.  
Additional resources: [GUILayout.Width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Width.html), [GUILayout.Height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Height.html), [GUILayout.MinWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinWidth.html), [GUILayout.MaxWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxWidth.html), [GUILayout.MinHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinHeight.html), [GUILayout.MaxHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxHeight.html), [GUILayout.ExpandWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandWidth.html), [GUILayout.ExpandHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandHeight.html).  
### Returns
**Vector3** The value entered by the user. 
### Description
Make an X, Y & Z field for entering a [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html).
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorGUILayoutVector3Field.png)   
_Measure the distance between 2 GameObjects or 2 positions in 3D space._
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class EditorGUILayoutVector3Field : UnityEditor.EditorWindow
{
    float distance = 0f;
    Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) obj1;
    Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) obj2;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Measure Distance between 2 objects")]
    static void Init()
    {
        EditorGUILayoutVector3Field window = (EditorGUILayoutVector3Field)EditorWindow.GetWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindow.html)(typeof(EditorGUILayoutVector3Field), true, "My Empty Window");
        window.Show();
    }  
  
    void OnGUI()
    {
        GUILayout.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Label.html)("Select an object in the Hierarchy[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Hierarchy.Hierarchy.html) view and click 'Capture Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Position.html)'");
        EditorGUILayout.BeginHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.BeginHorizontal.html)();
        obj1 = EditorGUILayout.Vector3Field[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Vector3Field.html)("GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) 1:", obj1);
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Capture Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Position.html)"))
            obj1 = Selection.activeTransform.position;
        EditorGUILayout.EndHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.EndHorizontal.html)();  
  
        EditorGUILayout.BeginHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.BeginHorizontal.html)();
        obj2 = EditorGUILayout.Vector3Field[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Vector3Field.html)("GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) 2:", obj2);
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Capture Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Position.html)"))
            obj2 = Selection.activeTransform.position;
        EditorGUILayout.EndHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.EndHorizontal.html)();
        EditorGUILayout.LabelField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.LabelField.html)("Distance:", distance.ToString());
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Close"))
            this.Close();
    }  
  
    void OnInspectorUpdate()
    {
        distance = Vector3.Distance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Distance.html)(obj1, obj2);
        this.Repaint();
    }
}

```

* * *
