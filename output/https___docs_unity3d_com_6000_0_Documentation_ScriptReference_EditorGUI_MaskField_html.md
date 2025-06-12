* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.MaskField.html

#  [EditorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.html).MaskField
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
public static int MaskField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, int mask, string[] displayedOptions, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.popup); 
## Declaration
public static int MaskField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, string label, int mask, string[] displayedOptions, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.popup); 
## Declaration
public static int MaskField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, int mask, string[] displayedOptions, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.popup); 
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to use for this control.  
label | Label for the field.  
mask | The current mask to display.  
displayedOption | A string array containing the labels for each flag.  
style | Optional [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html).  
displayedOptions | A string array containing the labels for each flag.  
### Returns
**int** The value modified by the user. 
### Description
Makes a field for masks.
**Note:** The mask values for the flags associated with each option in the menu will be consecutive powers of 2 starting with 1, i.e. 1, 2, 4, 8, 16, and so on.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/MaskField.png)  
_Simple window that shows the mask field._
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
class SimpleMaskUsage : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    int flags = 0;
    string[] options = { "CanJump", "CanShoot", "CanSwim" };  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Mask Field Usage")]
    static void Init()
    {
        var window = GetWindow<SimpleMaskUsage>();
        window.Show();
    }  
  
    void OnGUI()
    {
        flags = EditorGUI.MaskField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.MaskField.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 300, 20), "Player Flags[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.Flags.html)", flags, options);
    }
}

```

* * *
