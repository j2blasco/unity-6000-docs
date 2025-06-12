* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.EndGroup.html

#  [GUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html).EndGroup
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
public static void EndGroup(); 
### Description
End a group.
Should be attached with [GUI.BeginGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.BeginGroup.html).  
  
Additional resources: [BeginGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.BeginGroup.html).
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnGUI()
    {
        // Constrain all drawing to be within a 800x600 pixel area centered on the screen.
        GUI.BeginGroup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.BeginGroup.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(Screen.width[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-width.html) / 2 - 400, Screen.height[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-height.html) / 2 - 300, 800, 600));  
  
        // Draw a box in the new coordinate space defined by the BeginGroup.
        // Notice how (0,0) has now been moved on-screen
        GUI.Box[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Box.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 800, 600), "This box is now centered! - here you would put your main menu");  
  
        // We need to match all BeginGroup calls with an EndGroup
        GUI.EndGroup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.EndGroup.html)();
    }
}

```

* * *
