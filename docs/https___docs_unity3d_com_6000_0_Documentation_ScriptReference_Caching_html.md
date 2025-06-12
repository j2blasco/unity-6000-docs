* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.html

# Caching
class in UnityEngine
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
The Caching class lets you manage cached AssetBundles, downloaded using [UnityWebRequestAssetBundle.GetAssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequestAssetBundle.GetAssetBundle.html).
**Note:** The Cache API is not supported in WebGL because AssetBundles are stored in the browser cache for the WebGL platform.  
  
Additional resources: [DownloadHandlerAssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandlerAssetBundle.html).
```
using System.Collections;
using UnityEngine;
using System.IO;
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using UnityEngine.Networking;
using System.Collections.Generic;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    IEnumerator DownloadAndCacheAssetBundle(string uri, string manifestBundlePath)
    {
        //Load the manifest
        AssetBundle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html) manifestBundle = AssetBundle.LoadFromFile[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.LoadFromFile.html)(manifestBundlePath);
        AssetBundleManifest[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleManifest.html) manifest = manifestBundle.LoadAsset<AssetBundleManifest[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleManifest.html)>("AssetBundleManifest[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleManifest.html)");  
  
        //Create new cache
        string today = DateTime.Today.ToLongDateString();
        Directory.CreateDirectory[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Directory.CreateDirectory.html)(today);
        Cache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html) newCache = Caching.AddCache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.AddCache.html)(today);  
  
        //Set current cache for writing to the new cache if the cache is valid
        if (newCache.valid)
            Caching.currentCacheForWriting[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching-currentCacheForWriting.html) = newCache;  
  
        //Download the bundle
        Hash128[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Hash128.html) hash = manifest.GetAssetBundleHash("bundleName");
        UnityWebRequest[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) request = UnityWebRequestAssetBundle.GetAssetBundle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequestAssetBundle.GetAssetBundle.html)(uri, hash, 0);
        yield return request.SendWebRequest();
        AssetBundle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html) bundle = DownloadHandlerAssetBundle.GetContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandlerAssetBundle.GetContent.html)(request);  
  
        //Get all the cached versions
        List<Hash128[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Hash128.html)> listOfCachedVersions = new List<Hash128[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Hash128.html)>();
        Caching.GetCachedVersions[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.GetCachedVersions.html)(bundle.name, listOfCachedVersions);  
  
        if (!AssetBundleContainsAssetIWantToLoad(bundle))     //Or any conditions you want to check on your new asset bundle
        {
            //If our criteria wasn't met, we can remove the new cache and revert back to the most recent one
            Caching.currentCacheForWriting[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching-currentCacheForWriting.html) = Caching.GetCacheAt[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.GetCacheAt.html)(Caching.cacheCount[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching-cacheCount.html));
            Caching.RemoveCache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.RemoveCache.html)(newCache);  
  
            for (int i = listOfCachedVersions.Count - 1; i > 0; i--)
            {
                //Load a different bundle from a different cache
                request = UnityWebRequestAssetBundle.GetAssetBundle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequestAssetBundle.GetAssetBundle.html)(uri, listOfCachedVersions[i], 0);
                yield return request.SendWebRequest();
                bundle = DownloadHandlerAssetBundle.GetContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandlerAssetBundle.GetContent.html)(request);  
  
                //Check and see if the newly loaded bundle from the cache meets your criteria
                if (AssetBundleContainsAssetIWantToLoad(bundle))
                    break;
            }
        }
        else
        {
            //This is if we only want to keep 5 local caches at any time
            if (Caching.cacheCount[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching-cacheCount.html) > 5)
                Caching.RemoveCache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.RemoveCache.html)(Caching.GetCacheAt[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.GetCacheAt.html)(1));     //Removes the oldest user created cache
        }  
  
        manifestBundle.Unload(true);
        bundle.Unload(true);  
  
    }  
  
    bool AssetBundleContainsAssetIWantToLoad(AssetBundle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html) bundle)
    {
        return (bundle.LoadAsset<GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)>("MyAsset") != null);     //this could be any conditional
    }
}

```

