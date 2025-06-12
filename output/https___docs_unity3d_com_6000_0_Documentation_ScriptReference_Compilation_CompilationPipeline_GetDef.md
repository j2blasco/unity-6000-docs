* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.CompilationPipeline.GetDefinesFromAssemblyName.html

#  [CompilationPipeline](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.CompilationPipeline.html).GetDefinesFromAssemblyName
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
public static string[] GetDefinesFromAssemblyName(string assemblyName); 
### Parameters
Parameter | Description  
---|---  
assemblyName | The name of the assembly without the extension.  
### Returns
**string[]** A string array of #define directives declared for the assembly. Returns null if the assembly is not found. 
### Description
Lists all the #define directives used to compile the specified assembly.
Additional resources: [Assembly](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.Assembly.html), [CompilationPipeline](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.CompilationPipeline.html).
* * *
