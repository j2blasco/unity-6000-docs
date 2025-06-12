* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.IJobExtensions.RunByRef.html

#  [IJobExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.IJobExtensions.html).RunByRef
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
public static void RunByRef(ref T jobData); 
### Parameters
Parameter | Description  
---|---  
jobData | The job and data to run.  
### Description
Performs the job's Execute method immediately on the same thread by reference.
Additional resources: [IJob](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.IJob.html).
* * *
