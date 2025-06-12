* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.UnloadAllAssetBundles.html

#  [AssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html).UnloadAllAssetBundles
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
public static void UnloadAllAssetBundles(bool unloadAllObjects); 
### Parameters
Parameter | Description  
---|---  
unloadAllObjects | Determines whether the current instances of objects loaded from AssetBundles will also be unloaded.  
### Description
Unloads all currently loaded AssetBundles.
When `unloadAllObjects` is false, tracking data structures and any memory buffers holding content of the AssetBundle will be freed. But any instances of objects loaded from this bundle will remain intact.  
  
When `unloadAllObjects` is true, all objects that were loaded from the currently loaded bundles will be destroyed as well. If there are GameObjects in your Scene referencing those assets, the references to them will become missing.  
  
In either case you won't be able to load any more objects from the currently loaded bundles unless they are reloaded.  
  
**Note:** Passing a value of `false` for `unloadAllObjects` can cause unexpected behavior in the Editor. For example, the [Mip Map Streaming](https://docs.unity3d.com/6000.0/Documentation/Manual/TextureStreaming.html) system might still reference textures loaded from a bundle after exiting play mode. This means when the Mip Map streaming system tries to update each texture's mipmaps, it can't access the unloaded bundle and displays errors in the console. To avoid this, use [conditional compilation](https://docs.unity3d.com/6000.0/Documentation/Manual/platform-dependent-compilation.html) to pass `true` in the Editor, and `false` in builds. See [AssetBundles compression](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Cache.html) for a description of the different compression formats used and their impact on memory while loaded.  
  
Additional resources: [Unload](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.Unload.html), [UnloadAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.UnloadAsync.html), [Using AssetBundles Natively](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Native.html).
* * *
