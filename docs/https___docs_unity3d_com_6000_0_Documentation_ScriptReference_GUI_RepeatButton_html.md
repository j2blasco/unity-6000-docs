* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.RepeatButton.html

#  [GUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html).RepeatButton
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
public static bool RepeatButton([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, string text); 
## Declaration
public static bool RepeatButton([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) image); 
## Declaration
public static bool RepeatButton([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) content); 
## Declaration
public static bool RepeatButton([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, string text, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style); 
## Declaration
public static bool RepeatButton([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) image, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style); 
## Declaration
public static bool RepeatButton([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) content, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style); 
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to use for the button.  
text | Text to display on the button.  
image |  [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) to display on the button.  
content | Text, image and tooltip for this button.  
style | The style to use. If left out, the `button` style from the current [GUISkin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISkin.html) is used.  
### Returns
**bool** True when the users clicks the button. 
### Description
Make a button that is active as long as the user holds it down.
```
// Draws 2 buttons, one with an image, and other with a text
// Prints a message when they get clicked.  
  
// Prints a message when they get clicked.  
  
using UnityEngine;
using System.Collections;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) btnTexture;  
  
    void OnGUI()
    {
        if (!btnTexture)
        {
            Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)("Please assign a texture on the inspector");
            return;
        }  
  
        if (GUI.RepeatButton[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.RepeatButton.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 10, 50, 50), btnTexture))
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Clicked the button with an image");  
  
        if (GUI.RepeatButton[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.RepeatButton.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 70, 50, 30), "Click"))
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Clicked the button with text");
    }
}

```

* * *
