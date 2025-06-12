* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-playModeStateChanged.html

#  [EditorApplication](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.html).playModeStateChanged
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
### Description
Event that is raised whenever the Editor's play mode state changes.
Add an event handler to this event to receive a notification that the play mode state has changed, as well as information about the state it has changed into.  
  
The following example script logs the Editor's play mode state to the console whenever if changes. Copy it into a file called PlayModeStateChangedExample.cs and put it in a folder called Editor.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
// ensure class initializer is called whenever scripts recompile
[InitializeOnLoadAttribute[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InitializeOnLoadAttribute.html)]
public static class PlayModeStateChangedExample
{
    // register an event handler when the class is initialized
    static PlayModeStateChangedExample()
    {
        EditorApplication.playModeStateChanged[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-playModeStateChanged.html) += LogPlayModeState;
    }  
  
    private static void LogPlayModeState(PlayModeStateChange[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayModeStateChange.html) state)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(state);
    }
}

```

Additional resources: [PlayModeStateChange](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayModeStateChange.html), [EditorApplication.isPlaying](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-isPlaying.html), [EditorApplication.pauseStateChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-pauseStateChanged.html).
* * *
