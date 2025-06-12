* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle-border.html

#  [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html).border
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
[RectOffset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectOffset.html) border; 
### Description
The borders of all background images.
This corresponds to the border settings for IMGUI elements. It only affects the rendering of the background image and has no effect on positioning.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Prints the left, right, top and down values of the GUIStyle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) border  
  
    RectOffset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectOffset.html) bdr;
    void OnGUI()
    {
        bdr = GUI.skin.button.border;
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Left: " + bdr.left + " Right: " + bdr.right);
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Top: " + bdr.top + " Bottom: " + bdr.bottom);
    }
}

```

* * *
