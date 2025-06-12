* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.LoadFromMemoryAsync.html

#  [AssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html).LoadFromMemoryAsync
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
public static [AssetBundleCreateRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleCreateRequest.html) LoadFromMemoryAsync(byte[] binary); 
## Declaration
public static [AssetBundleCreateRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleCreateRequest.html) LoadFromMemoryAsync(byte[] binary, uint crc); 
### Parameters
Parameter | Description  
---|---  
binary | Array of bytes with the AssetBundle data.  
crc | An optional CRC-32 checksum of the uncompressed content. If this is non-zero, then the content will be compared against the checksum before loading it, and give an error if it does not match.  
### Returns
**AssetBundleCreateRequest** Asynchronous load request for an AssetBundle. Use [assetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleCreateRequest-assetBundle.html) property to get an AssetBundle once it is loaded. 
### Description
Asynchronously load an AssetBundle from a memory region.
Use this method to load an AssetBundle from an array of bytes asynchronously. This is useful when you have downloaded the data with encryption using UnityWebRequest and have the unencrypted bytes in memory instead of stored in a file.  
  
Compared to [LoadFromMemory](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.LoadFromMemory.html), this version will perform AssetBundle decompression on a background thread, and will not create the AssetBundle object immediately.  
  
The content of the provided byte array is copied to create a temporary AssetBundle file in Memory, and that file is then loaded. Depending on the compression of the original AssetBundle, and the setting for [Caching.compressionEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching-compressionEnabled.html), this may also involve converting the content to LZ4 or uncompressed format. See [AssetBundles compression](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Cache.html) for more details.  
  
The following example shows how to use this method. Note, for the sake of keeping the example simple it reads the bytes from disk, which means it has no advantage over calling AssetBundle.LoadFromFileAsync directly. 
```
using UnityEngine;
using System.Collections;
using System.IO;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    IEnumerator LoadFromMemoryAsync(string path)
    {
        AssetBundleCreateRequest[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleCreateRequest.html) createRequest = AssetBundle.LoadFromMemoryAsync[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.LoadFromMemoryAsync.html)(File.ReadAllBytes[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.File.ReadAllBytes.html)(path));
        yield return createRequest;
        AssetBundle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html) bundle = createRequest.assetBundle;
        var prefab = bundle.LoadAsset<GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)>("MyObject");
        Instantiate(prefab);  
  
        bundle.Unload(true);
    }
}

```

Additional resources: [AssetBundleCreateRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleCreateRequest.html), [LoadFromMemory](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.LoadFromMemory.html), [LoadFromFileAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.LoadFromFileAsync.html).
* * *
