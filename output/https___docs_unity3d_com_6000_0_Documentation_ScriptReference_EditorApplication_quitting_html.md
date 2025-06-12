* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-quitting.html

#  [EditorApplication](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.html).quitting
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
Unity raises this event when the editor application is quitting.
Add an event handler to this event to receive a notification that the application is quitting.  
  
Note that this will not fire if the Editor is forced to quit or if there is a crash. This event is raised when the quitting process cannot be cancelled.  
  
To prevent the EditorApplication from quitting look at the [EditorApplication.wantsToQuit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-wantsToQuit.html) event.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
// Ensure class initializer is called whenever scripts recompile
[InitializeOnLoad]
public class EditorQuitExample
{
    static void Quit()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Quitting the Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)");
    }  
  
    static EditorQuitExample()
    {
        EditorApplication.quitting[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-quitting.html) += Quit;
    }
}

```

Additional resources: [EditorApplication.wantsToQuit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-wantsToQuit.html).
* * *
