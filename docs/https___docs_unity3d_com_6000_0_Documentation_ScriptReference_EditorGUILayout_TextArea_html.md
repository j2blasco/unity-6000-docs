* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.TextArea.html

#  [EditorGUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.html).TextArea
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
public static string TextArea(string text, params GUILayoutOption[] options); 
## Declaration
public static string TextArea(string text, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
### Parameters
Parameter | Description  
---|---  
text | The text to edit.  
style | Optional [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html).  
options | An optional list of layout options that specify extra layout properties. Any values passed in here will override settings defined by the `style`.  
Additional resources: [GUILayout.Width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Width.html), [GUILayout.Height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Height.html), [GUILayout.MinWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinWidth.html), [GUILayout.MaxWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxWidth.html), [GUILayout.MinHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinHeight.html), [GUILayout.MaxHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxHeight.html), [GUILayout.ExpandWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandWidth.html), [GUILayout.ExpandHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandHeight.html).  
### Returns
**string** The text entered by the user. 
### Description
Make a text area.
This works just like @@[GUILayout.TextArea](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.TextArea.html)@@ with proper responsiveness to actions like **Select all** , **Copy** , **Paste** in the Editor.  
For Undo support, see [Undo.RecordObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.RecordObject.html).  
To make the text wrap, set **EditorStyles.textField.wordWrap**.   
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorGUILayoutTextArea.png)  
_Quick script editor._
```
// Simple script that lets you visualize your scripts in an editor window
// This can be expanded to save your scripts also in the editor window.  
  
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class TextAreaExample : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    string text = "Nothing Opened...";
    TextAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset.html) txtAsset;
    Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) scroll;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/TextArea usage")]
    static void Init()
    {
        TextAreaExample window = (TextAreaExample)GetWindow(typeof(TextAreaExample), true, "EditorGUILayout.TextArea[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.TextArea.html)");
        window.Show();
    }  
  
    Object source;  
  
    void OnGUI()
    {
        source = EditorGUILayout.ObjectField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.ObjectField.html)(source, typeof(Object), true);
        TextAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset.html) newTxtAsset = (TextAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset.html))source;  
  
        if (newTxtAsset != txtAsset)
            ReadTextAsset(newTxtAsset);  
  
        scroll = EditorGUILayout.BeginScrollView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.BeginScrollView.html)(scroll, GUILayout.Height[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Height.html)(position.height - 30));
        text = EditorGUILayout.TextArea[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.TextArea.html)(text);
        EditorGUILayout.EndScrollView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.EndScrollView.html)();
    }  
  
    void ReadTextAsset(TextAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset.html) txt)
    {
        text = txt.text;
        txtAsset = txt;
    }
}

```

* * *
