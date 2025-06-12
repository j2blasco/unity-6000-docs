* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.BeginArea.html

#  [GUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.html).BeginArea
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
public static void BeginArea([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) screenRect); 
## Declaration
public static void BeginArea([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) screenRect, string text); 
## Declaration
public static void BeginArea([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) screenRect, [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) image); 
## Declaration
public static void BeginArea([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) screenRect, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) content); 
## Declaration
public static void BeginArea([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) screenRect, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style); 
## Declaration
public static void BeginArea([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) screenRect, string text, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style); 
## Declaration
public static void BeginArea([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) screenRect, [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) image, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style); 
## Declaration
public static void BeginArea([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) screenRect, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) content, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style); 
### Parameters
Parameter | Description  
---|---  
text | Optional text to display in the area.  
image | Optional texture to display in the area.  
content | Optional text, image and tooltip top display for this area.  
style | The style to use. If left out, the empty [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) ([GUIStyle.none](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle-none.html)) is used, giving a transparent background.  
### Description
Begin a GUILayout block of GUI controls in a fixed screen area.
By default, any GUI controls made using GUILayout are placed in the top-left corner of the screen. If you want to place a series of automatically laid out controls in an arbitrary area, use GUILayout.BeginArea to define a new area for the automatic layouting system to use.  
  
Additional resources: [EndArea](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.EndArea.html)  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/GUILayoutArea.png)  
_Explained Area of the example._
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnGUI()
    {
        // Starts an area to draw elements
        GUILayout.BeginArea[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.BeginArea.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 10, 100, 100));
        GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Click me");
        GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Or me");
        GUILayout.EndArea[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.EndArea.html)();
    }
}

```

This function is very useful when mixing GUILayout code. It must be matched with a call to EndArea. BeginArea / EndArea cannot be nested.
* * *
