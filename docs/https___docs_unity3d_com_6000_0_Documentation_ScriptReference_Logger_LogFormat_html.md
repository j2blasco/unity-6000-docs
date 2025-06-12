* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Logger.LogFormat.html

#  [Logger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Logger.html).LogFormat
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
public void LogFormat([LogType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LogType.html) logType, string format, params object[] args); 
## Declaration
public void LogFormat([LogType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LogType.html) logType, [Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) context, string format, params object[] args); 
### Parameters
Parameter | Description  
---|---  
logType | The type of the log message.  
context | Object to which the message applies.  
format | A composite format string.  
args | Format arguments.  
### Description
Logs a formatted message.
For formatting details, see the MSDN documentation on Composite Formatting. Rich text markup can be used to add emphasis. See the manual page about [rich text](https://docs.unity3d.com/6000.0/Documentation/Manual/StyledText.html) for details of the different markup tags available.
* * *
