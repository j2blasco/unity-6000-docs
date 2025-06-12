* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPlayerOptions-locationPathName.html

#  [BuildPlayerOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPlayerOptions.html).locationPathName
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
locationPathName; 
### Description
The path where the application will be built.
The path you specify should end with the correct extension for the file format you will build. This path won't be changed by Unity. Set the file format using [EditorUserBuildSettings.buildAppBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUserBuildSettings-buildAppBundle.html).   

  * If your file is an Android Package, end `locationPathName` with `.apk`.
  * If your file is an Android App Bundle, end `locationPathName` with `.aab`.


Additional resources: [EditorUserBuildSettings.GetBuildLocation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUserBuildSettings.GetBuildLocation.html), [Build path requirements for target platforms](https://docs.unity3d.com/6000.0/Documentation/Manual/build-path-requirements.html).
* * *
