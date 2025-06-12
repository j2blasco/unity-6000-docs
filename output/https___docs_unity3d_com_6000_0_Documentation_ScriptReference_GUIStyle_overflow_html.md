* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle-overflow.html

#  [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html).overflow
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
[RectOffset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectOffset.html) overflow; 
### Description
Extra space to be added to the background image.
This is used if your image has a drop shadow and you want to extend the background image beyond the rectangles specified for gui elements that use this style.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Prints the left, right, top and down values of the GUIStyle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) overflow  
  
    RectOffset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectOffset.html) rctOff;  
  
    void OnGUI()
    {
        rctOff = GUI.skin.button.overflow;
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Left: " + rctOff.left + " Right: " + rctOff.right);
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Top: " + rctOff.top + " Bottom: " + rctOff.bottom);
    }
}

```

* * *
