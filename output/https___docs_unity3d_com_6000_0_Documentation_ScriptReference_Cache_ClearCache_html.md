* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.ClearCache.html

#  [Cache](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html).ClearCache
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
public bool ClearCache(); 
## Declaration
public bool ClearCache(int expiration); 
### Parameters
Parameter | Description  
---|---  
expiration | The number of seconds that AssetBundles may remain unused in the cache.  
### Returns
**bool** Returns True when cache clearing succeeded. 
### Description
Removes all cached content in the cache that has been cached by the current application.
Returns false if any cached bundle is in use.
* * *
