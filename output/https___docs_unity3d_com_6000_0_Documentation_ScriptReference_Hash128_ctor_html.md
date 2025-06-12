* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Hash128-ctor.html

# Hash128 Constructor
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
public Hash128(uint u32_0, uint u32_1, uint u32_2, uint u32_3); 
## Declaration
public Hash128(ulong u64_0, ulong u64_1); 
### Parameters
Parameter | Description  
---|---  
u32_0 | First 32 bits of hash value.  
u32_1 | Second 32 bits of hash value.  
u32_2 | Third 32 bits of hash value.  
u32_3 | Fourth 32 bits of hash value.  
u64_0 | First 64 bits of hash value.  
u64_1 | Second 64 bits of hash value.  
### Description
Directly initialize a Hash128 with a 128-bit value.
To compute hash value of some data, use [Hash128.Compute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Hash128.Compute.html) function.
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        var hash = new Hash128[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Hash128.html)(0x01020304, 0xaabbccdd, 0x12345678, 0xbaadc0de);
        // prints "04030201ddccbbaa78563412dec0adba",
        // because the hash values are in little-endian byte order
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(hash.ToString());
    }
}

```

* * *
