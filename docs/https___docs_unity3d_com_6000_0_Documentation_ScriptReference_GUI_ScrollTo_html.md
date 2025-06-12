* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.ScrollTo.html

#  [GUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html).ScrollTo
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
public static void ScrollTo([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position); 
### Description
Scrolls all enclosing scrollviews so they try to make `position` visible.
```
// Draws a Scroll view with 2 buttons inside.
// When clicked each button it moves the scroll
// where the other button is located  
  
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) scrollPos = Vector2.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2-zero.html);
    void OnGUI()
    {
        scrollPos = GUI.BeginScrollView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.BeginScrollView.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 10, 100, 50), scrollPos, new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 220, 10));  
  
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 100, 20), "Go Right"))
            GUI.ScrollTo[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.ScrollTo.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(120, 0, 100, 20));  
  
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(120, 0, 100, 20), "Go Left"))
            GUI.ScrollTo[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.ScrollTo.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 100, 20));  
  
        GUI.EndScrollView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.EndScrollView.html)();
    }
}

```

* * *
