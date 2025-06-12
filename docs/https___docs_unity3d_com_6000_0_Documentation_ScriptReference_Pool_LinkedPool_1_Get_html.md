* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pool.LinkedPool_1.Get.html

#  [LinkedPool<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pool.LinkedPool_1.html).Get
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
public T Get(); 
### Returns
**T** A pooled object or a new instance if the pool is empty. 
### Description
Get an instance from the pool. If the pool is empty then a new instance will be created.
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
* * *
## Declaration
public PooledObject<T> Get(out T v); 
### Parameters
Parameter | Description  
---|---  
v | Out parameter that will contain a reference to an instance from the pool.  
### Returns
**PooledObject <T>** A PooledObject that will return the instance back to the pool when its Dispose method is called. 
### Description
Returns a PooledObject that will automatically return the instance to the pool when it is disposed.
```
using System.Text;
using UnityEngine;
using UnityEngine.Pool;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    static LinkedPool<StringBuilder> stringBuilderPool = new LinkedPool<StringBuilder>(
        () => new StringBuilder(),
        (sb) => sb.Clear());  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        StringBuilder stringBuilder;  
  
        // When the pooled object is disposed the string builder will be returned back to the pool
        using (stringBuilderPool.Get(out stringBuilder))
        {
            stringBuilder.AppendLine("Some text");
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(stringBuilder.ToString());
        }
    }
}

```

* * *
