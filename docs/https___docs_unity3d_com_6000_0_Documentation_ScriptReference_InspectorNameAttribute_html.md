* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InspectorNameAttribute.html

# InspectorNameAttribute
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
Use this attribute on enum value declarations to change the display name shown in the Inspector.
Additional resources: [SerializedProperty.enumDisplayNames](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-enumDisplayNames.html)
```
using UnityEngine;  
  
public enum ModelImporterIndexFormat[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterIndexFormat.html)
{
    Auto = 0,
    [InspectorName("16 bits")]
    UInt16 = 1,
    [InspectorName("32 bits")]
    UInt32 = 2,
}

```

### Properties
Property | Description  
---|---  
[displayName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InspectorNameAttribute-displayName.html) | Name to display in the Inspector.  
### Constructors
Constructor | Description  
---|---  
[InspectorNameAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InspectorNameAttribute-ctor.html) | Specify a display name for an enum value.  
### Inherited Members
### Properties
Property | Description  
---|---  
[applyToCollection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyAttribute-applyToCollection.html) | Makes attribute affect collections instead of their items.  
[order](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyAttribute-order.html) | Optional field to specify the order that multiple DecorationDrawers should be drawn in.  
* * *
