* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache-spaceOccupied.html

#  [Cache](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html).spaceOccupied
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
spaceOccupied; 
### Description
Returns the used disk space in bytes.
Initially this is 0. As you download AssetBundles to the cache, this will increase. If insufficient space is available in the cache to store a requested AssetBundle, the least-recently-used cached AssetBundles in the cache will be iteratively removed until enough space is available for the new AssetBundle.
* * *
