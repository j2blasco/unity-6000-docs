* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Analytics.AnalyticsSettings.OnRequireInBuildHandler.html

#  [AnalyticsSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Analytics.AnalyticsSettings.html).OnRequireInBuildHandler
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
Dispatches whenever a platform build starts. Use this event to enable Analytics in a platform build.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
[InitializeOnLoad]
internal class SomeNewServiceRequiresAnalyticsDeviceStats
{
    static SomeNewServiceRequiresAnalyticsDeviceStats()
    {
        UnityEditor.Analytics.AnalyticsSettings.OnRequireInBuildHandler += () =>
        {
            return true;
        };
    }
}

```

* * *
