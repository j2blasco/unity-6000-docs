* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.IsTrue.html

#  [Assert](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.html).IsTrue
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
public static void IsTrue(bool condition); 
## Declaration
public static void IsTrue(bool condition, string message); 
### Parameters
Parameter | Description  
---|---  
message | The string used to describe the [Assert](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.html).  
condition |  `true` or `false`.  
### Description
Asserts that the condition is true.
```
using UnityEngine;
using UnityEngine.Assertions;  
  
public class AssertionExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    int i = 0;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // announce if i is larger than zero
        Assert.IsTrue[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.IsTrue.html)(i > 0);  
  
        // announce if i is zero
        Assert.IsFalse[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.IsFalse.html)(i == 0);
    }
}

```

* * *
