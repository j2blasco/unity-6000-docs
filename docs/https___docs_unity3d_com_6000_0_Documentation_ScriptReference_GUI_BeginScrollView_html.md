* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.BeginScrollView.html

#  [GUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html).BeginScrollView
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
public static [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) BeginScrollView([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) scrollPosition, [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) viewRect); 
## Declaration
public static [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) BeginScrollView([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) scrollPosition, [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) viewRect, bool alwaysShowHorizontal, bool alwaysShowVertical); 
## Declaration
public static [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) BeginScrollView([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) scrollPosition, [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) viewRect, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) horizontalScrollbar, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) verticalScrollbar); 
## Declaration
public static [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) BeginScrollView([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) scrollPosition, [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) viewRect, bool alwaysShowHorizontal, bool alwaysShowVertical, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) horizontalScrollbar, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) verticalScrollbar); 
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to use for the ScrollView.  
scrollPosition | The pixel distance that the view is scrolled in the X and Y directions.  
viewRect | The rectangle used inside the scrollview.  
horizontalScrollbar | Optional [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) to use for the horizontal scrollbar. If left out, the `horizontalScrollbar` style from the current [GUISkin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISkin.html) is used.  
verticalScrollbar | Optional [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) to use for the vertical scrollbar. If left out, the `verticalScrollbar` style from the current [GUISkin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISkin.html) is used.  
alwaysShowHorizontal | Optional parameter to always show the horizontal scrollbar. If false or left out, it is only shown when `viewRect` is wider than `position`.  
alwaysShowVertical | Optional parameter to always show the vertical scrollbar. If false or left out, it is only shown when `viewRect` is taller than `position`.  
### Returns
**Vector2** The modified scrollPosition. Feed this back into the variable you pass in, as shown in the example. 
### Description
Begin a scrolling view inside your GUI.
ScrollViews let you make a smaller area on-screen look 'into' a much larger area, using scrollbars placed on the sides of the ScrollView.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // The position on of the scrolling viewport
    public Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) scrollPosition = Vector2.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2-zero.html);  
  
    void OnGUI()
    {
        // An absolute-positioned example: We make a scrollview that has a really large client
        // rect and put it in a small rect on the screen.
        scrollPosition = GUI.BeginScrollView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.BeginScrollView.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 300, 100, 100), scrollPosition, new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 220, 200));  
  
        // Make four buttons - one in each corner. The coordinate system is defined
        // by the last parameter to BeginScrollView.
        GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 100, 20), "Top-left");
        GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(120, 0, 100, 20), "Top-right");
        GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 180, 100, 20), "Bottom-left");
        GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(120, 180, 100, 20), "Bottom-right");  
  
        // End the scroll view that we began above.
        GUI.EndScrollView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.EndScrollView.html)();
    }
}

```

* * *
