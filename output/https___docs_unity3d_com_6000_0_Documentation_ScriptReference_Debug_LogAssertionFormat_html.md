* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogAssertionFormat.html

#  [Debug](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.html).LogAssertionFormat
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
public static void LogAssertionFormat(string format, params object[] args); 
## Declaration
public static void LogAssertionFormat([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) context, string format, params object[] args); 
### Parameters
Parameter | Description  
---|---  
format | A composite format string.  
args | Format arguments.  
context | Object to which the message applies.  
### Description
Logs a formatted assertion message to the Unity console.
Note that these methods work only if UNITY_ASSERTIONS symbol is defined. This means that if you are building assemblies externally, you need to define this symbol otherwise the call becomes a no-op. (For more details see [System.Diagnostics.ConditionalAttribute](https://msdn.microsoft.com/en-us/library/system.diagnostics.conditionalattribute\(v=vs.110\).aspx) on the MSDN website.
* * *
