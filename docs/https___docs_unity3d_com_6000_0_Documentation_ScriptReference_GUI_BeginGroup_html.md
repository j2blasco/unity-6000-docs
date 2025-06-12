* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.BeginGroup.html

#  [GUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html).BeginGroup
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
public static void BeginGroup([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position); 
## Declaration
public static void BeginGroup([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, string text); 
## Declaration
public static void BeginGroup([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) image); 
## Declaration
public static void BeginGroup([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) content); 
## Declaration
public static void BeginGroup([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style); 
## Declaration
public static void BeginGroup([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, string text, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style); 
## Declaration
public static void BeginGroup([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) image, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style); 
## Declaration
public static void BeginGroup([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) content, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style); 
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to use for the group.  
text | Text to display on the group.  
image |  [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) to display on the group.  
content | Text, image and tooltip for this group. If supplied, any mouse clicks are "captured" by the group and not If left out, no background is rendered, and mouse clicks are passed.  
style | The style to use for the background.  
### Description
Begin a group. Must be matched with a call to [EndGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.EndGroup.html).
When you begin a group, the coordinate system for GUI controls are set so (0,0) is the top-left corner of the group. All controls are clipped to the group. Groups can be nested - if they are, children are clipped to their parents.  
  
This is very useful when moving a bunch of GUI elements around on screen. A common use case is designing your menus to fit on a specific screen size, then centering the GUI on larger displays. Additional resources: [matrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-matrix.html), [BeginScrollView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.BeginScrollView.html).
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnGUI()
    {
        // Constrain all drawing to be within a 800x600 pixel area centered on the screen.
        GUI.BeginGroup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.BeginGroup.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(Screen.width[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-width.html) / 2 - 400, Screen.height[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-height.html) / 2 - 300, 800, 600));  
  
        // Draw a box in the new coordinate space defined by the BeginGroup.
        // Notice how (0,0) has now been moved on-screen
        GUI.Box[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Box.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 800, 600), "This box is now centered! - here you would put your main menu");  
  
        // We need to match all BeginGroup calls with an EndGroup
        GUI.EndGroup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.EndGroup.html)();
    }
}

```

* * *
