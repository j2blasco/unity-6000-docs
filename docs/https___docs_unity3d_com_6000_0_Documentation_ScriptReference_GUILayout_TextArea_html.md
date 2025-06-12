* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.TextArea.html

#  [GUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.html).TextArea
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
public static string TextArea(string text, int maxLength, params GUILayoutOption[] options); 
## Declaration
public static string TextArea(string text, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
## Declaration
public static string TextArea(string text, int maxLength, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
### Parameters
Parameter | Description  
---|---  
text | Text to edit. The return value of this function should be assigned back to the string as shown in the example.  
maxLength | The maximum length of the string. If left out, the user can type for ever and ever.  
style | The style to use. If left out, the `textField` style from the current [GUISkin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISkin.html) is used.  
options | An optional list of layout options that specify extra layouting properties. Any values passed in here will override settings defined by the `style`.&amp;lt;br&amp;gt; Additional resources: [GUILayout.Width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Width.html), [GUILayout.Height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Height.html), [GUILayout.MinWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinWidth.html), [GUILayout.MaxWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxWidth.html), [GUILayout.MinHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinHeight.html), [GUILayout.MaxHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxHeight.html), [GUILayout.ExpandWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandWidth.html), [GUILayout.ExpandHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandHeight.html).  
### Returns
**string** The edited string. 
### Description
Make a multi-line text field where the user can edit a string.
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/GUILayoutTextArea.png)   
_Text area in the Game View._
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    string stringToEdit = "Hello World\nI've got 2 lines...";  
  
    void OnGUI()
    {
        // Make a multiline text area that modifies stringToEdit.
        stringToEdit = GUILayout.TextArea[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.TextArea.html)(stringToEdit, 200);
    }
}

```

* * *
