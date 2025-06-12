* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Hash128.ToString.html

#  [Hash128](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Hash128.html).ToString
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
public string ToString(); 
### Description
Convert a Hash128 to string.
This creates a string that is 32 characters long. Each of the 16 hash bytes is represented as two hexadecimal characters.
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
Additional resources: [Hash128.Parse](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Hash128.Parse.html).
* * *
