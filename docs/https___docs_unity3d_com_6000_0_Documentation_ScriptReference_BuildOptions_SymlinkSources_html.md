* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildOptions.SymlinkSources.html

#  [BuildOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildOptions.html).SymlinkSources
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
Symlink sources when generating the project. This is useful if you're changing source files inside the generated project and want to bring the changes back into your Unity project or a package.
This option affects sources in both Unity projects and packages. Only the following platforms support this option:  
  
**iOS** : When `symlinkSources` is enabled, Unity creates symlinks for libraries (libil2cpp.a, libiPhone-lib.a, etc.). This means you don't need to copy the libraries. Sources with .mm, .m, .cpp, .c, .h, .swift, and .xib extensions are referenced externally from Xcode project.  
  
**Android** : When `symlinkSources` is enabled, Gradle project references .java, .kt and .androidlib plug-in sources externally from Unity project rather than copying the source files directly into the Gradle project. In case of .androidlib plug-in, the plug-in folder must include `build.gradle` file for the `symlinkSources` option to work.  
  
Additional resources: [BuildPipeline.BuildPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.BuildPlayer.html), [EditorUserBuildSettings.symlinkSources](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUserBuildSettings-symlinkSources.html).
* * *
