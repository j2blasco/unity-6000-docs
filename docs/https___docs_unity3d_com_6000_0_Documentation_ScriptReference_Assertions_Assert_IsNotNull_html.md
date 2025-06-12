* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.IsNotNull.html

#  [Assert](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.html).IsNotNull
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
public static void IsNotNull([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) value, string message); 
## Declaration
public static void IsNotNull(T value); 
## Declaration
public static void IsNotNull(T value, string message); 
### Parameters
Parameter | Description  
---|---  
value | The `Object` or `type` being checked for.  
message | The string used to describe the [Assert](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.html).  
### Description
Assert that the value is not null.
```
using UnityEngine;
using UnityEngine.Assertions;  
  
public class AssertionExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    MyClass myClassReference;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // Make sure the myClassReference reference is set
        Assert.IsNotNull[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.IsNotNull.html)(myClassReference);
    }
}  
  
public class MyClass {}

```

* * *
