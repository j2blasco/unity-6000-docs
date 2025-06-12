* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.TextField.html

#  [EditorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.html).TextField
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
public static string TextField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, string text, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.textField); 
## Declaration
public static string TextField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, string label, string text, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.textField); 
## Declaration
public static string TextField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, string text, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.textField); 
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to use for the text field.  
label | Optional label to display in front of the text field.  
text | The text to edit.  
style | Optional [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html).  
### Returns
**string** The text entered by the user. 
### Description
Makes a text field.
This works just like [GUI.TextField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.TextField.html), but correctly responds to select all, copy, paste etc. in the editor, and it can have an optional label in front.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorGUITextField.png)  
_Text field in an Editor Window._
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
// Changes the name of the selected Objects to the one typed in the text field  
  
class EditorGUITextField : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    string objNames = "";  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Bulk Name change")]
    static void Init()
    {
        var window = GetWindow<EditorGUITextField>();
        window.Show();
    }  
  
    void OnGUI()
    {
        EditorGUI.DropShadowLabel[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.DropShadowLabel.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, position.width, 20),
            "Select the objects to rename.");  
  
        objNames = EditorGUI.TextField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.TextField.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 25, position.width - 20, 20),
            "New Names:",
            objNames);  
  
        if (Selection.activeTransform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeTransform.html))
        {
            if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 50, position.width, 30), "Bulk rename!"))
            {
                foreach (Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) t in Selection.transforms[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-transforms.html))
                {
                    t.name = objNames;
                }
            }
        }
    }  
  
    void OnInspectorUpdate()
    {
        Repaint();
    }
}

```

* * *
