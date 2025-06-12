* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Toggle.html

#  [GUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html).Toggle
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
public static bool Toggle([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, bool value, string text); 
## Declaration
public static bool Toggle([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, bool value, [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) image); 
## Declaration
public static bool Toggle([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, bool value, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) content); 
## Declaration
public static bool Toggle([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, bool value, string text, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style); 
## Declaration
public static bool Toggle([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, bool value, [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) image, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style); 
## Declaration
public static bool Toggle([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, bool value, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) content, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style); 
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to use for the button.  
value | Is this button on or off?  
text | Text to display on the button.  
image |  [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) to display on the button.  
content | Text, image and tooltip for this button.  
style | The style to use. If left out, the `toggle` style from the current [GUISkin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISkin.html) is used.  
### Returns
**bool** The new value of the button. 
### Description
Make an on/off toggle button.
```
// Draws 2 toggle controls, one with a text, the other with an image.  
  
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) aTexture;  
  
    private bool toggleTxt = false;
    private bool toggleImg = false;  
  
    void OnGUI()
    {
        if (!aTexture)
        {
            Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)("Please assign a texture in the inspector.");
            return;
        }  
  
        toggleTxt = GUI.Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Toggle.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 10, 100, 30), toggleTxt, "A Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Toggle.html) text");
        toggleImg = GUI.Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Toggle.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 50, 50, 50), toggleImg, aTexture);
    }
}

```

* * *
