* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-genuine.html

#  [Application](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.html).genuine
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
genuine; 
### Description
Returns false if application is altered in any way after it was built.
Otherwise returns true.  
  
**Note** : Use [Application.genuineCheckAvailable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-genuineCheckAvailable.html) along with `Application.genuine` to verify app integrity. Accessing the `Application.genuine` property is a resource-intensive operation, so do not call it during frame updates or other time-critical code.  
  
**Android** : Returns false if the package name set in project settings mismatches with package name returned at runtime.  
  
You can use this as an anti-piracy check because it checks if the application was altered after being built. Refer to [iOS Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/iphone-API.html) and [Android mobile scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/android-API.html) for more information.
* * *
