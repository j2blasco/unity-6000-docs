* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Hash128.Append.html

#  [Hash128](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Hash128.html).Append
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
public void Append(int val); 
## Declaration
public void Append(float val); 
## Declaration
public void Append(ref T val); 
### Parameters
Parameter | Description  
---|---  
val | Input value.  
### Description
Hash new input data and combine with the current hash value.
The value must be an "unmanaged" C# type. Primitive types like int, float, bool, enums, pointers, or structs containing primitive types are all unmanaged types. See [Unmanaged types](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/unmanaged-types) in C# language reference.  
  
The int and float overloads use a dedicated code path that is optimized for 4-byte data sizes.
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        var hash = new Hash128[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Hash128.html)();
        hash.Append(42);
        hash.Append(13.0f);
        hash.Append("Hello");
        hash.Append(new int[] {1, 2, 3, 4, 5});
        // prints "2d6e582c3fcfb4b8f3c16650a75dc37b"
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(hash.ToString());
    }
}

```

* * *
## Declaration
public void Append(string data); 
### Parameters
Parameter | Description  
---|---  
data | Input data string. Note that Unity interprets the string as UTF-8 data, even if internally in C# strings are UTF-16.  
### Description
Hash new input string and combine with the current hash value.
* * *
## Declaration
public void Append(T[] data); 
## Declaration
public void Append(List<T> data); 
## Declaration
public void Append(NativeArray<T> data); 
### Parameters
Parameter | Description  
---|---  
data | Input data array.  
### Description
Hash new input data array and combine with the current hash value.
* * *
## Declaration
public void Append(T[] data, int start, int count); 
## Declaration
public void Append(List<T> data, int start, int count); 
## Declaration
public void Append(NativeArray<T> data, int start, int count); 
### Parameters
Parameter | Description  
---|---  
data | Input data array.  
start | The first element in the data to start hashing from.  
count | Number of array elements to hash.  
### Description
Hash a slice of new input data array and combine with the current hash value.
* * *
## Declaration
public void Append(void* data, ulong size); 
### Parameters
Parameter | Description  
---|---  
data | Raw data pointer, usually used with C# `stackalloc` data.  
size | Data size in bytes.  
### Description
Hash new input data and combine with the current hash value.
* * *
