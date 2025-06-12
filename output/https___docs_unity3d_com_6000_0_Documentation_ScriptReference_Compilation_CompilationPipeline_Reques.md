* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.CompilationPipeline.RequestScriptCompilation.html

#  [CompilationPipeline](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.CompilationPipeline.html).RequestScriptCompilation
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
public static void RequestScriptCompilation(); 
## Declaration
public static void RequestScriptCompilation([Compilation.RequestScriptCompilationOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.RequestScriptCompilationOptions.html) options); 
### Parameters
Parameter | Description  
---|---  
options | Optional parameter to specify whether the Editor should clear the build cache before compilation.  
### Description
Allows you to request that the Editor recompile scripts in the project.
When you call this method, the Unity Editor checks whether there have been any changes to scripts, or to settings affecting script compilation, and recompiles those scripts which require it. After the compilation, if the compilation was successful, the Unity Editor reloads all assemblies. If you want to force recompilation of all scripts, even if there are no changes, you can pass [RequestScriptCompilationOptions.CleanBuildCache](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.RequestScriptCompilationOptions.CleanBuildCache.html) for the options parameter. You may want to force recompilation of all scripts in the following situations: - If you have a successful compilation, but want to see all compiler warnings again. - If you have a setup where the compilation pipeline takes input from files that Unity cannot track (this is possible in rare circumstances when using response files). - If there is a bug or suspected bug in the compilation pipeline causing it to not pick up changes.
* * *
