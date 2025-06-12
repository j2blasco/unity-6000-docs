* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.GradientField.html

#  [EditorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.html).GradientField
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
public static [Gradient](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html) GradientField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [Gradient](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html) gradient); 
## Declaration
public static [Gradient](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html) GradientField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, string label, [Gradient](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html) gradient); 
## Declaration
public static [Gradient](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html) GradientField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, [Gradient](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html) gradient); 
## Declaration
public static [Gradient](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html) GradientField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, [Gradient](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html) gradient, bool hdr); 
## Declaration
public static [Gradient](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html) GradientField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, [Gradient](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html) gradient, bool hdr, [ColorSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColorSpace.html) colorSpace); 
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to use for the field.  
label | Optional label to display in front of the field.  
gradient | The gradient to edit.  
hdr | Display the HDR Gradient Editor.  
colorSpace | Display the gradient and Gradient Editor in this color space.  
### Returns
**Gradient** The gradient edited by the user. 
### Description
Makes a field for editing a [Gradient](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html).
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
        gradient = EditorGUI.GradientField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.GradientField.html)(
            new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(3, 3, position.width - 6, 50), "Gradient[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html)", gradient);
    }
}

```

* * *
