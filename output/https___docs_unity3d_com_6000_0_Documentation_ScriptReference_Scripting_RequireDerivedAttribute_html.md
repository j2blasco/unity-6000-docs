* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.RequireDerivedAttribute.html

# RequireDerivedAttribute
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
When the type is marked, all types derived from that type will also be marked.
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using UnityEngine;
using UnityEngine.Scripting;  
  
public class NewBehaviourScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        new Foo();
    }
}  
  
[RequireDerived]
class Foo {}  
  
// UnusedFoo is not used, however, it will survive managed code stripping due to Foo having the [RequireDerived] attribute.
class UnusedFoo : Foo
{
    // Note that unused members of UnusedFoo will still be removed by managed code stripping
    public static void UnusedMethod() {}
}  
  

// Bar is not used so it will be removed by managed code stripping
[RequireDerived]
class Bar {}  
  
// Because Bar is not used, the [RequireDerived] attribute on Bar has no impact.  UnusedBar will also be removed.
class UnusedBar : Bar {}

```

* * *
