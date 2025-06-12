* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HashUtilities.ComputeHash128.html

#  [HashUtilities](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HashUtilities.html).ComputeHash128
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
public static void ComputeHash128(byte[] value, ref [Hash128](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Hash128.html) hash); 
## Declaration
public static void ComputeHash128(ref T value, ref [Hash128](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Hash128.html) hash); 
### Parameters
Parameter | Description  
---|---  
value | A reference to the value to hash.  
hash | A reference to the Hash128 to updated with the computed hash.  
### Description
Compute a 128 bit hash based on a value. the type of the value must be a value type.
```
using UnityEngine;
using System.Runtime.InteropServices;  
  
public class HashUtilitiesSample
{
    [StructLayout(LayoutKind.Sequential)]
    struct TestData
    {
        public ulong V1;
        public ulong V2;
    }  
  
    public void ComputeHash128_ToHash128()
    {
        var message = new TestData
        {
            V1 = 0x73BC2A67F,
            V2 = 0x54B1A5C2C
        };  
  
        Hash128[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Hash128.html) hash = new Hash128[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Hash128.html)();
        HashUtilities.ComputeHash128[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HashUtilities.ComputeHash128.html)(ref message, ref hash);
    }
}

```

* * *
