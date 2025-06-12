* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Window.html

#  [GUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.html).Window
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
public static [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) Window(int id, [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) screenRect, [GUI.WindowFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.WindowFunction.html) func, string text, params GUILayoutOption[] options); 
## Declaration
public static [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) Window(int id, [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) screenRect, [GUI.WindowFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.WindowFunction.html) func, [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) image, params GUILayoutOption[] options); 
## Declaration
public static [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) Window(int id, [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) screenRect, [GUI.WindowFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.WindowFunction.html) func, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) content, params GUILayoutOption[] options); 
## Declaration
public static [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) Window(int id, [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) screenRect, [GUI.WindowFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.WindowFunction.html) func, string text, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
## Declaration
public static [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) Window(int id, [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) screenRect, [GUI.WindowFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.WindowFunction.html) func, [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) image, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
## Declaration
public static [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) Window(int id, [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) screenRect, [GUI.WindowFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.WindowFunction.html) func, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) content, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
### Parameters
Parameter | Description  
---|---  
id | A unique ID to use for each window. This is the ID you'll use to interface to it.  
screenRect | Rectangle on the screen to use for the window. The layouting system will attempt to fit the window inside it - if that cannot be done, it will adjust the rectangle to fit.  
func | The function that creates the GUI `inside` the window. This function must take one parameter - the `id` of the window it's currently making GUI for.  
text | Text to display as a title for the window.  
image |  [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) to display an image in the titlebar.  
content | Text, image and tooltip for this window.  
style | An optional style to use for the window. If left out, the `window` style from the current [GUISkin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISkin.html) is used.  
options | An optional list of layout options that specify extra layouting properties. Any values passed in here will override settings defined by the `style` or the `screenRect` you pass in.  
Additional resources: [GUILayout.Width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Width.html), [GUILayout.Height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Height.html), [GUILayout.MinWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinWidth.html), [GUILayout.MaxWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxWidth.html), [GUILayout.MinHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinHeight.html), [GUILayout.MaxHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxHeight.html), [GUILayout.ExpandWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandWidth.html), [GUILayout.ExpandHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandHeight.html).  
### Returns
**Rect** The rectangle the window is at. This can be in a different position and have a different size than the one you passed in. 
### Description
Make a popup window that layouts its contents automatically.
Windows float above normal GUI controls, feature click-to-focus and can optionally be dragged around by the end user. Unlike other controls, you need to pass them a separate function for the GUI controls to put inside the window. Here is a small example to get you started:  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/GUILayoutWindow.png)  
_Window in the Game View._
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) windowRect = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(20, 20, 120, 50);  
  
    void OnGUI()
    {
        // Register the window. Notice the 3rd parameter
        windowRect = GUILayout.Window[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Window.html)(0, windowRect, DoMyWindow, "My Window");
    }  
  
    // Make the contents of the window
    void DoMyWindow(int windowID)
    {
        // This button will size to fit the window
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Hello World"))
        {
            print("Got a click");
        }
    }
}

```

The screen rectangle you pass in to the function only acts as a guide. To Apply extra limits to the window, pass in some extra layout options. The ones applied here will override the size calculated. Here is a small example:
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) windowRect = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(20, 20, 120, 50);  
  
    void OnGUI()
    {
        // Register the window. Here we instruct the layout system to
        // make the window 100 pixels wide no matter what.
        windowRect = GUILayout.Window[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Window.html)(0, windowRect, DoMyWindow, "My Window", GUILayout.Width[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Width.html)(100));
    }  
  
    // Make the contents of the window
    void DoMyWindow(int windowID)
    {
        // This button is too large to fit the window
        // Normally, the window would have been expanded to fit the button, but due to
        // the GUILayout.Width[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Width.html) call above the window will only ever be 100 pixels wide
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Please click me a lot"))
        {
            print("Got a click");
        }
    }
}

```

* * *
