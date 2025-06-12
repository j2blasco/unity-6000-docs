* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.BeginScrollView.html

#  [EditorGUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.html).BeginScrollView
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
public static [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) BeginScrollView([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) scrollPosition, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
## Declaration
public static [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) BeginScrollView([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) scrollPosition, bool alwaysShowHorizontal, bool alwaysShowVertical, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) horizontalScrollbar, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) verticalScrollbar, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) background, params GUILayoutOption[] options); 
### Parameters
Parameter | Description  
---|---  
scrollPosition | The position to use display.  
style | Optional [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) to use for the background.  
background | Optional [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) to use for the background.  
alwaysShowHorizontal | Optional parameter to always show the horizontal scrollbar. If false or left out, it is only shown when the content inside the ScrollView is wider than the scrollview itself.  
alwaysShowVertical | Optional parameter to always show the vertical scrollbar. If false or left out, it is only shown when content inside the ScrollView is taller than the scrollview itself.  
horizontalScrollbar | Optional [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) to use for the horizontal scrollbar. If left out, the `horizontalScrollbar` style from the current [GUISkin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISkin.html) is used.  
verticalScrollbar | Optional [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) to use for the vertical scrollbar. If left out, the `verticalScrollbar` style from the current [GUISkin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISkin.html) is used.  
### Returns
**Vector2** The modified scrollPosition. Feed this back into the variable you pass in, as shown in the example. 
### Description
Begin an automatically laid out scrollview.
These work just like [GUILayout.BeginScrollView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.BeginScrollView.html) but feel more application-like and should be used in the editor  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/BeginEndScrollView.png)  
_Label inside a scroll view._
```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class BeginScrollViewExample : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) scrollPos;
    string t = "This is a string inside a Scroll view!";  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Modify internal Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html)")]
    static void Init()
    {
        BeginScrollViewExample window = (BeginScrollViewExample)EditorWindow.GetWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindow.html)(typeof(BeginScrollViewExample), true, "My Empty Window");
        window.Show();
    }  
  
    void OnGUI()
    {
        EditorGUILayout.BeginHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.BeginHorizontal.html)();
        scrollPos =
            EditorGUILayout.BeginScrollView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.BeginScrollView.html)(scrollPos, GUILayout.Width[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Width.html)(100), GUILayout.Height[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Height.html)(100));
        GUILayout.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Label.html)(t);
        EditorGUILayout.EndScrollView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.EndScrollView.html)();
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Add More Text", GUILayout.Width[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Width.html)(100), GUILayout.Height[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Height.html)(100)))
            t += " \nAnd this is more text!";
        EditorGUILayout.EndHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.EndHorizontal.html)();
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Clear"))
            t = "";
    }
}

```

* * *
