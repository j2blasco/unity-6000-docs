* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ProcessService.ReadParameter.html

#  [ProcessService](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ProcessService.html).ReadParameter
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
public static string ReadParameter(string paramName); 
### Parameters
Parameter | Description  
---|---  
paramName | Specific name of a command line parameter.  
### Returns
**string** The parameter value. If empty, the parameter wasn't used on the command line. 
### Description
A utility function to read command line arguments passed to the current process.
* * *
