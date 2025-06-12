* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.BeginScrollView.html

#  [GUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.html).BeginScrollView
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
public static [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) BeginScrollView([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) scrollPosition, params GUILayoutOption[] options); 
## Declaration
public static [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) BeginScrollView([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) scrollPosition, bool alwaysShowHorizontal, bool alwaysShowVertical, params GUILayoutOption[] options); 
## Declaration
public static [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) BeginScrollView([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) scrollPosition, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) horizontalScrollbar, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) verticalScrollbar, params GUILayoutOption[] options); 
## Declaration
public static [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) BeginScrollView([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) scrollPosition, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style); 
## Declaration
public static [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) BeginScrollView([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) scrollPosition, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
## Declaration
public static [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) BeginScrollView([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) scrollPosition, bool alwaysShowHorizontal, bool alwaysShowVertical, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) horizontalScrollbar, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) verticalScrollbar, params GUILayoutOption[] options); 
## Declaration
public static [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) BeginScrollView([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) scrollPosition, bool alwaysShowHorizontal, bool alwaysShowVertical, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) horizontalScrollbar, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) verticalScrollbar, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) background, params GUILayoutOption[] options); 
### Parameters
Parameter | Description  
---|---  
scrollPosition | The position to use display.  
alwaysShowHorizontal | Optional parameter to always show the horizontal scrollbar. If false or left out, it is only shown when the content inside the ScrollView is wider than the scrollview itself.  
alwaysShowVertical | Optional parameter to always show the vertical scrollbar. If false or left out, it is only shown when content inside the ScrollView is taller than the scrollview itself.  
horizontalScrollbar | Optional [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) to use for the horizontal scrollbar. If left out, the `horizontalScrollbar` style from the current [GUISkin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISkin.html) is used.  
verticalScrollbar | Optional [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) to use for the vertical scrollbar. If left out, the `verticalScrollbar` style from the current [GUISkin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISkin.html) is used.  
### Returns
**Vector2** The modified scrollPosition. Feed this back into the variable you pass in, as shown in the example. 
### Description
Begin an automatically laid out scrollview.
Automatically laid out scrollviews will take whatever content you have inside them and display normally. If it doesn't fit, scrollbars will appear. A call to BeginScrollView must always be matched with a call to EndScrollView.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/GUILayoutScrollView.png)  
_Scroll View in the Game View.._
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // The variable to control where the scrollview 'looks' into its child elements.
    Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) scrollPosition;  
  
    // The string to display inside the scrollview. 2 buttons below add & clear this string.
    string longString = "This is a long-ish string";  
  
    void OnGUI()
    {
        // Begin a scroll view. All rects are calculated automatically -
        // it will use up any available screen space and make sure contents flow correctly.
        // This is kept small with the last two parameters to force scrollbars to appear.
        scrollPosition = GUILayout.BeginScrollView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.BeginScrollView.html)(
            scrollPosition, GUILayout.Width[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Width.html)(100), GUILayout.Height[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Height.html)(100));  
  
        // We just add a single label to go inside the scroll view. Note how the
        // scrollbars will work correctly with wordwrap.
        GUILayout.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Label.html)(longString);  
  
        // Add a button to clear the string. This is inside the scroll area, so it
        // will be scrolled as well. Note how the button becomes narrower to make room
        // for the vertical scrollbar
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Clear"))
            longString = "";  
  
        // End the scrollview we began above.
        GUILayout.EndScrollView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.EndScrollView.html)();  
  
        // Now we add a button outside the scrollview - this will be shown below
        // the scrolling area.
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Add More Text"))
            longString += "\nHere is another line";
    }
}

```

* * *
