* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache-expirationDelay.html

#  [Cache](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html).expirationDelay
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
expirationDelay; 
### Description
The number of seconds that an AssetBundle may remain unused in the cache before it is automatically deleted.
This value defaults to 150 days (12,960,000 seconds). Lower values will cause the cache to be cleaned more aggressively in order to minimize disk storage usage. The delay cannot be set greater than 12,960,000 seconds.
* * *
