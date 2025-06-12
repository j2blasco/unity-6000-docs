* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Recorder.FilterToCurrentThread.html

#  [Recorder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Recorder.html).FilterToCurrentThread
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
public void FilterToCurrentThread(); 
### Description
Configures the recorder to only collect data from the current thread.
By default, a Recorder collects samples from its corresponding Sampler regardless of which thread those samples occur on. Call this function to limit sample collection to the current thread only.  
  
Limiting sample collection to the current thread is particularly useful when performing tests with very commonly-used samplers (such as GC.Alloc), as ensuring that background threads are not active during the test can be difficult.  
  
Reset the Recorder to collect samples from all threads by calling [Recorder.CollectFromAllThreads](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Recorder.CollectFromAllThreads.html).  
  
Note that when you have more than one Recorder object for the same Sampler, this filter setting affects all of them. If all of these Recorder instances are destroyed, any new Recorder instances obtained for the Sampler revert to the default behavior and collect samples from all threads. However, because it is difficult to predict the timing of object destruction, always call [Recorder.CollectFromAllThreads](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Recorder.CollectFromAllThreads.html) to reset sample collection.
* * *
