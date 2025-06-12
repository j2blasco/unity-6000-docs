* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.VerticalScrollbar.html

#  [GUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html).VerticalScrollbar
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
public static float VerticalScrollbar([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, float value, float size, float topValue, float bottomValue); 
## Declaration
public static float VerticalScrollbar([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, float value, float size, float topValue, float bottomValue, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style); 
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to use for the scrollbar.  
value | The position between min and max.  
size | How much can we see?  
topValue | The value at the top of the scrollbar.  
bottomValue | The value at the bottom of the scrollbar.  
style | The style to use for the scrollbar background. If left out, the `horizontalScrollbar` style from the current [GUISkin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISkin.html) is used.  
### Returns
**float** The modified value. This can be changed by the user by dragging the scrollbar, or clicking the arrows at the end. 
### Description
Make a vertical scrollbar. Scrollbars are what you use to scroll through a document. Most likely, you want to use scrollViews instead.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public float vSbarValue;  
  
    void OnGUI()
    {
        vSbarValue = GUI.VerticalScrollbar[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.VerticalScrollbar.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(25, 25, 100, 30), vSbarValue, 1.0F, 10.0F, 0.0F);
    }
}

```

**Finding extra elements:**   
  
The styles of the buttons at the end of the scrollbar are searched for in the current skin by adding "upbutton" and "downbutton" to the style name. The name of the scrollbar thumb (the thing you drag) is found by appending "thumb" to the style name.
```
// This will use the following style names to determine the size / placement of the buttons
// MyVertScrollbarupbutton   - Name of style used for the up button.
// MyVertScrollbardownbutton - Name of style used for the down button.
// MyVertScrollbarthumb      - Name of style used for the draggable thumb.  
  
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public float scrollPos = 0.5f;  
  
    void OnGUI()
    {
        scrollPos = GUI.VerticalScrollbar[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.VerticalScrollbar.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 100, 20), scrollPos, 1, 0, 100, "Scroll");
    }
}

```

* * *
