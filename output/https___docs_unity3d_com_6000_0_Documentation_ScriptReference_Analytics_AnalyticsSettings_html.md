* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Analytics.AnalyticsSettings.html

# AnalyticsSettings
class in UnityEditor.Analytics
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
Editor API for the Unity Services editor feature. Normally Analytics is enabled from the Services window, but if writing your own editor extension, this API can be used.
### Static Properties
Property | Description  
---|---  
[configUrl](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Analytics.AnalyticsSettings-configUrl.html) | Set the Analytics config end point.  
[dashboardUrl](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Analytics.AnalyticsSettings-dashboardUrl.html) | Get the Analytics dashboard endpoint.  
[deviceStatsEnabledInBuild](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Analytics.AnalyticsSettings-deviceStatsEnabledInBuild.html) | Reports whether device stats are enabled at runtime.  
[enabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Analytics.AnalyticsSettings-enabled.html) | If set to true, this Boolean field enables the Analytics feature in Unity. It disables the feature if it is set to false.  
[eventUrl](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Analytics.AnalyticsSettings-eventUrl.html) | Set the Analytics event end point.  
[initializeOnStartup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Analytics.AnalyticsSettings-initializeOnStartup.html) | Controls whether Unity initializes Analytics immediately on startup.  
[testMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Analytics.AnalyticsSettings-testMode.html) | Set to true for testing Analytics integration only within the Editor.  
### Events
Event | Description  
---|---  
[OnRequireInBuildHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Analytics.AnalyticsSettings.OnRequireInBuildHandler.html) | Dispatches whenever a platform build starts. Use this event to enable Analytics in a platform build.  
### Delegates
Delegate | Description  
---|---  
[RequireInBuildDelegate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Analytics.AnalyticsSettings.RequireInBuildDelegate.html) | Defines the delegate signature to handle AnalyticsSettings.RequireInBuildDelegate events.  
* * *
