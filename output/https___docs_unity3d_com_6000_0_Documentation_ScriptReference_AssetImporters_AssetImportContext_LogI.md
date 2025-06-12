* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext.LogImportWarning.html

#  [AssetImportContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext.html).LogImportWarning
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
public void LogImportWarning(string msg, [Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) obj); 
### Parameters
Parameter | Description  
---|---  
msg | The warning message.  
obj | Optional Object that is targeted by the warning.  
### Description
Logs a warning message encountered during import.
Use this method to warn the user of a non-critical issue. This method outputs to the console. Traces in the console are linked to the asset.
* * *
