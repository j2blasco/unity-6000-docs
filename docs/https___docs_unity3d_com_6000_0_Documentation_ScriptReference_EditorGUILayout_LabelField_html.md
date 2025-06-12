* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.LabelField.html

#  [EditorGUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.html).LabelField
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
public static void LabelField(string label, params GUILayoutOption[] options); 
## Declaration
public static void LabelField(string label, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
## Declaration
public static void LabelField([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, params GUILayoutOption[] options); 
## Declaration
public static void LabelField([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
## Declaration
public static void LabelField(string label, string label2, params GUILayoutOption[] options); 
## Declaration
public static void LabelField(string label, string label2, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
## Declaration
public static void LabelField([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label2, params GUILayoutOption[] options); 
## Declaration
public static void LabelField([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label2, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
### Parameters
Parameter | Description  
---|---  
label | Label in front of the label field.  
label2 | The label to show to the right.  
options | An optional list of layout options that specify extra layout properties. Any values passed in here will override settings defined by the `style`.  
Additional resources: [GUILayout.Width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Width.html), [GUILayout.Height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Height.html), [GUILayout.MinWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinWidth.html), [GUILayout.MaxWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxWidth.html), [GUILayout.MinHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinHeight.html), [GUILayout.MaxHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxHeight.html), [GUILayout.ExpandWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandWidth.html), [GUILayout.ExpandHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandHeight.html).  
### Description
Make a label field. (Useful for showing read-only info.)
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorGUILayoutLabel.png)   
_Shows a label in the editor (Label) with the seconds since the editor started (Label2)._
```
// Shows a label in the editor with the seconds since the editor started
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class LabelFieldExample : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) GUILayout[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.html) Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html) Usage")]
    static void Init()
    {
        LabelFieldExample window = (LabelFieldExample)EditorWindow.GetWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindow.html)(typeof(LabelFieldExample), true, "My Empty Window");
        window.Show();
    }  
  
    void OnGUI()
    {
        EditorGUILayout.LabelField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.LabelField.html)("Time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time.html) since start: ",
            EditorApplication.timeSinceStartup.ToString());
        this.Repaint();
    }
}

```

* * *
