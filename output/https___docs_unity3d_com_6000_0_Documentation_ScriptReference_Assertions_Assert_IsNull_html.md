* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.IsNull.html

#  [Assert](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.html).IsNull
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
public static void IsNull([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) value, string message); 
## Declaration
public static void IsNull(T value); 
## Declaration
public static void IsNull(T value, string message); 
### Parameters
Parameter | Description  
---|---  
value | The `Object` or `type` being checked for.  
message | The string used to describe the [Assert](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.html).  
### Description
Assert the value is null.
```
using UnityEngine;
using UnityEngine.Assertions;  
  
public class AssertionExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    MyClass myClassReference;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // Make sure the myClassReference reference is never set
        Assert.IsNull[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.IsNull.html)(myClassReference);
    }
}  
  
public class MyClass {}

```

* * *
