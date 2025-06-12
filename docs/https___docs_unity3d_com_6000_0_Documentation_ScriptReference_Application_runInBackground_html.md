* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-runInBackground.html

#  [Application](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.html).runInBackground
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
runInBackground; 
### Description
Determines whether the Player should run when the application is in the background
By default, this is set to false and the application pauses when it is in the background.  
  
**Android** : This property works in Android only if the application is visible, but not when it's in focused state. For example, when the app is run in [ multi-window mode](https://developer.android.com/reference/android/app/Activity.html#isInMultiWindowMode\(\)), such as Samsung Dex and Oculus Quest 2. If the application is running in [background](https://developer.android.com/guide/background), it pauses regardless of the `Application.runInBackground` option. If you want to execute tasks while it is in background, you need to implement the [background service](https://developer.android.com/training/run-background-service/create-service).  
  
**iOS** : This property is ignored on iOS.  
  
**Web** : On Web, the update loop runs at approximately one update per second when the application is running in the background. In addition, mobile browsers might pause the application if the screen is locked, even with this option enabled.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html) 
{
    void Example() 
    {
        Application.runInBackground[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-runInBackground.html) = true;
    }
}

```

* * *
