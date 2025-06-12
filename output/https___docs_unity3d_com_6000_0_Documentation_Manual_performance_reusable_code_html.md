* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/performance-reusable-code.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Code optimization](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-optimization.html)
  * [Optimizing your code for managed memory](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-optimizing-code-managed-memory.html)
  * Using coding patterns with reusable memory 


[](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-reference-types.html)
Reference type management
[](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-optimizing-arrays.html)
Optimizing arrays
# Using coding patterns with reusable memory
One way to avoid unnecessary allocations on the managed heap is to adopt coding patterns that allow you to reuse parts of your memory allocations. The following examples outline approaches that can help improve the performance of your application.
## Use reusable object pools
There are a lot of cases where you can reduce the number of times that your application creates and destroys objects, to avoid generating garbage. There are certain types of objects in games, such as projectiles, which might appear over and over again even though only a small number are ever in play at once. In cases like this, you can reuse the objects, rather than destroy old ones and replace them with new ones. 
For example, it’s not optimal to instantiate a new projectile object from a **prefab** An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Prefab) every time one is fired. Instead, you can calculate the maximum number of projectiles that might ever exist simultaneously during gameplay, and instantiate an array of objects of the correct size when the game first enters the gameplay **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene). To do this:
  1. Start with all the projectile **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) set to inactive.
  2. When a projectile is fired, search through the array to find the first inactive projectile in the array, move it to the required position and set the GameObject to active.
  3. When the projectile is destroyed, set the GameObject to inactive again.


The [`ObjectPool`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pool.ObjectPool_1.html) class provides an implementation of this reusable object pool technique, which is the easiest way to implement an object pool in your application. 
However, if you’re using a version of Unity that doesn’t contain the `ObjectPool` API, or you’d like to understand how you can implement a custom object pool, the following code shows a simple implementation of a stack-based object pool:
```
using System.Collections.Generic;
using UnityEngine;

public class ExampleObjectPool : MonoBehaviour {

   public GameObject PrefabToPool;
   public int MaxPoolSize = 10;
  
   private Stack<GameObject> inactiveObjects = new Stack<GameObject>();
  
   void Start() {
       if (PrefabToPool != null) {
           for (int i = 0; i < MaxPoolSize; ++i) {
               var newObj = Instantiate(PrefabToPool);
               newObj.SetActive(false);
               inactiveObjects.Push(newObj);
           }
       }
   }

   public GameObject GetObjectFromPool() {
       while (inactiveObjects.Count > 0) {
           var obj = inactiveObjects.Pop();
          
           if (obj != null) {
               obj.SetActive(true);
               return obj;
           }
           else {
               Debug.LogWarning("Found a null object in the pool. Has some code outside the pool destroyed it?");
           }
       }
      
       Debug.LogError("All pooled objects are already in use or have been destroyed");
       return null;
   }
  
   public void ReturnObjectToPool(GameObject objectToDeactivate) {
       if (objectToDeactivate != null) {
           objectToDeactivate.SetActive(false);
           inactiveObjects.Push(objectToDeactivate);
       }
   }
}

```

## Reuse arrays and classes from System.Collection
When you use arrays or classes from the [`System.Collection`](https://docs.microsoft.com/en-us/dotnet/api/system.collections.generic?view=net-6.0) namespace (for example, Lists or Dictionaries), it’s efficient to reuse or pool the allocated collection or array. Collection classes expose a `Clear` method, which removes a collection’s values but doesn’t release the memory allocated to the collection.
This is useful if you want to allocate temporary helper collections for complex computations. The following code example demonstrates this:
```
// Bad C# script example. This Update method allocates a new `List` every frame.
void Update() {

    List<float> nearestNeighbors = new List<float>();

    findDistancesToNearestNeighbors(nearestNeighbors);

    nearestNeighbors.Sort();

    // … use the sorted list somehow …
}

```

This example code allocates the `nearestNeighbors` `List` once per frame to collect a set of data points. 
You can hoist this `List` out of the method and into the containing class, so that your code doesn’t need to allocate a new `List` each frame:
```
// Good C# script example. This method re-uses the same List every frame.
List<float> m_NearestNeighbors = new List<float>();

void Update() {

    m_NearestNeighbors.Clear();

    findDistancesToNearestNeighbors(NearestNeighbors);

    m_NearestNeighbors.Sort();

    // … use the sorted list somehow …
}

```

This example code retains and reuses the `List` instances memory across multiple frames. The code only allocates new memory when the `List` needs to expand.
## Additional resources
  * [Managed memory introduction](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-managed-memory-introduction.html)
  * [Reference type management](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-reference-types.html)
  * [Optimizing arrays](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-optimizing-arrays.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-reference-types.html)
Reference type management
[](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-optimizing-arrays.html)
Optimizing arrays
