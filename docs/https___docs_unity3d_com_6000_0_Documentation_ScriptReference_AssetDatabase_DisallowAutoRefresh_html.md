* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.DisallowAutoRefresh.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).DisallowAutoRefresh
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
public static void DisallowAutoRefresh(); 
### Description
Increments an internal counter which Unity uses to determine whether to allow automatic AssetDatabase refreshing behavior.
Unity uses this method and the corresponding AssetDatabase.AllowAutoRefresh together internally to prevent an auto-refresh from happening during certain operations. For example, Unity's version control integration uses it to prevent an auto-refresh from happening while it gets new changesets.  
  
This method is useful if you are building your own Editor tools and you want to prevent auto-refreshing of Assets during your own operations (for example, if you are building custom integration with a version control system).  
  
This method does not simply disable the auto-refresh feature. Instead it increments a counter, and only allows auto-refresh when the counter is returned to zero. Therefore, each time you call DisallowAutoRefresh, you must make sure you also make a corresponding call to AllowAutoRefresh. For example:
```
 AssetDatabase.DisallowAutoRefresh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.DisallowAutoRefresh.html)();
 // your code here, performed while auto-refresh is not allowed
 AssetDatabase.AllowAutoRefresh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.AllowAutoRefresh.html)();
```

This internal counter is used so that if your code executes multiple nested "disable" and "enable" pairs, the inner pairs do not accidentally re-enable auto-refresh too early. Instead, each pair increments and decrements the counter by one, and if your code is correctly nested, the final outer call to AllowAutoRefresh sets the counter to zero.  
  
Important Notes:  
  
This method does not influence the behaviour of AssetDatabase.Refresh. The Asset Database always performs a refresh if AssetDatabase.Refresh is called, regardless of this method and its internal counter.  
  
This method is separate from the Auto Refresh setting in Unity's Preferences window, which does not modify this internal counter. If Unity's Auto Refresh preference setting is disabled, calling Allow and Disallow still modifies the internal counter, however the Editor does not automatically refresh regardless of whether the internal counter is at zero or not.  
  
Additional resources: [AssetDatabase.AllowAutoRefresh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.AllowAutoRefresh.html).
* * *
