* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.AreNotEqual.html

#  [Assert](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.html).AreNotEqual
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
public static void AreNotEqual([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) expected, [Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) actual, string message); 
## Declaration
public static void AreNotEqual(sbyte expected, sbyte actual); 
## Declaration
public static void AreNotEqual(sbyte expected, sbyte actual, string message); 
## Declaration
public static void AreNotEqual(byte expected, byte actual); 
## Declaration
public static void AreNotEqual(byte expected, byte actual, string message); 
## Declaration
public static void AreNotEqual(char expected, char actual); 
## Declaration
public static void AreNotEqual(char expected, char actual, string message); 
## Declaration
public static void AreNotEqual(short expected, short actual); 
## Declaration
public static void AreNotEqual(short expected, short actual, string message); 
## Declaration
public static void AreNotEqual(ushort expected, ushort actual); 
## Declaration
public static void AreNotEqual(ushort expected, ushort actual, string message); 
## Declaration
public static void AreNotEqual(int expected, int actual); 
## Declaration
public static void AreNotEqual(int expected, int actual, string message); 
## Declaration
public static void AreNotEqual(uint expected, uint actual); 
## Declaration
public static void AreNotEqual(uint expected, uint actual, string message); 
## Declaration
public static void AreNotEqual(long expected, long actual); 
## Declaration
public static void AreNotEqual(long expected, long actual, string message); 
## Declaration
public static void AreNotEqual(ulong expected, ulong actual); 
## Declaration
public static void AreNotEqual(ulong expected, ulong actual, string message); 
## Declaration
public static void AreNotEqual(T expected, T actual); 
## Declaration
public static void AreNotEqual(T expected, T actual, string message); 
## Declaration
public static void AreNotEqual(T expected, T actual, string message, IEqualityComparer<T> comparer); 
### Parameters
Parameter | Description  
---|---  
expected | The assumed [Assert](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.html) value.  
actual | The exact [Assert](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.html) value.  
message | The string used to describe the [Assert](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.html).  
comparer | Method to compare `expected` and `actual` arguments have the same value.  
### Description
Assert that the values are not equal.
Show message when the `expected` and `actual` are equal.
```
using UnityEngine;
using UnityEngine.Assertions;  
  
public class AssertionExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // Make sure the Game Object's layer is never set to 0
        Assert.AreNotEqual[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.AreNotEqual.html)(0, gameObject.layer);
    }
}

```

Another example:
```
using UnityEngine;
using UnityEngine.Assertions;  
  
// Assert.AreEqual[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.AreEqual.html) and Assert.AreNotEqual[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.AreNotEqual.html) example
//
// Compare 32 to 32. AreNotEqual prints message.
// Compare 32 to 33. AreEqual prints message.  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        int expectedInt = 32;
        int actualInt = 32;  
  
        // Do not show message (32 is equal to 32).
        Assert.AreEqual[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.AreEqual.html)(expectedInt, actualInt, "AreEqual: " + expectedInt + " equals " + actualInt);  
  
        // Show message (32 is equal to 32).
        Assert.AreNotEqual[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.AreNotEqual.html)(expectedInt, actualInt, "AreNotEqual: " + expectedInt + " not equal to " + actualInt);  
  
        actualInt = 33;  
  
        // Show message (32 is not equal to 33).
        Assert.AreEqual[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.AreEqual.html)(expectedInt, actualInt, "AreEqual: " + expectedInt + " equals " + actualInt);  
  
        // Do not show message (32 is not equal to 33).
        Assert.AreNotEqual[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.AreNotEqual.html)(expectedInt, actualInt, "AreNotEqual: " + expectedInt + " not equal to " + actualInt);
    }
}

```

* * *
