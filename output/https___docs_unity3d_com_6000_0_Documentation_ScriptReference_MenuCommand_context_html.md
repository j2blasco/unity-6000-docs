* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuCommand-context.html

#  [MenuCommand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuCommand.html).context
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
context; 
### Description
Context is the object that is the target of a menu command.
Usually the context is the current selection or the item under the mouse when invoking a context menu. The new menu item is added to the list supplied by the selected component. The component in the Inspector has a clickable circular item at the top right. The image below shows how the Rigidbody has a MenuItem that is accessible with a click. The Context name is "Do Something". See the script below.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/MenuCommandContext.png)  
_Context menu location._
```
// Add a context menu item named "Do Something" to the Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) top right context menu  
  
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class Something : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    // Add menu item
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("CONTEXT/Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)/Do Something")]
    static void DoSomething(MenuCommand[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuCommand.html) command)
    {
        Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) body = (Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html))command.context;
        body.mass = 5;
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Changed Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)'s Mass to " + body.mass + " from Context Menu[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Menu.html)...");
    }
}

```

* * *
