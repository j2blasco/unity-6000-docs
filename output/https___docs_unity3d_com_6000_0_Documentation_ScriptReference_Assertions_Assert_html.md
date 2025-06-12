* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.html

# Assert
class in UnityEngine.Assertions
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
The Assert class contains assertion methods for setting invariants in the code.
All method calls will be conditionally included only in a development build, unless specified explicitly. See [BuildOptions.ForceEnableAssertions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildOptions.ForceEnableAssertions.html). The inclusion of an assertion is controlled by the `UNITY_ASSERTIONS` define.  
  
Assert throws exceptions whenever an assertion fails.  
  
If a debugger is attached to the project (System.Diagnostics.Debugger.IsAttached is true), [AssertionException](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.AssertionException.html) is thrown to pause the execution and invoke the debugger.
```
using UnityEngine;
using UnityEngine.Assertions;  
  
public class AssertionExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public int health;
    public GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) go;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // You expect the health never to be equal to zero
        Assert.AreNotEqual[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.AreNotEqual.html)(0, health);  
  
        // The referenced GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) should be always (in every frame) be active
        Assert.IsTrue[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.IsTrue.html)(go.activeInHierarchy);
    }
}

```

### Static Methods
Method | Description  
---|---  
[AreApproximatelyEqual](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.AreApproximatelyEqual.html) | Assert the values are approximately equal.  
[AreEqual](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.AreEqual.html) | Assert that the values are equal.  
[AreNotApproximatelyEqual](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.AreNotApproximatelyEqual.html) | Asserts that the values are approximately not equal.  
[AreNotEqual](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.AreNotEqual.html) | Assert that the values are not equal.  
[IsFalse](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.IsFalse.html) | Return true when the condition is false. Otherwise return false.  
[IsNotNull](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.IsNotNull.html) | Assert that the value is not null.  
[IsNull](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.IsNull.html) | Assert the value is null.  
[IsTrue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.IsTrue.html) | Asserts that the condition is true.  
* * *
