* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.Dispatcher.Enqueue.html

#  [Dispatcher](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.Dispatcher.html).Enqueue
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
public static void Enqueue([Unity.Android.Gradle.Manifest.Action](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) action); 
## Declaration
public static void Enqueue([Unity.Android.Gradle.Manifest.Action](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) action, double delayInSeconds); 
### Parameters
Parameter | Description  
---|---  
action | Action to be executed in the main thread later.  
delay | Minimum amount of time in seconds for which the main thread will wait before executing the enqueued action.  
### Description
This function can be used in a thread to enqueue an action that will be executed later in the main thread.
* * *
