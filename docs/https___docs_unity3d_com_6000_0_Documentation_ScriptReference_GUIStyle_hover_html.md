* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle-hover.html

#  [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html).hover
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
[GUIStyleState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyleState.html) hover; 
### Description
Rendering settings for when the mouse is hovering over the control.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Prints the text color that button is using
    // when the mouse is hovering over a control  
  
    void OnGUI()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(GUI.skin.button.hover.textColor);
    }
}

```

* * *
