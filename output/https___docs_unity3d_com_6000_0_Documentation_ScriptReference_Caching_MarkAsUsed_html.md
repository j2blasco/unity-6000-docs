* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.MarkAsUsed.html

#  [Caching](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.html).MarkAsUsed
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
**Obsolete** Please use MarkAsUsed with Hash128 instead.
## Declaration
public static bool MarkAsUsed(string url, int version); 
### Description
Bumps the timestamp of a cached file to be the current time.
This allows you to keep files in the cache even if you are not explicitly loading them. Returns true if the url is cached.
* * *