To store up to five cached versions of the same bundle and use the previous caches if your most recent cache becomes invalid, or the downloaded Asset Bundle has a problem, use the following setup.
```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;
using System.IO;  
  
public class Example2 : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public static class CacheWithPriority
    {
        public enum ResolutionType
        {
            High,
            Medium,
            Low,
        }
        static readonly Dictionary<ResolutionType, Cache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html)> ResolutionCaches = new Dictionary<ResolutionType, Cache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html)>();  
  
        public static void InitResolutionCaches()
        {
            string highResPath = "HighRes";
            string medResPath = "MedRes";
            string lowResPath = Application.streamingAssetsPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-streamingAssetsPath.html);  
  
            //Create cache paths
            Directory.CreateDirectory[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Directory.CreateDirectory.html)(highResPath);
            Directory.CreateDirectory[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Directory.CreateDirectory.html)(medResPath);  
  
            //Create the caches and add them to a Dictionary
            ResolutionCaches.Add(ResolutionType.High, Caching.AddCache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.AddCache.html)(highResPath));
            ResolutionCaches.Add(ResolutionType.Medium, Caching.AddCache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.AddCache.html)(medResPath));
            ResolutionCaches.Add(ResolutionType.Low, Caching.AddCache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.AddCache.html)(lowResPath));
        }  
  
        public static void PrioritizeCacheForLoading(ResolutionType resolutionToPrioritize)
        {
            //Move cache to the start of the queue
            Caching.MoveCacheBefore[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.MoveCacheBefore.html)(ResolutionCaches[resolutionToPrioritize], Caching.GetCacheAt[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.GetCacheAt.html)(0));
        }  
  
        public static void SetResolutionCacheForWriting(ResolutionType resolutionToWriteTo)
        {
            Caching.currentCacheForWriting[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching-currentCacheForWriting.html) = ResolutionCaches[resolutionToWriteTo];
        }
    }  
  
    AssetBundle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html) currentTextureAssetBundle;
    IEnumerator RearrangeCacheOrderExample(string manifestBundlePath)
    {
        CacheWithPriority.InitResolutionCaches();  
  
        //Load the manifest
        AssetBundle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html) manifestBundle = AssetBundle.LoadFromFile[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.LoadFromFile.html)(manifestBundlePath);
        AssetBundleManifest[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleManifest.html) manifest = manifestBundle.LoadAsset<AssetBundleManifest[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleManifest.html)>("AssetBundleManifest[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleManifest.html)");  
  
        //We know we want to start loading from the Low Resolution[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resolution.html) Cache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html)
        CacheWithPriority.PrioritizeCacheForLoading(CacheWithPriority.ResolutionType.Low);  
  
        //Load the low res bundle from StreamingAssets
        UnityWebRequest[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) lowRequest = UnityWebRequestAssetBundle.GetAssetBundle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequestAssetBundle.GetAssetBundle.html)("lowResBundlePath",
            manifest.GetAssetBundleHash("lowResBundle"), 0);
        yield return lowRequest;
        currentTextureAssetBundle = DownloadHandlerAssetBundle.GetContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandlerAssetBundle.GetContent.html)(lowRequest);  
  
        //In the background we can start downloading our higher resolution bundles
        StartCoroutine(StartDownloadHigherResolutionBundles(manifest));  
  
        //Do work with low res bundle while the higher resolutions download...  
  
        //Unload the AssetBundle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html)
        manifestBundle.Unload(true);
    }  
  
    IEnumerator StartDownloadHigherResolutionBundles(AssetBundleManifest[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleManifest.html) manifest)
    {
        CacheWithPriority.SetResolutionCacheForWriting(CacheWithPriority.ResolutionType.Medium);
        UnityWebRequest[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) medRequest = UnityWebRequestAssetBundle.GetAssetBundle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequestAssetBundle.GetAssetBundle.html)("medResBundleUrl", manifest.GetAssetBundleHash("medResBundle"), 0);
        medRequest.SendWebRequest();  
  
        while (!medRequest.isDone)
            yield return null;
        SwitchTextureBundleTo(CacheWithPriority.ResolutionType.Medium, medRequest);  
  
        //Now you'll be using the medium resolution bundle  
  
        CacheWithPriority.SetResolutionCacheForWriting(CacheWithPriority.ResolutionType.High);
        UnityWebRequest[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) highRequest = UnityWebRequestAssetBundle.GetAssetBundle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequestAssetBundle.GetAssetBundle.html)("highResBundleUrl", manifest.GetAssetBundleHash("highResBundle"), 0);
        highRequest.SendWebRequest();  
  
        while (!highRequest.isDone)
            yield return null;
        SwitchTextureBundleTo(CacheWithPriority.ResolutionType.High, highRequest);  
  
        //Do work with the high resolution bundle now...
    }  
  
    void SwitchTextureBundleTo(CacheWithPriority.ResolutionType typeToSwitchTo, UnityWebRequest[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) request)
    {
        //For performance, we tell the Caching[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.html) system what cache we want it to search first
        CacheWithPriority.PrioritizeCacheForLoading(typeToSwitchTo);
        //Unload our current texture bundle
        currentTextureAssetBundle.Unload(true);
        //Load the new one from the passed in UnityWebRequest[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html)
        currentTextureAssetBundle = DownloadHandlerAssetBundle.GetContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandlerAssetBundle.GetContent.html)(request);
        currentTextureAssetBundle.Unload(true);
    }
}

```

