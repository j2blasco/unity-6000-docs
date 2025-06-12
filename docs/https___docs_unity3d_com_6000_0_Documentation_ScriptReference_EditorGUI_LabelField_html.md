* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.LabelField.html

#  [EditorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.html).LabelField
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
public static void LabelField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, string label, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.label); 
## Declaration
public static void LabelField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.label); 
## Declaration
public static void LabelField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, string label, string label2, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.label); 
## Declaration
public static void LabelField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label2, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.label); 
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to use for the label field.  
label | Label in front of the label field.  
label2 | The label to show to the right.  
style | Style information (color, etc) for displaying the label.  
### Description
Makes a label field. (Useful for showing read-only info.)
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorGUILabelField.png)   
_Shows a label in an editor window with the seconds since the editor started._
```
// Shows a label in the editor with the seconds since the editor started  
  
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using System.Collections;  
  
//Select the dependencies of the found GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
public class EditorGUIObjectField : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/EditorGUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.html) Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html) Usage")]
    static void Init()
    {
        UnityEditor.EditorWindow window = GetWindow(typeof(EditorGUIObjectField));
        window.Show();
    }  
  
    void OnGUI()
    {
        EditorGUI.LabelField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.LabelField.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(3, 3, position.width, 20),
            "Time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time.html) since start: ",
            EditorApplication.timeSinceStartup.ToString());
        this.Repaint();
    }
}

```

* * *
