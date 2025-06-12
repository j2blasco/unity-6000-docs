* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequestAssetBundle.GetAssetBundle.html

#  [UnityWebRequestAssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequestAssetBundle.html).GetAssetBundle
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
public static [Networking.UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) GetAssetBundle(string uri); 
## Declaration
public static [Networking.UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) GetAssetBundle(Uri uri); 
## Declaration
public static [Networking.UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) GetAssetBundle(string uri, uint crc); 
## Declaration
public static [Networking.UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) GetAssetBundle(Uri uri, uint crc); 
## Declaration
public static [Networking.UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) GetAssetBundle(string uri, uint version, uint crc); 
## Declaration
public static [Networking.UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) GetAssetBundle(Uri uri, uint version, uint crc); 
## Declaration
public static [Networking.UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) GetAssetBundle(string uri, [Hash128](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Hash128.html) hash, uint crc); 
## Declaration
public static [Networking.UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) GetAssetBundle(Uri uri, [Hash128](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Hash128.html) hash, uint crc); 
## Declaration
public static [Networking.UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) GetAssetBundle(string uri, [CachedAssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CachedAssetBundle.html) cachedAssetBundle, uint crc); 
## Declaration
public static [Networking.UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) GetAssetBundle(Uri uri, [CachedAssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CachedAssetBundle.html) cachedAssetBundle, uint crc); 
### Parameters
Parameter | Description  
---|---  
uri | The URI of the asset bundle to download.  
crc | If nonzero, this number will be compared to the checksum of the downloaded asset bundle data. If the CRCs do not match, an error will be logged and the asset bundle will not be loaded. If set to zero, CRC checking will be skipped.  
version | An integer version number, which will be compared to the cached version of the asset bundle to download. Increment this number to force Unity to redownload a cached asset bundle.  
  
Analogous to the `version` parameter for WWW.LoadFromCacheOrDownload.  
hash | A version hash. If this hash does not match the hash for the cached version of this asset bundle, the asset bundle will be redownloaded.  
cachedAssetBundle | A structure used to download a given version of AssetBundle to a customized cache path.  
### Returns
**UnityWebRequest** A UnityWebRequest configured to downloading a Unity Asset Bundle. 
### Description
Creates a UnityWebRequest optimized for downloading a Unity Asset Bundle via HTTP GET.
This method creates a UnityWebRequest, sets the method to `GET` and sets the target URL to the string `uri` argument. Sets no other flags or custom headers.  
  
This method attaches a [DownloadHandlerAssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandlerAssetBundle.html) to the [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html). This [DownloadHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandler.html) has a special [DownloadHandlerAssetBundle.assetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandlerAssetBundle-assetBundle.html) property, which can be used to extract the asset bundle once enough data has been downloaded and decoded to permit access to the resources inside the bundle.  
  
In addition, the [DownloadHandlerAssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandlerAssetBundle.html) streams data into a ringbuffer and decompresses the data on a worker thread, saving many memory allocations compared to downloading the data all at once.  
  
If supplied with an integer `version` or Hash128 `hash` argument, the [DownloadHandlerAssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandlerAssetBundle.html) will employ the Asset Bundle caching system. If an Asset Bundle has been cached and does not need to be redownloaded, then the [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) will complete once the Asset Bundle has finished loading from the cache.  
  
Cached AssetBundles are uniquely identified solely by the filename and version. All domain and path information in `url` is ignored by Caching. Since cached AssetBundles are identified by filename instead of the full URL, you can change the directory from where the asset bundle is downloaded at any time. This is useful for pushing out new versions of the game and ensuring that files are not cached incorrectly by the browser or by a CDN.  
  
Usually using the filename of the AssetBundle to generate the cache path is fine. But if there are different AssetBundles with the same last file name, cache conflicts happens. With CachedAssetBundle struct, you can use [CachedAssetBundle.name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CachedAssetBundle-name.html) to customized the cache path to avoid the cache conflicts. You can also utilize this to organize the cache data structure.  
  
**Note** , that while you can use this API to load Asset Bundle from local storage (using file:// URI or jar:file// on Android), this is not recommended, use [AssetBundle.LoadFromFileAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.LoadFromFileAsync.html) instead.
```
using UnityEngine;
using UnityEngine.Networking;
using System.Collections;  
  
public class MyBehaviour : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        StartCoroutine(GetText());
    }  
  
    IEnumerator GetText()
    {
        using (UnityWebRequest[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) uwr = UnityWebRequestAssetBundle.GetAssetBundle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequestAssetBundle.GetAssetBundle.html)("https://www.my-server.com/mybundle"))
        {
            yield return uwr.SendWebRequest();  
  
            if (uwr.result != UnityWebRequest.Result.Success[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.Result.Success.html))
            {
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(uwr.error);
            }
            else
            {
                // Get downloaded asset bundle
                AssetBundle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html) bundle = DownloadHandlerAssetBundle.GetContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandlerAssetBundle.GetContent.html)(uwr);  
  
                // Unload the AssetBundle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html) 
                bundle.Unload(true);
            }
        }
    }
}

```

* * *
