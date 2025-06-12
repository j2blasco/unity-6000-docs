* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.RequireImplementorsAttribute.html

# RequireImplementorsAttribute
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
When the interface type is marked, all types implementing that interface will be marked.
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using UnityEngine;
using UnityEngine.Scripting;  
  
public class NewBehaviourScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        IFoo ifoo = new Foo();
    }
}  
  
[RequireImplementors]
interface IFoo {}  
  
class Foo : IFoo {}  
  
// UnusedFoo is not used, however, it will survive managed code stripping due to IFoo having the [RequireImplementors] attribute.
class UnusedFoo : IFoo
{
    // Note that unused members of UnusedFoo will still be removed by managed code stripping
    public static void UnusedMethod() {}
}  
  
// IBar is not used so it will be removed by managed code stripping
[RequireImplementors]
interface IBar {}  
  
// Because IBar is not used, the [RequireImplementors] attribute on IBar has no impact.  UnusedBar will also be removed.
class UnusedBar : IBar {}

```

* * *
