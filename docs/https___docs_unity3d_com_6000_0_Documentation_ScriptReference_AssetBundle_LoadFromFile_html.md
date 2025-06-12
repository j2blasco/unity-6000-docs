* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.LoadFromFile.html

#  [AssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html).LoadFromFile
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
public static [AssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html) LoadFromFile(string path); 
## Declaration
public static [AssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html) LoadFromFile(string path, uint crc); 
## Declaration
public static [AssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html) LoadFromFile(string path, uint crc, ulong offset); 
### Parameters
Parameter | Description  
---|---  
path | Path of the file on disk.  
crc | An optional CRC-32 checksum of the uncompressed content. If this is non-zero, then the content will be compared against the checksum before loading it, and give an error if it does not match.  
offset | An optional byte offset. This value specifies where to start reading the AssetBundle from.  
### Returns
**AssetBundle** Loaded AssetBundle object or null if failed. 
### Description
Synchronously loads an AssetBundle from a file on disk.
The function supports bundles of any compression type. In case of **LZMA** compression, the file content will be fully decompressed into memory and loaded from there. See [AssetBundles compression](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Cache.html) for more details.  
  
Compared to [LoadFromFileAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.LoadFromFileAsync.html), this version is synchronous and will not return until it is done creating the AssetBundle object.  
  
This is the fastest way to load an AssetBundle.
```
using UnityEngine;
using System.Collections;
using System.IO;  
  
public class LoadFromFileExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        var myLoadedAssetBundle = AssetBundle.LoadFromFile[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.LoadFromFile.html)(Path.Combine(Application.streamingAssetsPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-streamingAssetsPath.html), "myassetBundle"));
        if (myLoadedAssetBundle == null)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Failed to load AssetBundle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html)!");
            return;
        }  
  
        var prefab = myLoadedAssetBundle.LoadAsset<GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)>("MyObject");
        Instantiate(prefab);  
  
        myLoadedAssetBundle.Unload(false);
    }
}

```

Additional resources: [AssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html), [LoadFromFileAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.LoadFromFileAsync.html).
* * *
