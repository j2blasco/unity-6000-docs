* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.AreNotApproximatelyEqual.html

#  [Assert](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.html).AreNotApproximatelyEqual
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
public static void AreNotApproximatelyEqual(float expected, float actual); 
## Declaration
public static void AreNotApproximatelyEqual(float expected, float actual, string message); 
## Declaration
public static void AreNotApproximatelyEqual(float expected, float actual, float tolerance); 
## Declaration
public static void AreNotApproximatelyEqual(float expected, float actual, float tolerance, string message); 
### Parameters
Parameter | Description  
---|---  
tolerance | Tolerance of approximation.  
expected | The assumed [Assert](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.html) value.  
actual | The exact [Assert](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.html) value.  
message | The string used to describe the [Assert](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.html).  
### Description
Asserts that the values are approximately not equal.
An absolute error check is used for approximate equality check (|a-b| < tolerance). Default tolerance is 0.00001f.
```
using UnityEngine;
using UnityEngine.Assertions;  
  
public class AssertionExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) rb;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // Make sure the rigidbody never stops.
        // AreNotApproximatelyEqual should be used for comparing floating point variables.
        // Unless specified, default error tolerance will be used.
        Assert.AreNotApproximatelyEqual[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.AreNotApproximatelyEqual.html)(0.0f, rb.velocity.magnitude);
    }
}

```

* * *
