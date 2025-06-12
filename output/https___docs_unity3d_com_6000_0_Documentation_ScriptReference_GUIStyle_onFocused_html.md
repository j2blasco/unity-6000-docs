* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle-onFocused.html

#  [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html).onFocused
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
[GUIStyleState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyleState.html) onFocused; 
### Description
Rendering settings for when the element has keyboard and is turned on.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnGUI()
    {
        GUI.skin.button.onFocused.textColor = Color.green[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-green.html);
    }
}

```

* * *
