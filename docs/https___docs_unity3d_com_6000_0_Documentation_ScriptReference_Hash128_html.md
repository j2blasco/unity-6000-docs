* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Hash128.html

# Hash128
struct in UnityEngine
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
Represents a 128-bit hash value.
Use `Hash128` to uniquely identify a piece of data. A 128-bit hash value has an extremely low probability of hash collisions, so you can assume that if the hash values of two pieces of data are identical, then the data is identical too. For example, to quickly determine whether texture pixel contents have changed, or if they are identical between several textures, you can use [Texture.imageContentsHash](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-imageContentsHash.html).  
  
To compute the hash values for some data, use the [Hash128.Compute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Hash128.Compute.html) function. To compute the hash values incrementally for several pieces of data, use [Hash128.Append](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Hash128.Append.html).
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
The hash algorithm used to compute `Hash128` values is [SpookyHash V2](https://en.wikipedia.org/wiki/Jenkins_hash_function#SpookyHash). Note that while this hash algorithm is quite fast to compute and has good hash distribution qualities, it is not a cryptographic hash function.
### Properties
Property | Description  
---|---  
[isValid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Hash128-isValid.html) | Returns true is the hash value is valid. (Read Only)  
### Constructors
Constructor | Description  
---|---  
[Hash128](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Hash128-ctor.html) | Directly initialize a Hash128 with a 128-bit value.  
### Public Methods
Method | Description  
---|---  
[Append](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Hash128.Append.html) | Hash new input data and combine with the current hash value.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Hash128.ToString.html) | Convert a Hash128 to string.  
### Static Methods
Method | Description  
---|---  
[Compute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Hash128.Compute.html) | Compute a hash of input data.  
[Parse](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Hash128.Parse.html) | Convert a hex-encoded string into Hash128 value.  
* * *
