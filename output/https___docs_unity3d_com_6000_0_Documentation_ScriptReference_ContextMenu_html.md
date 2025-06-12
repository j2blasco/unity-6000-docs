* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContextMenu.html

# ContextMenu
class in UnityEngine
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
Use the ContextMenu attribute to add commands to the context menu of the Inspector window.
In the Inspector window of the attached script, when the user selects the context menu, the function executes.  
  
This is most useful for automatically setting up Scene data from the script. The function has to be non-static.  
  
If you want to create a context menu when you right-click a property in the Inspector, use [EditorApplication.contextualPropertyMenu](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-contextualPropertyMenu.html).   
  

```
using UnityEngine;  
  
public class ContextTesting : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    /// Add a context menu named "Do Something" in the inspector
    /// of the attached script.
    [ContextMenu[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContextMenu.html)("Do Something")]
    void DoSomething()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Perform operation");
    }
}

```

### Constructors
Constructor | Description  
---|---  
[ContextMenu](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContextMenu-ctor.html) | Adds the function to the context menu of the component.  
* * *
