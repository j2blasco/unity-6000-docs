* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomYieldInstruction.html

# CustomYieldInstruction
class in UnityEngine
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
Base class for custom yield instructions to suspend coroutines.
[CustomYieldInstruction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomYieldInstruction.html) lets you implement custom yield instructions to suspend coroutine execution until an event happens. Under the hood, custom yield instruction is just another running coroutine. To implement it, inherit from [CustomYieldInstruction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomYieldInstruction.html) class and override [keepWaiting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomYieldInstruction-keepWaiting.html) property. To keep coroutine suspended return `true`. To let coroutine proceed with execution return `false`. [keepWaiting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomYieldInstruction-keepWaiting.html) property is queried each frame after [MonoBehaviour.Update](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.Update.html) and before [MonoBehaviour.LateUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.LateUpdate.html).  
  
This class requires Unity 5.3 or later.  
  
To keep coroutine suspended, return `true`. To let coroutine proceed with execution, return `false`.
```
// Example showing how a CustomYieldInstruction[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomYieldInstruction.html) script file
// can be used.  This waits for the left button to go up and then
// waits for the right button to go down.
using System.Collections;
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (Input.GetMouseButtonUp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetMouseButtonUp.html)(0))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Left mouse button up");
            StartCoroutine(waitForMouseDown());
        }
    }  
  
    public IEnumerator waitForMouseDown()
    {
        yield return new WaitForMouseDown();
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Right mouse button pressed");
    }
}

```

The following script implements the overridable version of `keepWaiting`. This c# implementation can be used by JS. In this case make sure this c# script is in a folder such as `Plugins` so it is compiled before the JS script example above.
```
using UnityEngine;  
  
public class WaitForMouseDown : CustomYieldInstruction[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomYieldInstruction.html)
{
    public override bool keepWaiting
    {
        get
        {
            return !Input.GetMouseButtonDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetMouseButtonDown.html)(1);
        }
    }  
  
    public WaitForMouseDown()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Waiting for Mouse right button down");
    }
}

```

```
using System.Collections;
using UnityEngine;
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);  
  
// Implementation of WaitWhile[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitWhile.html) yield instruction. This can be later used as:
// yield return new WaitWhile[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitWhile.html)(() => Princess.isInCastle);
class WaitWhile1 : CustomYieldInstruction[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomYieldInstruction.html)
{
    Func<bool> m_Predicate;  
  
    public override bool keepWaiting { get { return m_Predicate(); } }  
  
    public WaitWhile1(Func<bool> predicate) { m_Predicate = predicate; }
}

```

To have more control and implement more complex yield instructions you can inherit directly from `System.Collections.IEnumerator` class. In this case, implement `MoveNext()` method the same way you would implement [keepWaiting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomYieldInstruction-keepWaiting.html) property. Additionally to that, you can also return an object in `Current` property, that will be processed by Unity's coroutine scheduler after executing `MoveNext()` method. So for example if `Current` returned another object inheriting from `IEnumerator`, then current enumerator would be suspended until the returned one has completed.
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.Collections;  
  
// Same WaitWhile[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitWhile.html) implemented by inheriting from IEnumerator.
class WaitWhile2 : IEnumerator
{
    Func<bool> m_Predicate;  
  
    public object Current { get { return null; } }  
  
    public bool MoveNext() { return m_Predicate(); }  
  
    public void Reset() {}  
  
    public WaitWhile2(Func<bool> predicate) { m_Predicate = predicate; }
}

```

### Properties
Property | Description  
---|---  
[keepWaiting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomYieldInstruction-keepWaiting.html) | Indicates if coroutine should be kept suspended.  
* * *
