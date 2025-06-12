* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuCommand.html

# MenuCommand
class in UnityEditor
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
Used to extract the context for a [MenuItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html).
[MenuCommand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuCommand.html) objects are passed to custom menu item functions defined using the [MenuItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html) attribute.  
  
**Note:** The menu is added to the object and is accessible by right-clicking in the inspector. The script code requires the CONTEXT option.
```
// Add context menu named "Do Something" to context menu
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
Additional resources: [MenuItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html).
### Properties
Property | Description  
---|---  
[context](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuCommand-context.html) | Context is the object that is the target of a menu command.  
[userData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuCommand-userData.html) | An integer for passing custom information to a menu item.  
### Constructors
Constructor | Description  
---|---  
[MenuCommand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuCommand-ctor.html) | Creates a new MenuCommand object.  
* * *
