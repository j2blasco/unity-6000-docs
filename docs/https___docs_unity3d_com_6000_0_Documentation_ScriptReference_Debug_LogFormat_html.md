* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogFormat.html

#  [Debug](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.html).LogFormat
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Debug.html "Go to Debug Component in the Manual")
## Declaration
public static void LogFormat(string format, params object[] args); 
## Declaration
public static void LogFormat([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) context, string format, params object[] args); 
## Declaration
public static void LogFormat([LogType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LogType.html) logType, [LogOption](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LogOption.html) logOptions, [Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) context, string format, params object[] args); 
### Parameters
Parameter | Description  
---|---  
format | A composite format string.  
args | Format arguments.  
context | Object to which the message applies.  
logType | Type of message e.g. warn or error etc.  
logOptions | Option flags to treat the log message special.  
### Description
Logs a formatted message to the Unity Console.
For formatting details, see the MSDN documentation on Composite Formatting. Rich text markup can be used to add emphasis. See the manual page about [rich text](https://docs.unity3d.com/6000.0/Documentation/Manual/StyledText.html) for details of the different markup tags available.  
  
Additional resources: [Debug.unityLogger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug-unityLogger.html), [ILogger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ILogger.html).
* * *
