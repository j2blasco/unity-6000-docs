* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContextMenu-ctor.html

# ContextMenu Constructor
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
## Declaration
public ContextMenu(string itemName); 
## Declaration
public ContextMenu(string itemName, bool isValidateFunction); 
## Declaration
public ContextMenu(string itemName, bool isValidateFunction, int priority); 
### Parameters
Parameter | Description  
---|---  
itemName | The name of the context menu item.  
isValidateFunction | Whether this is a validate function (defaults to false).  
priority | Priority used to override the ordering of the menu items (defaults to 1000000). The lower the number the earlier in the menu it will appear.  
### Description
Adds the function to the context menu of the component.
In the inspector of the attached script. When the user selects the context menu, the function will be executed.  
  
This is most useful for automatically setting up Scene data from the script. The function has to be non-static.
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
* * *
