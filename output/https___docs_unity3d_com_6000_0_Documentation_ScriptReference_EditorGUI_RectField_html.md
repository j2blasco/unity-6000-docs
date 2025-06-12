* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.RectField.html

#  [EditorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.html).RectField
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
public static [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) RectField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) value); 
## Declaration
public static [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) RectField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, string label, [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) value); 
## Declaration
public static [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) RectField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) value); 
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to use for the field.  
label | Optional label to display above the field.  
value | The value to edit.  
### Returns
**Rect** The value entered by the user. 
### Description
Makes an X, Y, W, and H field for entering a [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html).
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorGUIRectField.png)   
_Rect field in an Editor Window._
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
// Find all the cameras in the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) and shows all their viewports togheter  
  
class EditorGUIRectField : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)[] cameras;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) GUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html) RectField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.RectField.html) usage")]
    static void Init()
    {
        var window = GetWindow<EditorGUIRectField>();
        window.position = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 150, 120);
        window.Show();
    }  
  
    void OnGUI()
    {
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(3, 3, position.width - 6, 20), "Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html) list"))
            cameras = FindObjectsOfType<Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)>();  
  
        if (cameras.Length > 0)
        {
            for (var i = 0; i < cameras.Length; i++)
            {
                cameras[i].rect = EditorGUI.RectField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.RectField.html)(
                    new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(3, 25 + 45 * i, position.width - 6, 25),
                    cameras[i].name,
                    cameras[i].rect);
            }
        }
    }
}

```

* * *
### Description
Makes an X, Y, W, and H for Rect using SerializedProperty (not public).
* * *
