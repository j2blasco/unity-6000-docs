* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ProcessService.EnableProfileConnection.html

#  [ProcessService](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ProcessService.html).EnableProfileConnection
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
public static int EnableProfileConnection(string dataPath); 
### Parameters
Parameter | Description  
---|---  
dataPath | Where to save profiling data. Normally this is set to [Application.dataPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-dataPath.html).  
### Returns
**int** Greater than 0 if successful. 
### Description
Enables a connection to the Profiler. The standalone Profiler uses this method.
* * *
