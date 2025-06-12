* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.Dispose.html

#  [PropertyDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.html).Dispose
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
public void Dispose(); 
### Description
Dispose of the resources used by this [PropertyDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.html).
You should try to always call dispose when you no longer need the [PropertyDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.html). Even if it is recommended to keep the [PropertyDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.html) alive as much as possible and use the [views](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.IPropertyDatabaseView.html) when accessing it, calling dispose will make sure that the lock that prevents multiple openings on the same file will be removed properly. It also helps removing pressure on the C# garbage collection by preventing the finalizer from being called.
* * *
