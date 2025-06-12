* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.LoadFromMemory.html

#  [AssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html).LoadFromMemory
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
public static [AssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html) LoadFromMemory(byte[] binary); 
## Declaration
public static [AssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html) LoadFromMemory(byte[] binary, uint crc); 
### Parameters
Parameter | Description  
---|---  
binary | Array of bytes with the AssetBundle data.  
crc | An optional CRC-32 checksum of the uncompressed content. If this is non-zero, then the content will be compared against the checksum before loading it, and give an error if it does not match.  
### Returns
**AssetBundle** Loaded AssetBundle object or null if failed. 
### Description
Synchronously load an AssetBundle from a memory region.
Use this method to load an AssetBundle from an array of bytes. This is useful when you have downloaded the data with encryption and need to load the AssetBundle from the decrypted bytes.  
  
Compared to [LoadFromMemoryAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.LoadFromMemoryAsync.html), this version is synchronous and will not return until it is done creating the AssetBundle object.
```
using UnityEngine;
using UnityEngine.Networking;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    byte[] MyDecrypt(byte[] binary)
    {
        // ...Perform some decryption process here to transform the input...
        return binary;
    }  
  
    IEnumerator Start()
    {
        var uwr = UnityWebRequest.Get[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.Get.html)("https://myserver/myBundle.unity3d");
        yield return uwr.SendWebRequest();
        byte[] decryptedBytes = MyDecrypt(uwr.downloadHandler.data);
        AssetBundle.LoadFromMemory[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.LoadFromMemory.html)(decryptedBytes);
    }
}

```

Additional resources: [AssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html), [LoadFromMemoryAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.LoadFromMemoryAsync.html), [LoadFromFile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.LoadFromFile.html).
* * *
