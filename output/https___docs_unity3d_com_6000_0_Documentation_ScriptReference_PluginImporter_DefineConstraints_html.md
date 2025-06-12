* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.DefineConstraints.html

#  [PluginImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.html).DefineConstraints
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
DefineConstraints; 
### Description
Allows you to specify a list of #define directives which controls whether your plug-in should be included.
You can set this property on each plug-in to control whether it should or shouldn't be included in your build according to the currently defined [define directives](https://docs.unity3d.com/6000.0/Documentation/Manual/platform-dependent-compilation.html).  
  
By specifying the names of one or more #define directives in an array in this property on your plug-in, you can specify that your plug-in should only be included in the build when your project defines one of those #define directives.  
  
Each plug-in in your project can have its own unique array of define constraints. This way, you can have different plug-ins included or excluded when you publish different types of builds, by changing which #define directives are set when you build.  
  
You can use the "!" character to specify that a plug-in should be included only when a certain #define directive is **not** set in the currently defined [define directives](https://docs.unity3d.com/6000.0/Documentation/Manual/platform-dependent-compilation.html). For example, including "!ExampleDefine" in the list of define constraints means that the plug-in will not be included if "ExampleDefine" is set in the project's define directives.  
  
Note: There is a similar feature which allows you to conditionally control which script assemblies are included. For more information, see the [Script Assemblies Manual Page](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-files.html).
* * *
