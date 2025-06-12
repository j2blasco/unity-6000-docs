* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pool.LinkedPool_1.html

# LinkedPool<T0>
class in UnityEngine.Pool
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
Leave feedback
  

Implements interfaces:[IObjectPool<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pool.IObjectPool_1.html)
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
A linked list version of [IObjectPool<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pool.IObjectPool_1.html).
Object Pooling is a way to optimize your projects and lower the burden that is placed on the CPU when having to rapidly create and destroy new objects. It is a good practice and design pattern to keep in mind to help relieve the processing power of the CPU to handle more important tasks and not become inundated by repetitive create and destroy calls. The LinkedPool uses a linked list to hold a collection of object instances for reuse. Note this is not thread-safe.
```
using System.Text;
using UnityEngine;
using UnityEngine.Pool;  
  
// This component returns the particle system to the pool when the OnParticleSystemStopped event is received.
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)))]
public class ReturnToPool : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html) system;
    public IObjectPool<ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)> pool;  
  
    void Start()
    {
        system = GetComponent<ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)>();
        var main = system.main;
        main.stopAction = ParticleSystemStopAction.Callback[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemStopAction.Callback.html);
    }  
  
    void OnParticleSystemStopped()
    {
        // Return to the pool
        pool.Release(system);
    }
}  
  
// This example spans a random number of ParticleSystems using a pool so that old systems can be reused.
public class PoolExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public enum PoolType
    {
        Stack,
        LinkedList
    }  
  
    public PoolType poolType;  
  
    // Collection checks will throw errors if we try to release an item that is already in the pool.
    public bool collectionChecks = true;
    public int maxPoolSize = 10;  
  
    IObjectPool<ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)> m_Pool;  
  
    public IObjectPool<ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)> Pool
    {
        get
        {
            if (m_Pool == null)
            {
                if (poolType == PoolType.Stack)
                    m_Pool = new ObjectPool<ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)>(CreatePooledItem, OnTakeFromPool, OnReturnedToPool, OnDestroyPoolObject, collectionChecks, 10, maxPoolSize);
                else
                    m_Pool = new LinkedPool<ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)>(CreatePooledItem, OnTakeFromPool, OnReturnedToPool, OnDestroyPoolObject, collectionChecks, maxPoolSize);
            }
            return m_Pool;
        }
    }  
  
    ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html) CreatePooledItem()
    {
        var go = new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)("Pooled Particle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle.html) System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html)");
        var ps = go.AddComponent<ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)>();
        ps.Stop(true, ParticleSystemStopBehavior.StopEmittingAndClear[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemStopBehavior.StopEmittingAndClear.html));  
  
        var main = ps.main;
        main.duration = 1;
        main.startLifetime = 1;
        main.loop = false;  
  
        // This is used to return ParticleSystems to the pool when they have stopped.
        var returnToPool = go.AddComponent<ReturnToPool>();
        returnToPool.pool = Pool;  
  
        return ps;
    }  
  
    // Called when an item is returned to the pool using Release
    void OnReturnedToPool(ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html) system)
    {
        system.gameObject.SetActive(false);
    }  
  
    // Called when an item is taken from the pool using Get
    void OnTakeFromPool(ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html) system)
    {
        system.gameObject.SetActive(true);
    }  
  
    // If the pool capacity is reached then any items returned will be destroyed.
    // We can control what the destroy behavior does, here we destroy the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).
    void OnDestroyPoolObject(ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html) system)
    {
        Destroy(system.gameObject);
    }  
  
    void OnGUI()
    {
        GUILayout.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Label.html)("Pool size: " + Pool.CountInactive);
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Create Particles"))
        {
            var amount = Random.Range[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.Range.html)(1, 10);
            for (int i = 0; i < amount; ++i)
            {
                var ps = Pool.Get();
                ps.transform.position = Random.insideUnitSphere[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random-insideUnitSphere.html) * 10;
                ps.Play();
            }
        }
    }
}

```

### Properties
Property | Description  
---|---  
[CountInactive](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pool.LinkedPool_1.CountInactive.html) | Number of objects that are currently available in the pool.  
### Constructors
Constructor | Description  
---|---  
[LinkedPool_1](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pool.LinkedPool_1-ctor.html) | Creates a new LinkedPool instance.  
### Public Methods
Method | Description  
---|---  
[Clear](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pool.LinkedPool_1.Clear.html) | Removes all pooled items. If the pool contains a destroy callback then it will be called for each item that is in the pool.  
[Dispose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pool.LinkedPool_1.Dispose.html) | Removes all pooled items. If the pool contains a destroy callback then it will be called for each item that is in the pool.  
[Get](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pool.LinkedPool_1.Get.html) | Get an instance from the pool. If the pool is empty then a new instance will be created.  
[Release](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pool.LinkedPool_1.Release.html) | Returns the instance back to the pool.  
* * *
