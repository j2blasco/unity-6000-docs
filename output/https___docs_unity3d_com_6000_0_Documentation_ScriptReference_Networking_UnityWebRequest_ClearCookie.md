* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.ClearCookieCache.html

#  [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html).ClearCookieCache
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
public static void ClearCookieCache(); 
## Declaration
public static void ClearCookieCache(Uri uri); 
### Parameters
Parameter | Description  
---|---  
uri | An optional URL to define which cookies are removed. Only cookies that apply to this URL are removed from the cache.  
### Description
Clears stored cookies from the cache.
The cookie cache exists only in the current game session and will clear the next time the game is launched, except when the below exceptions apply.  
  
This method allows you to remove cookies from the cache. If you don't specify an argument, the method removes all cookies in the cache. If you do specify a string argument, the method only removes the cookies that apply to the given URL.  
  
Exceptions: 
  * iOS has a built-in cookie cache provided by the system, which persists across game sessions. This method removes cookies from that built-in cache.
  * On the Web Platform, cookies are managed by the browser and can't be removed, so this method doesn't do anything.


* * *
