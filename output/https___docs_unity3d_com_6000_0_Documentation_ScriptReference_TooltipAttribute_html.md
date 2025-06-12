* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TooltipAttribute.html

# TooltipAttribute
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
Specify a tooltip for a field in the Inspector window.
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/tooltip.png)   
_Tooltip hovering over the class it was added to._  
  
In the following script a `Tooltip` is added. This provides information to the user about the range of values for the `health` variable. The suggested range is provided in the `TooltipAttribute` string.  
  
Note: Unity will only use Tooltips from Fields when displaying them in the Editor. You can add Tooltips to other areas, such as classes, structs, and properties to work with user created editor extensions, but Unity won't display them in the Editor.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [Tooltip("Health value between 0 and 100.")]
    int health = 0;
}

```

### Properties
Property | Description  
---|---  
[tooltip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TooltipAttribute-tooltip.html) | The tooltip text.  
### Constructors
Constructor | Description  
---|---  
[TooltipAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TooltipAttribute-ctor.html) | Specify a tooltip for a field.  
### Inherited Members
### Properties
Property | Description  
---|---  
[applyToCollection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyAttribute-applyToCollection.html) | Makes attribute affect collections instead of their items.  
[order](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyAttribute-order.html) | Optional field to specify the order that multiple DecorationDrawers should be drawn in.  
* * *
