* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.TextField.html

#  [GUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html).TextField
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
public static string TextField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, string text); 
## Declaration
public static string TextField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, string text, int maxLength); 
## Declaration
public static string TextField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, string text, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style); 
## Declaration
public static string TextField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, string text, int maxLength, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style); 
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to use for the text field.  
text | Text to edit. The return value of this function should be assigned back to the string as shown in the example.  
maxLength | The maximum length of the string. If left out, the user can type for ever and ever.  
style | The style to use. If left out, the `textField` style from the current [GUISkin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISkin.html) is used.  
### Returns
**string** The edited string. 
### Description
Make a single-line text field where the user can edit a string.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public string stringToEdit = "Hello World";  
  
    void OnGUI()
    {
        // Make a text field that modifies stringToEdit.
        stringToEdit = GUI.TextField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.TextField.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 10, 200, 20), stringToEdit, 25);
    }
}

```

* * *
