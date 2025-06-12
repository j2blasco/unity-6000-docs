* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.MaskField.html

#  [EditorGUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.html).MaskField
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
public static int MaskField([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, int mask, string[] displayedOptions, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
## Declaration
public static int MaskField(string label, int mask, string[] displayedOptions, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
## Declaration
public static int MaskField([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, int mask, string[] displayedOptions, params GUILayoutOption[] options); 
## Declaration
public static int MaskField(string label, int mask, string[] displayedOptions, params GUILayoutOption[] options); 
## Declaration
public static int MaskField(int mask, string[] displayedOptions, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
## Declaration
public static int MaskField(int mask, string[] displayedOptions, params GUILayoutOption[] options); 
### Parameters
Parameter | Description  
---|---  
label | Prefix label of the field.  
mask | The current mask to display.  
displayedOption | A string array containing the labels for each flag.  
options | An optional list of layout options that specify extra layout properties. Any values passed in here will override settings defined by the `style`.  
Additional resources: [GUILayout.Width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Width.html), [GUILayout.Height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Height.html), [GUILayout.MinWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinWidth.html), [GUILayout.MaxWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxWidth.html), [GUILayout.MinHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinHeight.html), [GUILayout.MaxHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxHeight.html), [GUILayout.ExpandWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandWidth.html), [GUILayout.ExpandHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandHeight.html).  
### Returns
**int** The value modified by the user. 
### Description
Make a field for masks.
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/MaskField.png)   
_Simple window that shows the mask field._
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class MaskFieldExample : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    static int flags = 0;
    static string[] options = new string[] {"CanJump", "CanShoot", "CanSwim"};  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Mask Field usage")]
    static void Init()
    {
        MaskFieldExample window = (MaskFieldExample)GetWindow(typeof(MaskFieldExample));
        window.Show();
    }  
  
    void OnGUI()
    {
        flags = EditorGUILayout.MaskField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.MaskField.html)("Player Flags[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.Flags.html)", flags, options);  
  
        // Display[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display.html) the flags in disabled toggles
        GUI.enabled[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-enabled.html) = false;
        for (var i = 0; i < options.Length; i++)
        {
            var value = (flags & (1 << i)) != 0;
            EditorGUILayout.Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Toggle.html)(options[i], value);
        }
        GUI.enabled[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-enabled.html) = true;
    }
}

```

* * *
