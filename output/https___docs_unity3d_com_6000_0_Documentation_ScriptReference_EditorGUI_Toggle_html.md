* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.Toggle.html

#  [EditorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.html).Toggle
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
public static bool Toggle([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, bool value); 
## Declaration
public static bool Toggle([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, string label, bool value); 
## Declaration
public static bool Toggle([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, bool value, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style); 
## Declaration
public static bool Toggle([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, string label, bool value, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style); 
## Declaration
public static bool Toggle([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, bool value); 
## Declaration
public static bool Toggle([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, bool value, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style); 
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to use for the toggle.  
label | Optional label in front of the toggle.  
value | The shown state of the toggle.  
style | Optional [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html).  
### Returns
**bool** The selected state of the toggle. 
### Description
Makes a toggle.
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorGUIToggle.png)   
_Toggle control in an Editor Window._
```
// Use a toggle button to show/hide a button that can close the window.
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
class EditorGUIToggle : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    bool showClose =  true;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/EditorGUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.html) Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Toggle.html) usage")]
    static void Init()
    {
        EditorGUIToggle window = (EditorGUIToggle)GetWindow(typeof(EditorGUIToggle), true, "My Empty Window");
        window.Show();
    }  
  
    void OnGUI()
    {
        showClose = EditorGUI.Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.Toggle.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 5, position.width, 20),
            "Show Close Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)",
            showClose);
        if (showClose)
            if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 25, position.width, 100), "Close Window!"))
                this.Close();
    }
}

```

* * *
