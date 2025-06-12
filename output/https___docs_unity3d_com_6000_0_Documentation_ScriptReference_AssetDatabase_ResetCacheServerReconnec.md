* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.ResetCacheServerReconnectTimer.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).ResetCacheServerReconnectTimer
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
public static void ResetCacheServerReconnectTimer(); 
### Description
Resets the internal cache server connection reconnect timer values. The default delay timer value is 1 second, and the max delay value is 5 minutes. Everytime a connection attempt fails it will double the delay timer value, until a maximum time of the max value.
* * *
