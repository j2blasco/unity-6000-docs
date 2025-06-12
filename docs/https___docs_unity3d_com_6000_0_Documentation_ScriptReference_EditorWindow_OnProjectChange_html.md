* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.OnProjectChange.html

#  [EditorWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html).OnProjectChange()
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
Handler for message that is sent whenever the state of the project changes.
Actions that trigger this message include creating, renaming, or reparenting assets, as well as moving or renaming folders in the project. Note that the message is not sent immediately in response to these actions, but rather during the next update of the editor application.  
  
Actions taken with assets that have [HideFlags.HideInHierarchy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideFlags.HideInHierarchy.html) set will not cause this message to be sent.  
  
The [OnProjectChange](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.OnProjectChange.html) message is used to report when the items in the Project window change. Changes can include examples such as new GameObjects or Materials being added to the project. Additionally, adding folders with no contents will work as expected. As a final example [OnProjectChange](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.OnProjectChange.html) will be used to see any changes in the Project window.   
Additional resources: [EditorApplication.projectChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-projectChanged.html). .  

```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
class MyEditor : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    void OnProjectChange()
    {
         // Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html) editor according to changes in the Project
    }
}

```

* * *
