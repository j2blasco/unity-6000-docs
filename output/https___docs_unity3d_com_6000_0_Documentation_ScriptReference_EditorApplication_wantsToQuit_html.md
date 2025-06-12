* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-wantsToQuit.html

#  [EditorApplication](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.html).wantsToQuit
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
Unity raises this event when the editor application wants to quit.
Add an event handler to this event to receive a notification that the application is attempting to quit.  
  
When this event is raised the quit process has started but can be cancelled. This means the editor is not guaranteed to quit. For a guaranteed quit event take a look at [EditorApplication.quitting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-quitting.html)  
  
Return true and the quit process will continue. Return false and quit process will cancel. 
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
// Ensure class initializer is called whenever scripts recompile
[InitializeOnLoad]
public class EditorWantsToQuitExample
{
    static bool WantsToQuit()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) prevented from quitting.");
        return false;
    }  
  
    static EditorWantsToQuitExample()
    {
        EditorApplication.wantsToQuit[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-wantsToQuit.html) += WantsToQuit;
    }
}

```

Additional resources: [EditorApplication.quitting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-quitting.html).
* * *
