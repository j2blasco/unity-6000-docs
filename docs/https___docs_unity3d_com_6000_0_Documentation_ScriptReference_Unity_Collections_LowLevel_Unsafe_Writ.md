* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.LowLevel.Unsafe.WriteAccessRequiredAttribute.html

# WriteAccessRequiredAttribute
class in Unity.Collections.LowLevel.Unsafe
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
Specify which struct method and property requires write access to be invoked.
Used in conjunction with the [ReadOnlyAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.ReadOnlyAttribute.html), WriteAccessRequiredAttribute lets you specify which struct method and property requires write access to be invoked. When you add the [ReadOnly](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.ReadOnly.html) attribute to a native container, it indicates that only operations that read data can be performed on the native container, and you can't use methods and properties on the native container that modify the array. The `WriteAccessRequired` attribute indicates which methods and properties can't be used on a native container with the [ReadOnly](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.ReadOnly.html) attribute.
```
using Unity.Collections.LowLevel.Unsafe;
using Unity.Collections;
using UnityEngine;  
  
[NativeContainer]
public struct MyList<T> where T : struct
{
    public int Length[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Length.html) { get; private set; }  
  
    [WriteAccessRequired]
    public void Grow(int capacity)
    {
        // ...
    }
}  
  
public class MyMonoBehaviour : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [ReadOnly[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.ReadOnly.html)]
    MyList<int> readOnlyList;  
  
    MyList<int> writableList = new MyList<int>();  
  
    public void OnUpdate()
    {
        writableList.Grow(10); // Ok
        readOnlyList.Grow(10); // Illegal
    }
}

```

* * *
