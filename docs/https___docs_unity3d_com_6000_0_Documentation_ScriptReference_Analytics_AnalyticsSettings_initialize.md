* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Analytics.AnalyticsSettings-initializeOnStartup.html

#  [AnalyticsSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Analytics.AnalyticsSettings.html).initializeOnStartup
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
initializeOnStartup; 
### Description
Controls whether Unity initializes Analytics immediately on startup.
Set this property to false to delay the initialization of Analytics until you call [Analytics.ResumeInitialization](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Analytics.Analytics.ResumeInitialization.html). For example, if you want to ask the player to opt-in to analytics data collection, set this property to false in an Editor script, ask the player, and then only call `ResumeInitialization` if they approve.  
  
By default `InitializeOnStartup` is true. You can change the value in the Editor using a build script.  
  
Additional resources: [Analytics.Analytics.InitializeOnStartup]], [Analytics.ResumeInitialization](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Analytics.Analytics.ResumeInitialization.html)
* * *
