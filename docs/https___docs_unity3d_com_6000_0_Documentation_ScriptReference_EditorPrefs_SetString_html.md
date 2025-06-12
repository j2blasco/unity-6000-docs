* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.SetString.html

#  [EditorPrefs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.html).SetString
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
public static void SetString(string key, string value); 
### Description
Sets the value of the preference identified by `key`. Note that EditorPrefs does not support null strings and will store an empty string instead.
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/QuickNotes.png)   
_Quick notes that last between Unity Sessions._
```
// Simple Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) Script that lets you create / save quick notes
// Between Unity Sessions.  
  
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class ExampleClass : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    string note = "Notes:\n->\n->";  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/QuickNotes")]
    static void Init()
    {
        ExampleClass window = (ExampleClass)EditorWindow.GetWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindow.html)(typeof(ExampleClass));
        window.Show();
    }  
  
    void OnGUI()
    {
        note = EditorGUILayout.TextArea[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.TextArea.html)(note,
            GUILayout.Width[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Width.html)(position.width - 5),
            GUILayout.Height[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Height.html)(position.height - 30));
        EditorGUILayout.BeginHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.BeginHorizontal.html)();
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Reset"))
            note = "";
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Clear Story", GUILayout.Width[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Width.html)(72)))
        {
            note = "Notes:\n->\n->";
        }
        EditorGUILayout.EndHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.EndHorizontal.html)();
    }  
  
    void OnFocus()
    {
        if (EditorPrefs.HasKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.HasKey.html)("QuickNotes"))
            note = EditorPrefs.GetString[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.GetString.html)("QuickNotes");
    }  
  
    void OnLostFocus()
    {
        EditorPrefs.SetString[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.SetString.html)("QuickNotes", note);
    }  
  
    void OnDestroy()
    {
        EditorPrefs.SetString[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.SetString.html)("QuickNotes", note);
    }
}

```

* * *
