* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/NonReorderableAttribute.html

# NonReorderableAttribute
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
Disables reordering of an array or list in the Inspector window.
By default, array or list script variables are presented with a UI control that allows array element reordering via drag handles to the left of element content. You can use [NonReorderable] attribute on a script array or list variable to disable this. When reordering is disabled, the Inspector shows arrays or lists with a simple UI control that has an array size followed by array elements.
```
using UnityEngine;  
  
public class NonReorderableAttributeTest : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [NonReorderable]
    public int[] array;
}

```

### Inherited Members
### Properties
Property | Description  
---|---  
[applyToCollection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyAttribute-applyToCollection.html) | Makes attribute affect collections instead of their items.  
[order](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyAttribute-order.html) | Optional field to specify the order that multiple DecorationDrawers should be drawn in.  
* * *
