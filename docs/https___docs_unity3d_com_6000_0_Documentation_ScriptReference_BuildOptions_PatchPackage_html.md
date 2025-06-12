* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildOptions.PatchPackage.html

#  [BuildOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildOptions.html).PatchPackage
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
Patch a [Development](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildOptions.Development.html) app package rather than completely rebuilding it.  
  
Supported only on Android platform.
Use the `PatchPackage` option in your build script to rebuild and deploy project changes. Patching an existing deployment can be significantly faster than rebuilding the entire application. Only [Development](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildOptions.Development.html) builds can be patched.  
  
To patch a package, build the project using the following options in your build script: `BuildOptions.PatchPackage` or [BuildOptions.Development](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildOptions.Development.html). Alternatively, you can click the **Patch** or **Patch And Run** buttons on the **Build Settings** window.  
  
This option will implicitly change some options to enhance performance of deployment. The application will not be split using expansion files (such as OBB).
* * *
