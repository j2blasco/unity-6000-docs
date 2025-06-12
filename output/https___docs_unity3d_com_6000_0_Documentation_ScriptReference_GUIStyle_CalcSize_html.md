* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.CalcSize.html

#  [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html).CalcSize
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GUIStyle.html "Go to GUIStyle Component in the Manual")
## Declaration
public [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) CalcSize([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) content); 
### Description
Calculate the size of some content if it is rendered with this style.
This function does not take word wrapping into account. To do that, you need to determine the allocated width and then call [CalcHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.CalcHeight.html) to figure out the word wrapped height.
```
// Example for the GUIStyle.CalcSize[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.CalcSize.html)  
  
using UnityEngine;  
  
public class CalcSizeExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    string s;  
  
    void Start()
    {
        s = "A string for GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)()";
    }  
  
    void OnGUI()
    {
        GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) content = new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)(s);  
  
        GUIStyle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = GUI.skin.box;
        style.alignment = TextAnchor.MiddleCenter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAnchor.MiddleCenter.html);  
  
        // Compute how large the button needs to be.
        Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) size = style.CalcSize(content);  
  
        // make the Box[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Box.html) double sized
        GUI.Box[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Box.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10.0f, 10.0f, 2.0f * size.x, 2.0f * size.y), s);
    }
}

```

* * *