The ability to have multiple caches allows you to keep several cached version of a particular Asset Bundle. You can use these for things like backups and fallbacks.  
  
This example shows downloading medium resolution and high resolution textures after startup and caching them in their own appropriate caches.
### Static Properties
Property | Description  
---|---  
[cacheCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching-cacheCount.html) | Returns the cache count in the cache list.  
[compressionEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching-compressionEnabled.html) | Controls compression of cache data. Enabled by default.  
[currentCacheForWriting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching-currentCacheForWriting.html) | Gets or sets the current cache in which AssetBundles should be cached.  
[defaultCache](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching-defaultCache.html) | Returns the default cache which is added by Unity internally.  
[ready](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching-ready.html) | Returns true if Caching system is ready for use.  
### Static Methods
Method | Description  
---|---  
[AddCache](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.AddCache.html) | Add a cache with the given path.  
[ClearAllCachedVersions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.ClearAllCachedVersions.html) | Removes all the cached versions of the given AssetBundle from the cache.  
[ClearCache](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.ClearCache.html) | Removes all AssetBundle content that has been cached by the current application.  
[ClearCachedVersion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.ClearCachedVersion.html) | Removes the given version of the AssetBundle.  
[ClearOtherCachedVersions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.ClearOtherCachedVersions.html) | Removes all the cached versions of the AssetBundle from the cache, except for the specified version.  
[GetAllCachePaths](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.GetAllCachePaths.html) | Returns all paths of the cache in the cache list.  
[GetCacheAt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.GetCacheAt.html) | Returns the Cache at the given position in the cache list.  
[GetCacheByPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.GetCacheByPath.html) | Returns the Cache that has the given cache path.  
[GetCachedVersions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.GetCachedVersions.html) | Returns all cached versions of the given AssetBundle.  
[IsVersionCached](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.IsVersionCached.html) | Checks if an AssetBundle is cached.  
[MarkAsUsed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.MarkAsUsed.html) | Bumps the timestamp of a cached file to be the current time.  
[MoveCacheAfter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.MoveCacheAfter.html) | Moves the source Cache after the destination Cache in the cache list.  
[MoveCacheBefore](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.MoveCacheBefore.html) | Moves the source Cache before the destination Cache in the cache list.  
[RemoveCache](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.RemoveCache.html) | Removes the Cache from cache list.  
* * *
