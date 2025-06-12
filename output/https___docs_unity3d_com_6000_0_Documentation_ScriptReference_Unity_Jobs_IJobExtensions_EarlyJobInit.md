* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.IJobExtensions.EarlyJobInit.html

#  [IJobExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.IJobExtensions.html).EarlyJobInit
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
public static void EarlyJobInit(); 
### Description
Gathers and caches reflection data for the internal job system's managed bindings.
Unity is responsible for calling this method: don't call it yourself. When the Jobs package is included in the project, Unity generates code to call EarlyJobInit at startup. This results in the following benefits: 
  * Job initialization doesn't lazily occur during job scheduling, which would increase the time it takes to schedule a job.
  * Burst compiled code may schedule jobs because the reflection part of initialization, which is not compatible with Burst compiler constraints, has already happened in EarlyJobInit.


**Note** : While the Jobs package code generator handles this automatically for all closed job types, you must register those with generic arguments (like IJob&lt;MyJobType&lt;T&gt;&gt;) manually for each specialization with Unity.Jobs.RegisterGenericJobTypeAttribute.
* * *
