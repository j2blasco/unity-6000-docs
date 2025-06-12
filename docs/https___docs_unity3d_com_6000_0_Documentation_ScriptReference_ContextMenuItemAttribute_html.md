* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContextMenuItemAttribute.html

# ContextMenuItemAttribute
class in UnityEngine
/
Inherits from:[PropertyAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyAttribute.html)
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
Use this attribute to add a context menu to a field that calls a named method.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [ContextMenuItem("Reset", "ResetBiography")]
    [Multiline(8)]
    [SerializeField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeField.html)] 
    string playerBiography = "";  
  
    void ResetBiography()
    {
        playerBiography = "";
    }
}

```

### Properties
Property | Description  
---|---  
[function](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContextMenuItemAttribute-function.html) | The name of the function that should be called.  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContextMenuItemAttribute-name.html) | The name of the context menu item.  
### Constructors
Constructor | Description  
---|---  
[ContextMenuItemAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContextMenuItemAttribute-ctor.html) | Use this attribute to add a context menu to a field that calls a named method.  
### Inherited Members
### Properties
Property | Description  
---|---  
[applyToCollection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyAttribute-applyToCollection.html) | Makes attribute affect collections instead of their items.  
[order](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyAttribute-order.html) | Optional field to specify the order that multiple DecorationDrawers should be drawn in.  
* * *
