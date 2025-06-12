* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache-spaceFree.html

#  [Cache](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html).spaceFree
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
spaceFree; 
### Description
Returns the number of currently unused bytes in the cache.
When the cache is empty, this value equals [Cache.maximumAvailableStorageSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache-maximumAvailableStorageSpace.html). As AssetBundles are stored in the cache, this value will decrease. Caching manages cached content based on a Least Recently Used (LRU) algorithm. If insufficient space is available in the cache to store a requested AssetBundle, the oldest AssetBundles in the cache will be iteratively removed until enough space is free for the new AssetBundle. This property does not account for total available disk space. If a user's computer has less available disk space on the drive where the cache is located than spaceFree, the full amount of spaceFree will not be usable.
* * *
