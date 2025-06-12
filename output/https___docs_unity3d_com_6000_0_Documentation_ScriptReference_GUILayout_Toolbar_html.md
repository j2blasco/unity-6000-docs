* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Toolbar.html

#  [GUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.html).Toolbar
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
public static int Toolbar(int selected, string[] texts, params GUILayoutOption[] options); 
## Declaration
public static int Toolbar(int selected, Texture[] images, params GUILayoutOption[] options); 
## Declaration
public static int Toolbar(int selected, GUIContent[] contents, params GUILayoutOption[] options); 
## Declaration
public static int Toolbar(int selected, string[] texts, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
## Declaration
public static int Toolbar(int selected, Texture[] images, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
## Declaration
public static int Toolbar(int selected, GUIContent[] contents, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
## Declaration
public static int Toolbar(int selected, string[] texts, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, [GUI.ToolbarButtonSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.ToolbarButtonSize.html) buttonSize, params GUILayoutOption[] options); 
## Declaration
public static int Toolbar(int selected, Texture[] images, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, [GUI.ToolbarButtonSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.ToolbarButtonSize.html) buttonSize, params GUILayoutOption[] options); 
## Declaration
public static int Toolbar(int selected, GUIContent[] contents, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, [GUI.ToolbarButtonSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.ToolbarButtonSize.html) buttonSize, params GUILayoutOption[] options); 
### Parameters
Parameter | Description  
---|---  
selected | The index of the selected button.  
texts | An array of strings to show on the buttons.  
images | An array of textures on the buttons.  
contents | An array of text, image and tooltips for the button.  
style | The style to use. If left out, the `button` style from the current [GUISkin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISkin.html) is used.  
options | An optional list of layout options that specify extra layouting properties. Any values passed in here will override settings defined by the `style`.  
Additional resources: [GUILayout.Width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Width.html), [GUILayout.Height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Height.html), [GUILayout.MinWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinWidth.html), [GUILayout.MaxWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxWidth.html), [GUILayout.MinHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinHeight.html), [GUILayout.MaxHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxHeight.html), [GUILayout.ExpandWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandWidth.html), [GUILayout.ExpandHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandHeight.html).  
buttonSize | Determines how toolbar button size is calculated.  
### Returns
**int** The index of the selected button. 
### Description
Make a toolbar.
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/GUILayoutToolbar.png)   
_Toolbar in the Game View._
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    int toolbarInt = 0;
    string[] toolbarStrings = {"Toolbar1", "Toolbar2", "Toolbar3"};  
  
    void OnGUI()
    {
        toolbarInt = GUILayout.Toolbar[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Toolbar.html)(toolbarInt, toolbarStrings);
    }
}

```

* * *
