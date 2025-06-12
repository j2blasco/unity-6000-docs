* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.IScriptableBakedReflectionSystem.html

**Experimental** : this API is experimental and might be changed or removed in the future.
# IScriptableBakedReflectionSystem
interface in UnityEditor.Experimental.Rendering
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
### Description
Defines the required members for a ScriptableBakedReflectionSystem implementation.
You can use the empty implementation as base class, see [ScriptableBakedReflectionSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.ScriptableBakedReflectionSystem.html).
```
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Rendering;
using UnityEditor.Experimental.Rendering;  
  
public interface IBakeJobs
{
    // Add job counts + remove jobs count
    int count { get; }
    int toAddCount { get; }
    int toRemoveCount { get; }
}  
  
public interface IBaker<TProbe>
{
    IBakeJobs PrepareBakeJobsFor(SceneStateHash[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.SceneStateHash.html) sceneStateHash);
    void IssueJobs(IBakeJobs jobs);
    List<TProbe> bakedProbes { get; set; }
    void StopRunningJobs();
}  
  
abstract class CustomScriptableBakedReflectionSystem : ScriptableBakedReflectionSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.ScriptableBakedReflectionSystem.html)
{
    enum Stage[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Stage.html)
    {
        None,
        BakeReflectionProbes
    }  
  
    IBaker<ReflectionProbe[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe.html)> m_ReflectionProbeBaker;  
  
    public CustomScriptableBakedReflectionSystem(
        IBaker<ReflectionProbe[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe.html)> reflectionProbeBaker)
    // Our custom system processes in 1 stage: reflection probes
        : base(1)
    {
        m_ReflectionProbeBaker = reflectionProbeBaker;
    }  
  
    public override void Tick(
        SceneStateHash[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.SceneStateHash.html) sceneStateHash,
        IScriptableBakedReflectionSystemStageNotifier[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.IScriptableBakedReflectionSystemStageNotifier.html) handle)
    {
        // Reflection Probes
        {
            // Calculate reflection probes to remove and to bake and add
            var jobs = m_ReflectionProbeBaker.PrepareBakeJobsFor(sceneStateHash);
            if (jobs.count > 0)
            {
                // Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html) progression information of current stage
                // Progress[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.html) is the progression of to bake and add jobs
                handle.EnterStage(
                    (int)Stage.BakeReflectionProbes,
                    string.Format("Reflection Probes | {0} jobs", jobs.toAddCount),
                    1 - (jobs.toAddCount / (float)m_ReflectionProbeBaker.bakedProbes.Count));  
  
                // Perform removal of remove jobs
                // Issue baking of add jobs if they are not in progress
                m_ReflectionProbeBaker.IssueJobs(jobs);  
  
                return;
            }
            handle.ExitStage((int)Stage.BakeReflectionProbes);
        }  
  
        // Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html) the hash of the reflection system
        stateHashes = CalculateStateHash();
        // Baking is complete for this sceneStateHash
        handle.SetIsDone(true);
    }  
  
    public override void SynchronizeReflectionProbes()
    {
        // Synchronize Reflection Probes
        for (int i = 0, c = m_ReflectionProbeBaker.bakedProbes.Count; i < c; ++i)
        {
            var probe = m_ReflectionProbeBaker.bakedProbes[i];
            probe.bakedTexture = GetReflectionProbeBakedTexture(probe);
        }
    }  
  
    public override void Clear()
    {
        m_ReflectionProbeBaker.bakedProbes.Clear();
        DeleteBakedReflectionProbeTextures();
    }  
  
    public override void Cancel()
    {
        m_ReflectionProbeBaker.StopRunningJobs();
    }  
  
    Cubemap[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cubemap.html) GetReflectionProbeBakedTexture(ReflectionProbe[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe.html) probe)
    {
        throw new System.NotImplementedException();
    }  
  
    protected abstract void DeleteBakedReflectionProbeTextures();
    protected abstract Hash128[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Hash128.html)[] CalculateStateHash();
}

```

### Properties
Property | Description  
---|---  
[stageCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.IScriptableBakedReflectionSystem-stageCount.html) | Number of stages of the baking process.  
[stateHashes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.IScriptableBakedReflectionSystem-stateHashes.html) | The hashes of the current baked state of the ScriptableBakedReflectionSystem.  
### Public Methods
Method | Description  
---|---  
[BakeAllReflectionProbes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.IScriptableBakedReflectionSystem.BakeAllReflectionProbes.html) | Implement this method to bake all of the loaded reflection probes.  
[Cancel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.IScriptableBakedReflectionSystem.Cancel.html) | Cancel the running bake jobs.  
[Clear](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.IScriptableBakedReflectionSystem.Clear.html) | Clear the state of the ScriptableBakedReflectionSystem.  
[SynchronizeReflectionProbes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.IScriptableBakedReflectionSystem.SynchronizeReflectionProbes.html) | Synchronize the baked data with the actual components and rendering settings.  
[Tick](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.IScriptableBakedReflectionSystem.Tick.html) | This method is called every Editor update until the ScriptableBakedReflectionSystem indicates that the baking is complete, with handle.SetIsDone(true). (See IScriptableBakedReflectionSystemStageNotifier.SetIsDone).  
* * *
