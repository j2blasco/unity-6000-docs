* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.GradientField.html

#  [EditorGUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.html).GradientField
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
public static [Gradient](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html) GradientField([Gradient](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html) value, params GUILayoutOption[] options); 
## Declaration
public static [Gradient](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html) GradientField(string label, [Gradient](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html) value, params GUILayoutOption[] options); 
## Declaration
public static [Gradient](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html) GradientField([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, [Gradient](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html) value, params GUILayoutOption[] options); 
## Declaration
public static [Gradient](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html) GradientField([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, [Gradient](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html) value, bool hdr, params GUILayoutOption[] options); 
### Parameters
Parameter | Description  
---|---  
label | Optional label to display in front of the field.  
value | The gradient to edit.  
options | An optional list of layout options that specify extra layout properties. Any values passed in here will override settings defined by the `style`.  
Additional resources: [GUILayout.Width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Width.html), [GUILayout.Height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Height.html), [GUILayout.MinWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinWidth.html), [GUILayout.MaxWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxWidth.html), [GUILayout.MinHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinHeight.html), [GUILayout.MaxHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxHeight.html), [GUILayout.ExpandWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandWidth.html), [GUILayout.ExpandHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandHeight.html).  
### Returns
**Gradient** The gradient edited by the user. 
### Description
Make a field for editing a [Gradient](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html).
```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class EditorGUIGradientField : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    Gradient[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html) gradient = new Gradient[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html)();  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Gradient[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html) Field demo")]
    static void Init()
    {
        EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html) window = GetWindow(typeof(EditorGUIGradientField));
        window.position = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 400, 199);
        window.Show();
    }  
  
    void OnGUI()
    {
        gradient = EditorGUILayout.GradientField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.GradientField.html)(
            "Gradient[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html)", gradient);
    }
}

```

* * *
