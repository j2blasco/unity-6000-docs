* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.ToggleLeft.html

#  [EditorGUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.html).ToggleLeft
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
public static bool ToggleLeft(string label, bool value, params GUILayoutOption[] options); 
## Declaration
public static bool ToggleLeft([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, bool value, params GUILayoutOption[] options); 
## Declaration
public static bool ToggleLeft(string label, bool value, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) labelStyle, params GUILayoutOption[] options); 
## Declaration
public static bool ToggleLeft([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, bool value, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) labelStyle, params GUILayoutOption[] options); 
### Parameters
Parameter | Description  
---|---  
label | Label to display next to the toggle.  
value | The value to edit.  
labelStyle | Optional [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) to use for the label.  
options | An optional list of layout options that specify extra layout properties. Any values passed in here will override settings defined by the `style`.  
Additional resources: [GUILayout.Width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Width.html), [GUILayout.Height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Height.html), [GUILayout.MinWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinWidth.html), [GUILayout.MaxWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxWidth.html), [GUILayout.MinHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinHeight.html), [GUILayout.MaxHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxHeight.html), [GUILayout.ExpandWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandWidth.html), [GUILayout.ExpandHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandHeight.html).  
### Description
Make a toggle field where the toggle is to the left and the label immediately to the right of it.
[EditorGUILayout.ToggleLeft](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.ToggleLeft.html) is similar to [GUILayout.Toggle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Toggle.html) but respects the [EditorGUI.showMixedValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI-showMixedValue.html) property and handles keyboard focus consistent with other Editor controls. [EditorGUILayout.ToggleLeft](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.ToggleLeft.html) has the label close and to the left of the toggle. (The [EditorGUILayout.Toggle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Toggle.html) has the opposite with the label at a distance from the toggle and to the right.) 
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorGUILayoutToggleLeft.png)   
_Show a button if the toggle control is selected._
```
// Creates a new menu in the Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) called "Examples" with a new menu item called "ToggleLeft example"  
  
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class Example : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    bool showBtn = true;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/ToggleLeft example")]
    static void Init()
    {
        Example window = (Example)EditorWindow.GetWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindow.html)(typeof(Example), true, "ToggleLeft example");
        window.Show();
    }  
  
    void OnGUI()
    {
        showBtn = EditorGUILayout.ToggleLeft[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.ToggleLeft.html)("Show Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)", showBtn);
        if (showBtn)
        {
            if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Close"))
            {
                this.Close();
            }
        }
    }
}

```

* * *
