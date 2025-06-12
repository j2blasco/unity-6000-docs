* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-isPaused.html

#  [EditorApplication](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.html).isPaused
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
isPaused; 
### Description
Whether the Editor is paused.
This returns true if the Editor is paused. Use this to change the pause state programmatically, like pressing the Pause button in the main toolbar.  
  
This also returns true when you press the Step button in the main toolbar or when you call [Step](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.Step.html).  
  
Additional resources: [isPlaying](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-isPlaying.html).
```
// Simple Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) script that confirms that the game
// is paused.  
  
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class isPausedExample
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) paused in Play mode")]
    static void EditorPlaying()
    {
        if (EditorApplication.isPaused[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-isPaused.html))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Paused");
        }
    }
}

```

* * *
