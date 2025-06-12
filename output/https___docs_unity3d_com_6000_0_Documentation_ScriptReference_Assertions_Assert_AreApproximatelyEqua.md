* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.AreApproximatelyEqual.html

#  [Assert](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.html).AreApproximatelyEqual
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
## Declaration
public static void AreApproximatelyEqual(float expected, float actual); 
## Declaration
public static void AreApproximatelyEqual(float expected, float actual, string message); 
## Declaration
public static void AreApproximatelyEqual(float expected, float actual, float tolerance); 
## Declaration
public static void AreApproximatelyEqual(float expected, float actual, float tolerance, string message); 
### Parameters
Parameter | Description  
---|---  
tolerance | Tolerance of approximation.  
expected | The assumed [Assert](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.html) value.  
actual | The exact [Assert](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.html) value.  
message | The string used to describe the [Assert](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.html).  
### Description
Assert the values are approximately equal.
An absolute error check is used for approximate equality check (|a-b| < `tolerance`). Default `tolerance` is 0.00001f.  
  
Note: Every time you call the method with tolerance specified, a new instance of [FloatComparer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Comparers.FloatComparer.html) is created. For performance reasons you might want to instance your own comparer and pass it to the [AreApproximatelyEqual](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.AreApproximatelyEqual.html) method. If the tolerance is not specifies, a default comparer is used and the issue does not occur.
```
using UnityEngine;
using UnityEngine.Assertions;  
  
public class AssertionExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // Make sure the position of the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) is always in the center of the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html).
        // AreApproximatelyEqual should be used for comparing floating point variables.
        // Unless specified, default error tolerance will be used.
        Assert.AreApproximatelyEqual[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.AreApproximatelyEqual.html)(0.0f, transform.position.x);
        Assert.AreApproximatelyEqual[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.AreApproximatelyEqual.html)(0.0f, transform.position.y);
        Assert.AreApproximatelyEqual[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.AreApproximatelyEqual.html)(0.0f, transform.position.z);
    }
}

```

* * *
