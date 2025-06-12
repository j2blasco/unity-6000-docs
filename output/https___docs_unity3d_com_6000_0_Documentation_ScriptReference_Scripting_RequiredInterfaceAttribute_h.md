* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.RequiredInterfaceAttribute.html

# RequiredInterfaceAttribute
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
When a type is marked, all interface implementations of the specified types will be marked.
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using UnityEngine;
using UnityEngine.Scripting;  
  
public class NewBehaviourScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        new Foo();
        new Bar();
        new Jar();
        new GenericFoo<int>();
    }
}  
  
interface IUnused {}  
  
interface IFoo {}  
  
interface IGeneric<T> {}  
  
// Foo will retain IFoo.  IUnused will be removed
[RequiredInterface(typeof(IFoo))]
class Foo : IFoo, IUnused {}  
  
// Bar will retain IGeneric<int> and IGeneric<double>.  IGeneric<string> will be removed
[RequiredInterface(typeof(IGeneric<int>))]
[RequiredInterface(typeof(IGeneric<double>))]
class Bar : IGeneric<int>, IGeneric<string>, IGeneric<double> {}  
  
// Jar will retain IGeneric<int>, IGeneric<string>, and IGeneric<double>
[RequiredInterface(typeof(IGeneric<>))]
class Jar : IGeneric<int>, IGeneric<string>, IGeneric<double> {}  
  
// GenericFoo<T> will retain IGeneric<T>
[RequiredInterface(typeof(IGeneric<>))]
class GenericFoo<T> : IGeneric<T> {}

```

* * *
