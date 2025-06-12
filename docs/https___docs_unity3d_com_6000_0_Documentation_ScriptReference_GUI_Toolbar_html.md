* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Toolbar.html

#  [GUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html).Toolbar
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
public static int Toolbar([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, int selected, string[] texts); 
## Declaration
public static int Toolbar([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, int selected, Texture[] images); 
## Declaration
public static int Toolbar([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, int selected, GUIContent[] contents); 
## Declaration
public static int Toolbar([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, int selected, string[] texts, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style); 
## Declaration
public static int Toolbar([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, int selected, Texture[] images, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style); 
## Declaration
public static int Toolbar([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, int selected, GUIContent[] contents, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style); 
## Declaration
public static int Toolbar([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, int selected, GUIContent[] contents, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, [GUI.ToolbarButtonSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.ToolbarButtonSize.html) buttonSize); 
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to use for the toolbar.  
selected | The index of the selected button.  
texts | An array of strings to show on the toolbar buttons.  
images | An array of textures on the toolbar buttons.  
contents | An array of text, image and tooltips for the toolbar buttons.  
style | The style to use. If left out, the `button` style from the current [GUISkin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISkin.html) is used.  
buttonSize | Determines how toolbar button size is calculated.  
### Returns
**int** The index of the selected button. 
### Description
Make a toolbar.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public int toolbarInt = 0;
    public string[] toolbarStrings = new string[] {"Toolbar1", "Toolbar2", "Toolbar3"};  
  
    void OnGUI()
    {
        toolbarInt = GUI.Toolbar[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Toolbar.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(25, 25, 250, 30), toolbarInt, toolbarStrings);
    }
}

```

* * *
