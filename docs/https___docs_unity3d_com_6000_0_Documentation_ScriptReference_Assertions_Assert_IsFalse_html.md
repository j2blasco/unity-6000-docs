* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.IsFalse.html

#  [Assert](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.html).IsFalse
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
public static void IsFalse(bool condition); 
## Declaration
public static void IsFalse(bool condition, string message); 
### Parameters
Parameter | Description  
---|---  
condition |  `true` or `false`.  
message | The string used to describe the result of the `Assert`.  
### Description
Return `true` when the condition is false. Otherwise return `false`.
```
using UnityEngine;
using UnityEngine.Assertions;  
  
public class AssertionExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) go;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // Make sure the Game Object is never in active state
        Assert.IsFalse[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.IsFalse.html)(go.activeSelf);
    }
}

```

* * *
