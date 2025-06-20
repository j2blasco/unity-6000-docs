* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.HorizontalScrollbar.html

#  [GUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.html).HorizontalScrollbar
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
public static float HorizontalScrollbar(float value, float size, float leftValue, float rightValue, params GUILayoutOption[] options); 
## Declaration
public static float HorizontalScrollbar(float value, float size, float leftValue, float rightValue, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
### Parameters
Parameter | Description  
---|---  
value | The position between min and max.  
size | How much can we see?  
leftValue | The value at the left end of the scrollbar.  
rightValue | The value at the right end of the scrollbar.  
style | The style to use for the scrollbar background. If left out, the `horizontalScrollbar` style from the current [GUISkin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISkin.html) is used.  
options | An optional list of layout options that specify extra layouting properties. Any values passed in here will override settings defined by the `style`.  
### Returns
**float** The modified value. This can be changed by the user by dragging the scrollbar, or clicking the arrows at the end. 
### Description
Make a horizontal scrollbar.
A scrollbar control returns a float value that represents the position of the draggable "thumb" withtin the bar. You can use the value to adjust another GUI element to reflect the scroll position. However, most scrollable views can be handled more easily using a _scroll view_ control.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/GUILayoutHorizontalScrollBar.png)  
_Horizontal Scrollbar in the Game View._
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    float hSbarValue;  
  
    void OnGUI()
    {
        hSbarValue = GUILayout.HorizontalScrollbar[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.HorizontalScrollbar.html)(hSbarValue, 1.0f, 0.0f, 10.0f);
        GUILayout.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Label.html)("This is a text that makes space");
    }
}

```

The styles of the scroll buttons at the end of the bar can be located in the current skin by adding "leftbutton" and "rightbutton" to the style name. The name of the scrollbar thumb (the thing you drag) is found by appending "thumb" to the style name.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public float scrollPos = 0.5F;
    // This will use the following style names to determine the size / placement of the buttons
    // MyScrollbarleftbutton    - Name of style used for the left button.
    // MyScrollbarrightbutton - Name of style used for the right button.
    // MyScrollbarthumb         - Name of style used for the draggable thumb.
    void OnGUI()
    {
        scrollPos = GUILayout.HorizontalScrollbar[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.HorizontalScrollbar.html)(scrollPos, 1, 0, 100, "MyScrollbar");
    }
}

```

Additional resources: [BeginScrollView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.BeginScrollView.html), [VerticalScrollbar](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.VerticalScrollbar.html).
* * *
