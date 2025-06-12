* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle-onActive.html

#  [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html).onActive
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
[GUIStyleState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyleState.html) onActive; 
### Description
Rendering settings for when the element is turned on and pressed down.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Sets the text color of button to yellow when an
    // element is turned on and pressed down.
    void OnGUI()
    {
        GUI.skin.button.onActive.textColor = Color.yellow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-yellow.html);
    }
}

```

* * *
