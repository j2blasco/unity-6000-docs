* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.LoadFromFileAsync.html

#  [AssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html).LoadFromFileAsync
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
public static [AssetBundleCreateRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleCreateRequest.html) LoadFromFileAsync(string path); 
## Declaration
public static [AssetBundleCreateRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleCreateRequest.html) LoadFromFileAsync(string path, uint crc); 
## Declaration
public static [AssetBundleCreateRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleCreateRequest.html) LoadFromFileAsync(string path, uint crc, ulong offset); 
### Parameters
Parameter | Description  
---|---  
path | Path of the file on disk.  
crc | An optional CRC-32 checksum of the uncompressed content. If this is non-zero, then the content will be compared against the checksum before loading it, and give an error if it does not match.  
offset | An optional byte offset. This value specifies where to start reading the AssetBundle from.  
### Returns
**AssetBundleCreateRequest** Asynchronous load request for an AssetBundle. Use [assetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleCreateRequest-assetBundle.html) property to get an AssetBundle once it is loaded. 
### Description
Asynchronously loads an AssetBundle from a file on disk.
The function supports bundles of any compression type. In case of **LZMA** compression, the data will be decompressed to the memory. See [AssetBundles compression](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Cache.html) for more details.  
  
This is the fastest way to load an AssetBundle.
```
using UnityEngine;
using System.Collections;
using System.IO;  
  
public class LoadFromFileAsyncExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    IEnumerator Start()
    {
        var bundleLoadRequest = AssetBundle.LoadFromFileAsync[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.LoadFromFileAsync.html)(Path.Combine(Application.streamingAssetsPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-streamingAssetsPath.html), "myassetBundle"));
        yield return bundleLoadRequest;  
  
        var myLoadedAssetBundle = bundleLoadRequest.assetBundle;
        if (myLoadedAssetBundle == null)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Failed to load AssetBundle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html)!");
            yield break;
        }  
  
        var assetLoadRequest = myLoadedAssetBundle.LoadAssetAsync<GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)>("MyObject");
        yield return assetLoadRequest;  
  
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) prefab = assetLoadRequest.asset as GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html);
        Instantiate(prefab);  
  
        myLoadedAssetBundle.Unload(false);
    }
}

```

Additional resources: [AssetBundleCreateRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleCreateRequest.html), [LoadFromFile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.LoadFromFile.html).
* * *
