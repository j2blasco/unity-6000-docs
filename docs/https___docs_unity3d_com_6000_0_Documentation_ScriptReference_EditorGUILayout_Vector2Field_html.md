* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Vector2Field.html

#  [EditorGUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.html).Vector2Field
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
public static [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) Vector2Field(string label, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) value, params GUILayoutOption[] options); 
## Declaration
public static [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) Vector2Field([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) value, params GUILayoutOption[] options); 
### Parameters
Parameter | Description  
---|---  
label | Label to display above the field.  
value | The value to edit.  
options | An optional list of layout options that specify extra layout properties. Any values passed in here will override settings defined by the `style`.  
  
### Returns
**Vector2** The value entered by the user. 
### Description
Make an X & Y field for entering a [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html).
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorGUILayoutVector2Field.png)   
_Measure the distance between 2 points._
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class EditorGUILayoutVector2Field : UnityEditor.EditorWindow
{
    float distance = 0f;
    Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) p1;
    Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) p2;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Measure Distance")]
    static void Init()
    {
        EditorGUILayoutVector2Field window = (EditorGUILayoutVector2Field)EditorWindow.GetWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindow.html)(typeof(EditorGUILayoutVector2Field), true, "My Empty Window");
        window.Show();
    }  
  
    void OnGUI()
    {
        p1 = EditorGUILayout.Vector2Field[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Vector2Field.html)("Point 1:", p1);
        p2 = EditorGUILayout.Vector2Field[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Vector2Field.html)("Point 2:", p2);
        EditorGUILayout.LabelField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.LabelField.html)("Distance:", distance.ToString());
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Close"))
            this.Close();
    }  
  
    void OnInspectorUpdate()
    {
        distance = Vector2.Distance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.Distance.html)(p1, p2);
        this.Repaint();
    }
}

```

* * *
