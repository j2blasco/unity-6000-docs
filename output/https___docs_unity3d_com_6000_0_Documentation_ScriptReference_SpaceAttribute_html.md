* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpaceAttribute.html

# SpaceAttribute
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
Use this [PropertyAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyAttribute.html) to add some spacing in the Inspector.
The spacing is done using a [DecoratorDrawer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DecoratorDrawer.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    int health = 0;
    int maxHealth = 100;  
  
    [Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.html)(10)] // 10 pixels of spacing here.  
  
    int shield = 0;
    int maxShield = 0;
}

```

### Properties
Property | Description  
---|---  
[height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpaceAttribute-height.html) | The spacing in pixels.  
### Constructors
Constructor | Description  
---|---  
[SpaceAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpaceAttribute-ctor.html) | Use this DecoratorDrawer to add some spacing in the Inspector.  
### Inherited Members
### Properties
Property | Description  
---|---  
[applyToCollection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyAttribute-applyToCollection.html) | Makes attribute affect collections instead of their items.  
[order](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyAttribute-order.html) | Optional field to specify the order that multiple DecorationDrawers should be drawn in.  
* * *
