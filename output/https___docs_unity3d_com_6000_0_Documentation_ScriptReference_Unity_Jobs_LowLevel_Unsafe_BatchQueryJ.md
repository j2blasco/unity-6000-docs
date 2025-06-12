* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.LowLevel.Unsafe.BatchQueryJob_2-ctor.html

#  [BatchQueryJob<T0,T1>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.LowLevel.Unsafe.BatchQueryJob_2.html).BatchQueryJob(NativeArray<CommandT> commands, NativeArray<ResultT> results)
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
### Parameters
Parameter | Description  
---|---  
commands | A [NativeArray<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.html) that contains the commands to execute during a batch. The job that executes the query only reads from this native array, and doesn't write to it.  
results | A [NativeArray<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.html) to contain the results from the commands. The job that executes the query writes to this native array.  
### Description
Initializes and returns an instance of [BatchQueryJob<T0,T1>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.LowLevel.Unsafe.BatchQueryJob_2.html).
* * *
