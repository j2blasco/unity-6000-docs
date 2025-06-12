* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EnumButtonsAttribute.html

# EnumButtonsAttribute
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
Attribute to enable editing an enum with a [ToggleButtonGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ToggleButtonGroup.html).
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.Collections.Generic;
using UnityEngine;

public enum Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Position.html)
{
    First,
    Second,
    Third
}

[Flags[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.Flags.html)]
public enum DaysOfWeek
{
    None = 0,
    Sunday = 1 << 0,
    Monday = 1 << 1,
    Tuesday = 1 << 2,
    Wednesday = 1 << 3,
    Thursday = 1 << 4,
    Friday = 1 << 5,
    Saturday = 1 << 6,

    Weekdays = Monday | Tuesday | Wednesday | Thursday | Friday,
    Weekend = Saturday | Sunday,
}

public class EnumExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [EnumButtons]
    public Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Position.html) number;

    [EnumButtons]
    public DaysOfWeek days;

    [EnumButtons]
    public List<Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Position.html)> numbersList;
}

```

### Properties
Property | Description  
---|---  
[includeObsolete](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EnumButtonsAttribute-includeObsolete.html) | Whether to display obsolete enum values?  
### Constructors
Constructor | Description  
---|---  
[EnumButtonsAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EnumButtonsAttribute-ctor.html) | Attribute to enable editing an enum with a ToggleButtonGroup.  
### Inherited Members
### Properties
Property | Description  
---|---  
[applyToCollection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyAttribute-applyToCollection.html) | Makes attribute affect collections instead of their items.  
[order](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyAttribute-order.html) | Optional field to specify the order that multiple DecorationDrawers should be drawn in.  
* * *
