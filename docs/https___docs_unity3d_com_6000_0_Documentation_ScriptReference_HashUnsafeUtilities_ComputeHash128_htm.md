* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HashUnsafeUtilities.ComputeHash128.html

#  [HashUnsafeUtilities](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HashUnsafeUtilities.html).ComputeHash128
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
public static void ComputeHash128(void* data, ulong dataSize, ulong* hash1, ulong* hash2); 
## Declaration
public static void ComputeHash128(void* data, ulong dataSize, Hash128* hash); 
### Parameters
Parameter | Description  
---|---  
data | Pointer to the data to hash.  
dataSize | The number of bytes to hash.  
hash1 | A pointer to store the low 64 bits of the computed hash.  
hash2 | A pointer to store the high 64 bits of the computed hash.  
hash | A pointer to the Hash128 to updated with the computed hash.  
### Description
Compute a 128 bit hash based on a data.
```
using UnityEngine;  
  
public class HashUtilitiesSample
{
    public void ComputeHash128_ToULong()
    {
        unsafe
        {
            ulong* message = stackalloc ulong[2];
            message[0] = 0x73BC2A67F;
            message[1] = 0x54B1A5C2C;  
  
            ulong h1 = 0;
            ulong h2 = 0;  
  
            HashUnsafeUtilities.ComputeHash128[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HashUnsafeUtilities.ComputeHash128.html)(message, sizeof(ulong) * 2, &h1, &h2);
        }
    }  
  
    public void ComputeHash128_ToHash128()
    {
        unsafe
        {
            ulong* message = stackalloc ulong[2];
            message[0] = 0x73BC2A67F;
            message[1] = 0x54B1A5C2C;  
  
            Hash128[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Hash128.html) hash = new Hash128[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Hash128.html)();  
  
            HashUnsafeUtilities.ComputeHash128[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HashUnsafeUtilities.ComputeHash128.html)(message, sizeof(ulong) * 2, &hash);
        }
    }
}

```

* * *
