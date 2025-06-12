* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.IProcessSceneWithReport.html

# IProcessSceneWithReport
interface in UnityEditor.Build
Leave feedback
  

Implements interfaces:[IOrderedCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.IOrderedCallback.html)
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
Implement this interface to receive a callback for each Scene during the build.
Note that if the scene or related content in the project is unchanged from the previous player build, the scene will not be built and instead cached player build data will be used. In this case the callback will not be called.
### Public Methods
Method | Description  
---|---  
[OnProcessScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.IProcessSceneWithReport.OnProcessScene.html) | Implement this function to receive a callback for each Scene during the build.  
* * *
