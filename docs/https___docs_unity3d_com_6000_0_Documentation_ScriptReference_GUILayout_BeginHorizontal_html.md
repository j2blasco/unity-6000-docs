* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.BeginHorizontal.html

#  [GUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.html).BeginHorizontal
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
public static void BeginHorizontal(params GUILayoutOption[] options); 
## Declaration
public static void BeginHorizontal([GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
## Declaration
public static void BeginHorizontal(string text, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
## Declaration
public static void BeginHorizontal([Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) image, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
## Declaration
public static void BeginHorizontal([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) content, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
### Parameters
Parameter | Description  
---|---  
text | Text to display on group.  
image |  [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) to display on group.  
content | Text, image, and tooltip for this group.  
style | The style to use for background image and padding values. If left out, the background is transparent.  
options | An optional list of layout options that specify extra layouting properties. Any values passed in here will override settings defined by the `style`.  
Additional resources: [GUILayout.Width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Width.html), [GUILayout.Height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Height.html), [GUILayout.MinWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinWidth.html), [GUILayout.MaxWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxWidth.html), [GUILayout.MinHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinHeight.html), [GUILayout.MaxHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxHeight.html), [GUILayout.ExpandWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandWidth.html), [GUILayout.ExpandHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandHeight.html).  
### Description
Begin a Horizontal control group.
All controls rendered inside this element will be placed horizontally next to each other. The group must be closed with a call to EndHorizontal.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/GUILayoutHorizontal.png)  
_Horizontal Layout._
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnGUI()
    {
        // Starts a horizontal group
        GUILayout.BeginHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.BeginHorizontal.html)("box");  
  
        GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("I'm the first button");
        GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("I'm to the right");  
  
        GUILayout.EndHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.EndHorizontal.html)();
    }
}

```

* * *
