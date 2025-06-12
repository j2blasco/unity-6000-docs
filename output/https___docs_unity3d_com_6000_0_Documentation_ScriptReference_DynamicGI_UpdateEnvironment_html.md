* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DynamicGI.UpdateEnvironment.html

#  [DynamicGI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DynamicGI.html).UpdateEnvironment
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
public static void UpdateEnvironment(); 
### Description
Schedules an update of the environment cubemap.
When you use this signature, Unity schedules an update of the environment cubemap.  
Query [SystemInfo.supportsAsyncGPUReadback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsAsyncGPUReadback.html) to determine if the system currently running Unity supports asynchronous readbacks. If the system supports these readbacks, Unity reads back the environment cubemap while waiting for the lighting result, but may lag one or more frames behind. You can schedule a limited number of environment readbacks. If you schedule updates in incremements more frequent than Unity can perform the readback, Unity silently ignores the request.  
If the current system does not support asynchronous readbacks, environment cubemap readback stalls the current thread, and Unity reads and processes each face of the cubemap one by one. An alternative to environment cubemap updates is to set the cubemap updates manually with [DynamicGI.SetEnvironmentData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DynamicGI.SetEnvironmentData.html). 
* * *
