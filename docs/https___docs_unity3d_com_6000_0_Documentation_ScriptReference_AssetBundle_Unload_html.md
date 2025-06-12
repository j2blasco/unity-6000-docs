* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.Unload.html

#  [AssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html).Unload
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
public void Unload(bool unloadAllLoadedObjects); 
### Parameters
Parameter | Description  
---|---  
unloadAllLoadedObjects | Determines whether the current instances of objects loaded from the AssetBundle will also be unloaded.  
### Description
Unloads an AssetBundle freeing its data.
When `unloadAllLoadedObjects` is false, tracking data structures and any memory buffers holding content of the AssetBundle are freed, but any instances of objects loaded from the bundle remain intact.  
  
When `unloadAllLoadedObjects` is true, all objects that were loaded from the bundle are destroyed. If any GameObjects in a Scene reference the destroyed assets, these references become missing.  
  
In either case no more objects can be loaded from from the bundle unless it is reloaded.  
  
For example, if a Material `M` is loaded from AssetBundle `AB`: 
  * `AB.Unload(true)` destroys all instances of `M` referenced in the active scene.
  * `AB.Unload(false)` keeps `M` instances in memory but detaches them from `AB`, causing duplicates if `AB` is reloaded.


**Warning:** Unloading an AssetBundle that serves as a dependency for other asset bundles still in use can lead to undefined behavior. This includes serialization errors that may occur even if the dependency AssetBundle is later reloaded. To avoid such issues, ensure that an AssetBundle and all AssetBundles that depend on it are unloaded together.  
  
For more information on the different compression formats used and their impact on memory while loaded, refer to [AssetBundle compression formats](https://docs.unity3d.com/6000.0/Documentation/Manual/assetbundles-compression-format.html) .  
  
Additional resources: [UnloadAllAssetBundles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.UnloadAllAssetBundles.html), [UnloadAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.UnloadAsync.html), [Using AssetBundles Natively](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Native.html).
* * *
