* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-backButtonLeavesApp.html

#  [Input](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.html).backButtonLeavesApp
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
backButtonLeavesApp; 
### Description
Should **Back** button quit the application?
**Note** : This API is part of the legacy Input Manager. The recommended best practice is that you don't use this API in new projects. For new projects, use the Input System package. To learn more about input, refer to [Input](https://docs.unity3d.com/6000.0/Documentation/Manual/Input.html).  
  
Only usable on Android or Universal Windows Platform (UWP).  
  
By default this property is set to false, which means you're responsible for responding to **Back** button. You can do this by calling [Input.GetKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKey.html) and passing [KeyCode.Escape](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Escape.html).  
  
If you set this property to true, clicking the **Back** button:   
* minimizes the application on Android.   
* suspends the application on UWP.
* * *
