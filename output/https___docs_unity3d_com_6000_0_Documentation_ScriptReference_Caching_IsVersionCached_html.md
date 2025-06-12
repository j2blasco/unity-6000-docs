* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.IsVersionCached.html

#  [Caching](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.html).IsVersionCached
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
public static bool IsVersionCached(string url, [Hash128](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Hash128.html) hash); 
**Obsolete** Please use IsVersionCached with Hash128 instead.
## Declaration
public static bool IsVersionCached(string url, int version); 
### Parameters
Parameter | Description  
---|---  
Url | The filename of the AssetBundle. Domain and path information are stripped from this string automatically.  
hash | The version hash of the AssetBundle to check for. Corresponds to the version hash in some signatures of [UnityWebRequestAssetBundle.GetAssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequestAssetBundle.GetAssetBundle.html).  
version | The version number of the AssetBundle to check for. Corresponds to the numeric version in some signatures of [UnityWebRequestAssetBundle.GetAssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequestAssetBundle.GetAssetBundle.html).  
### Returns
**bool** True if an AssetBundle matching the `url` and `version` parameters has previously been loaded using UnityWebRequestAssetBundle.GetAssetBundle() and is currently stored in the cache. Returns false if the AssetBundle is not in cache, either because it has been flushed from the cache or was never loaded using the Caching API. 
### Description
Checks if an AssetBundle is cached.
When using the default shared cache, the URL of the WebPlayer application bundle is automatically prepended to the `url` parameter; this prevents filename collisions with identically-named AssetBundles used by other developers' WebPlayer applications. WebPlayer applications that use a dedicated cache do not experience this behavior. This function can be utilized to enable AssetBundle preloading. First, call Caching.IsVersionCached() to see if the current version of an AssetBundle is already cached. If the AssetBundle is not cached, it can be preloaded in the background so that it is immediately available for loading into memory when requested. 
* * *
