* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorJobExtensions.AddJobDependency.html

#  [AnimatorJobExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorJobExtensions.html).AddJobDependency
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
public static void AddJobDependency([Animator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) animator, [Unity.Jobs.JobHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.html) jobHandle); 
### Parameters
Parameter | Description  
---|---  
animator | The [Animator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) instance that calls this method.  
jobHandle | The [JobHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.html) of the job that needs to run before animator jobs.  
### Description
Creates a dependency between animator jobs and the job represented by the supplied job handle. To add multiple job dependencies, call this method for each job that need to run before the Animator's jobs.
After each update the [Animator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) dependencies are flushed.
```
using UnityEngine;
using UnityEngine.Animations;
using UnityEngine.Playables;  
  
using Unity.Collections;
using Unity.Jobs;  
  
public class MyMonoBehaviour : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    NativeArray<int> input0;
    NativeArray<int> input1;
    NativeArray<int> output;  
  
    PlayableGraph[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.html) graph;
    Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) animator;  
  
    public struct SumDataForJob : IJob[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.IJob.html)
    {
        [ReadOnly[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.ReadOnly.html)]
        public NativeArray<int> input0;  
  
        [ReadOnly[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.ReadOnly.html)]
        public NativeArray<int> input1;  
  
        public NativeArray<int> output;  
  
        public void Execute()
        {
            for (var i = 0; i < output.Length; ++i)
                output[i] = input0[i] + input1[i];
        }
    }  
  
    public struct MyAnimationJob : IAnimationJob[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.IAnimationJob.html)
    {
        [ReadOnly[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.ReadOnly.html)]
        public NativeArray<int> input;  
  
        public float            sum;  
  
        public void ProcessRootMotion(AnimationStream[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream.html) stream)
        {
            sum = 0;
            for (var i = 0; i < input.Length; ++i)
                sum += input[i];
        }  
  
        public void ProcessAnimation(AnimationStream[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream.html) stream) {}
    }  
  
    public void Start()
    {
        input0 = new NativeArray<int>(10, Allocator.Persistent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.Persistent.html));
        input1 = new NativeArray<int>(10, Allocator.Persistent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.Persistent.html));
        output = new NativeArray<int>(10, Allocator.Persistent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.Persistent.html));  
  
        for (var i = 0; i < output.Length; i++)
        {
            input0[i] = i;
            input1[i] = 10 * i;
            output[i] = 0;
        }  
  
        animator = gameObject.AddComponent<Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html)>();  
  
        graph = PlayableGraph.Create[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.Create.html)();
        var myAnimationJob = new MyAnimationJob();
        myAnimationJob.input = output;  
  
        var scriptPlayable = AnimationScriptPlayable.Create[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationScriptPlayable.Create.html)(graph, myAnimationJob);
        var playableOutput = AnimationPlayableOutput.Create[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationPlayableOutput.Create.html)(graph, "output", animator);  
  
        playableOutput.SetSourcePlayable(scriptPlayable);
        graph.Play();
    }  
  
    public void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        SumDataForJob sumJob;
        sumJob.input0 = input0;
        sumJob.input1 = input1;
        sumJob.output = output;  
  
        var jobHandle = sumJob.Schedule();
        animator.AddJobDependency(jobHandle);
    }  
  
    public void OnDestroy()
    {
        graph.Destroy();
        input0.Dispose();
        input1.Dispose();
        output.Dispose();
    }
}

```

* * *
