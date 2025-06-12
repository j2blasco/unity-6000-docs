* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.CompilationPipeline.IsDefineConstraintsCompatible.html

#  [CompilationPipeline](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.CompilationPipeline.html).IsDefineConstraintsCompatible
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
public static bool IsDefineConstraintsCompatible(string[] defines, string[] defineConstraints); 
### Parameters
Parameter | Description  
---|---  
defines | A string array of #define directives.  
defineConstraints | A string array of #define directives to to check compatibility against.  
### Returns
**bool** True if the specified #define constraints are satisfied by the specified #define directives. Otherwise returns False. 
### Description
Allows you to test whether the specified #define constraints are satisfied by the specified list of #define directives.
Additional resources: [Assembly](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.Assembly.html), [CompilationPipeline](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.CompilationPipeline.html).
* * *
