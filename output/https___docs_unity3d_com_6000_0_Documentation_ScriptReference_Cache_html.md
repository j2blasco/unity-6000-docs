* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html

# Cache
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
Data structure for cache. For more information, see [Caching.AddCache](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.AddCache.html).
**Note:** The Cache API is not supported in WebGL because AssetBundles are stored in the browser cache for the WebGL platform.
### Properties
Property | Description  
---|---  
[expirationDelay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache-expirationDelay.html) | The number of seconds that an AssetBundle may remain unused in the cache before it is automatically deleted.  
[index](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache-index.html) | Returns the index of the cache in the cache list.  
[maximumAvailableStorageSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache-maximumAvailableStorageSpace.html) | Allows you to specify the total number of bytes that can be allocated for the cache.  
[path](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache-path.html) | Returns the path of the cache.  
[readOnly](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache-readOnly.html) | Returns true if the cache is readonly.  
[ready](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache-ready.html) | Returns true if the cache is ready.  
[spaceFree](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache-spaceFree.html) | Returns the number of currently unused bytes in the cache.  
[spaceOccupied](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache-spaceOccupied.html) | Returns the used disk space in bytes.  
[valid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache-valid.html) | Returns true if the cache is valid.  
### Public Methods
Method | Description  
---|---  
[ClearCache](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.ClearCache.html) | Removes all cached content in the cache that has been cached by the current application.  
* * *
