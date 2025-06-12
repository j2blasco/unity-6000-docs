* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle-clipping.html

#  [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html).clipping
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
[TextClipping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextClipping.html) clipping; 
### Description
What to do when the contents to be rendered is too large to fit within the area given.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Prints how is managed the text when the contents rendered
    // are too large to fir in the area given.  
  
    void OnGUI()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(GUI.skin.button.clipping);
    }
}

```

* * *
