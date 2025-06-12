* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.DropShadowLabel.html

#  [EditorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.html).DropShadowLabel
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
public static void DropShadowLabel([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, string text); 
## Declaration
public static void DropShadowLabel([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) content); 
## Declaration
public static void DropShadowLabel([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, string text, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style); 
## Declaration
public static void DropShadowLabel([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) content, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style); 
### Parameters
Parameter | Description  
---|---  
position | Where to show the label.  
content | Text to show @style style to use.  
### Description
Draws a label with a drop shadow.
Not superfast, so use with caution.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorGUIDropShadowLabel.png)  
_Shadow Label in and editor window._
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class EditorGUIDropShadowLabel : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    // Write some text using a Shadow Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html).
    string text = "This is some text with a Shadow Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html)";  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Shadow Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html)")]
    static void Init()
    {
        var window = GetWindow<EditorGUIDropShadowLabel>();
        window.position = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 250, 60);
        window.Show();
    }  
  
    void OnGUI()
    {
        EditorGUI.DropShadowLabel[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.DropShadowLabel.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 5, 245, 20), text);  
  
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 30, 250, 20), "Close"))
            this.Close();
    }  
  
    void OnInspectorUpdate()
    {
        Repaint();
    }
}

```

* * *
