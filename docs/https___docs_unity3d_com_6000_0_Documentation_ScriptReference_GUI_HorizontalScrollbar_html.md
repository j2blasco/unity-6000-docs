* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.HorizontalScrollbar.html

#  [GUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html).HorizontalScrollbar
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
public static float HorizontalScrollbar([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, float value, float size, float leftValue, float rightValue); 
## Declaration
public static float HorizontalScrollbar([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, float value, float size, float leftValue, float rightValue, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style); 
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to use for the scrollbar.  
value | The position between min and max.  
size | How much can we see?  
leftValue | The value at the left end of the scrollbar.  
rightValue | The value at the right end of the scrollbar.  
style | The style to use for the scrollbar background. If left out, the `horizontalScrollbar` style from the current [GUISkin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISkin.html) is used.  
### Returns
**float** The modified value. This can be changed by the user by dragging the scrollbar, or clicking the arrows at the end. 
### Description
Make a horizontal scrollbar. Scrollbars are what you use to scroll through a document. Most likely, you want to use scrollViews instead.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public float hSbarValue;  
  
    void OnGUI()
    {
        hSbarValue = GUI.HorizontalScrollbar[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.HorizontalScrollbar.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(25, 25, 100, 30), hSbarValue, 1.0F, 0.0F, 10.0F);
    }
}

```

**Finding extra elements:**   
  
The styles of the buttons at the end of the scrollbar are searched for in the current skin by adding "leftbutton" and "rightbutton" to the style name. The name of the scrollbar thumb (the thing you drag) is found by appending "thumb" to the style name.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public float scrollPos = 0.5f;  
  
    // This will use the following style names to determine the size / placement of the buttons
    // MyScrollbarleftbutton    - Name of style used for the left button.
    // MyScrollbarrightbutton - Name of style used for the right button.
    // MyScrollbarthumb         - Name of style used for the draggable thumb.
    void OnGUI()
    {
        scrollPos = GUI.HorizontalScrollbar[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.HorizontalScrollbar.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 100, 20),  scrollPos, 1.0f, 0.0f, 100.0f, "Scroll");
    }
}

```

* * *
