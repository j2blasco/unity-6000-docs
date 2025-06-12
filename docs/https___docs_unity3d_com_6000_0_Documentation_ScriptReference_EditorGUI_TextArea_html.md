* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.TextArea.html

#  [EditorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.html).TextArea
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
public static string TextArea([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, string text, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.textField); 
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to use for the text field.  
text | The text to edit.  
style | Optional [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html).  
### Returns
**string** The text entered by the user. 
### Description
Makes a text area.
This works just like [GUI.TextArea](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.TextArea.html), but correctly responds to select all, copy, paste etc. in the editor.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorGUITextArea.png)  
_Text Area in an Editor Window._
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
// Create a window where you can have notes
// This doesnt preserve the notes between sessions.
//
// check EditorPrefs[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.html) Get/SetString to save the notes.  
  
class EditorGUITextArea : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    string note = "Notes:\n->";  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Notes")]
    static void Init()
    {
        EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html) window = GetWindow<EditorGUITextArea>();
        window.position = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 350, 70);
        window.Show();
    }  
  
    void OnGUI()
    {
        note = EditorGUI.TextArea[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.TextArea.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(3, 3, position.width - 6, position.height - 35), note);
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, position.height - 30, position.width, 25), "Close"))
        {
            this.Close();
        }
    }
}

```

* * *
