* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-genuineCheckAvailable.html

#  [Application](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.html).genuineCheckAvailable
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
genuineCheckAvailable; 
### Description
Returns true if application integrity can be confirmed.
Otherwise returns false.  
  
**Note** : Use `Application.genuineCheckAvailable` along with [Application.genuine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-genuine.html) to verify app integrity. Accessing the [Application.genuine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-genuine.html) property is a resource-intensive operation, so do not call it during frame updates or other time-critical code.  
  
You can use this as part of an anti-piracy check. Refer to [iOS Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/iphone-API.html) and [Android mobile scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/android-API.html) for more information.
* * *
