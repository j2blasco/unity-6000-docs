* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.CompilationPipeline.ParseResponseFile.html

#  [CompilationPipeline](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.CompilationPipeline.html).ParseResponseFile
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
public static [Compilation.ResponseFileData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.ResponseFileData.html) ParseResponseFile(string relativePath, string projectDirectory, string[] systemReferenceDirectories); 
### Parameters
Parameter | Description  
---|---  
relativePath | The path to the response file to be parsed.  
projectDirectory | The absolute path to the root of the Project directory in which the response file is located.  
systemReferenceDirectories | Array of directories containing system reference libraries.  
### Returns
**ResponseFileData** Describes the content of the response file that was parsed. Errors, defines, etc. 
### Description
Retrieves the [ResponseFileData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.ResponseFileData.html) describing the content of the response file.
* * *
