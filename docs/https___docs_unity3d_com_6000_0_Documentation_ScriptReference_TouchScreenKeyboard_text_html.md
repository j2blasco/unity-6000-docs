* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboard-text.html

#  [TouchScreenKeyboard](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboard.html).text
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
text; 
### Description
Returns the text displayed by the input field of the keyboard.
This value can be accessed at any moment, even if user has not yet finished input process.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public string inputText = "text";
    private TouchScreenKeyboard[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboard.html) keyboard;
    // Updates button's text while user is typing
    void OnGUI()
    {
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 10, 200, 32), inputText))
            keyboard = TouchScreenKeyboard.Open[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboard.Open.html)(inputText);  
  
        if (keyboard != null)
            inputText = keyboard.text;
    }
}

```

* * *
