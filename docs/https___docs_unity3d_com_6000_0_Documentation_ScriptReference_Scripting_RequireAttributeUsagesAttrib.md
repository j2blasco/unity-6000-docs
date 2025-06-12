* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.RequireAttributeUsagesAttribute.html

# RequireAttributeUsagesAttribute
class in UnityEngine.Scripting
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
Only allowed on attribute types. If the attribute type is marked, then so too will all CustomAttributes of that type.
Note that Low and Medium Managed Stripping Levels do not remove any CustomAttributes.
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using UnityEngine;
using UnityEngine.Scripting;  
  
public class NewBehaviourScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        var f = new Foo();
        foreach (var attr in f.GetType().CustomAttributes)
        {
            if (attr.AttributeType == typeof(TypeUsedAttribute))
            {
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(attr.AttributeType);
            }
        }
    }
}  
  
[TypeUsed] // Will survive because TypeUsedAttribute is used
[Required] // Will survive because RequiredAttribute has the attribute [RequireAttributeUsages]
[UnusedAndNotRequiredAttribute] // Is considered valid for managed code stripping to remove
class Foo
{
}  
  

class TypeUsedAttribute : Attribute
{
}  
  
[RequireAttributeUsages]
class RequiredAttribute : Attribute
{
}  
  
class UnusedAndNotRequiredAttribute : Attribute
{
}

```

* * *
