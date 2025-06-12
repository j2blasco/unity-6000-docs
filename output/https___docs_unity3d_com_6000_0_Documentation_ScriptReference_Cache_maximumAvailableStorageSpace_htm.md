* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache-maximumAvailableStorageSpace.html

#  [Cache](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html).maximumAvailableStorageSpace
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
maximumAvailableStorageSpace; 
### Description
Allows you to specify the total number of bytes that can be allocated for the cache.
This value can be set to a smaller number in order to limit the amount of storage space used by cached AssetBundles. PC/Mac Standalone applications and iOS/Android applications have a limit of 4 GiB. This property does not account for total available storage space. If a user's computer has less available storage space on the drive where the cache is located than maximumAvailableStorageSpace, the full amount of maximumAvailableStorageSpace will not be usable. Cache storage is allocated on an as-needed basis in order to minimize storage space usage.
* * *
