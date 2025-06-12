* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InspectorOrderAttribute.html

# InspectorOrderAttribute
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
Shows sorted enum values in the Inspector enum UI dropdowns i.e. [EditorGUI.EnumPopup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.EnumPopup.html), PropertyField etc. This attribute can be applied to enum types only.
Note: this attribute affects enum UI order only, not the behavior.
```
using UnityEngine;  
  
public class SortedEnumExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Sorts enum by value in descending order
    [InspectorOrder(InspectorSort.ByValue, InspectorSortDirection.Descending)]
    public enum SortedByValueExample
    {
        SecondItem = 2,
        ThirdItem = 3,
        FirstItem = 1
    }  
  
    // Sorts enum by name in ascending order
    [InspectorOrder()]
    public enum SortedByNameExample
    {
        SecondItem,
        ThirdItem,
        FirstItem
    }  
  
    public SortedByValueExample sortedByValueExample;
    public SortedByNameExample sortedByNameExample;
}

```

### Constructors
Constructor | Description  
---|---  
[InspectorOrderAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InspectorOrderAttribute-ctor.html) | Default constructor initializes the attribute for enum to be shown sorted in UI dropdowns.  
### Inherited Members
### Properties
Property | Description  
---|---  
[applyToCollection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyAttribute-applyToCollection.html) | Makes attribute affect collections instead of their items.  
[order](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyAttribute-order.html) | Optional field to specify the order that multiple DecorationDrawers should be drawn in.  
* * *
