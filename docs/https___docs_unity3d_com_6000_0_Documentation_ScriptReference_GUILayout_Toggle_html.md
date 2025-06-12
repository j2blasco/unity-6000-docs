* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Toggle.html

#  [GUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.html).Toggle
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
public static bool Toggle(bool value, [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) image, params GUILayoutOption[] options); 
## Declaration
public static bool Toggle(bool value, string text, params GUILayoutOption[] options); 
## Declaration
public static bool Toggle(bool value, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) content, params GUILayoutOption[] options); 
## Declaration
public static bool Toggle(bool value, [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) image, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
## Declaration
public static bool Toggle(bool value, string text, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
## Declaration
public static bool Toggle(bool value, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) content, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
### Parameters
Parameter | Description  
---|---  
value | Is the button on or off?  
text | Text to display on the button.  
image |  [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) to display on the button.  
content | Text, image and tooltip for this button.  
style | The style to use. If left out, the `button` style from the current [GUISkin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISkin.html) is used.  
options | An optional list of layout options that specify extra layouting properties. Any values passed in here will override settings defined by the `style`.  
Additional resources: [GUILayout.Width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Width.html), [GUILayout.Height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Height.html), [GUILayout.MinWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinWidth.html), [GUILayout.MaxWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxWidth.html), [GUILayout.MinHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinHeight.html), [GUILayout.MaxHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxHeight.html), [GUILayout.ExpandWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandWidth.html), [GUILayout.ExpandHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandHeight.html).  
### Returns
**bool** The new value of the button. 
### Description
Make an on/off toggle button.
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/GUILayoutToggle.png)   
_Toggle button in the Game View._
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Draws 2 toggle controls, one with a text, the other with an image.
    Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) aTexture;  
  
    bool toggleTxt = false;
    bool toggleImg = false;  
  
    void OnGUI()
    {
        if (!aTexture)
        {
            Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)("Please assign a texture in the inspector.");
            return;
        }
        toggleTxt = GUILayout.Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Toggle.html)(toggleTxt, "A Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Toggle.html) text");
        toggleImg = GUILayout.Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Toggle.html)(toggleImg, aTexture);
    }
}

```

* * *
