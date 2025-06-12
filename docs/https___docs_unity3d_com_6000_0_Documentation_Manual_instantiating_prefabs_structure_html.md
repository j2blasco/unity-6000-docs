* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/instantiating-prefabs-structure.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-gameobjects.html)
  * [Prefabs](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)
  * [Instantiating prefabs at runtime](https://docs.unity3d.com/6000.0/Documentation/Manual/instantiating-prefabs.html)
  * Build a structure with prefabs


[](https://docs.unity3d.com/6000.0/Documentation/Manual/instantiating-prefabs-intro.html)
Introduction to instantiating prefabs
[](https://docs.unity3d.com/6000.0/Documentation/Manual/instantiating-prefabs-projectiles.html)
Instantiate projectiles and explosions
# Build a structure with prefabs
You can use code to create many copies of a **prefab** An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Prefab) in a particular configuration almost instantaneously. Using code to generate structures like this is called procedural generation.
## Create a wall of block instances
This task demonstrates how to create a wall of block instances.
### Attach the Wall script to a GameObject
  1. Create a MonoBehaviour script and name it `Wall`.
  2. Paste the code below into your `Wall` script.
  3. Attach the `Wall` script to an empty **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) in your **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene).

```
using UnityEngine;
public class Wall : MonoBehaviour
{
   public GameObject block;
   public int width = 10;
   public int height = 4;
  
   void Start()
   {
       for (int y=0; y<height; ++y)
       {
           for (int x=0; x<width; ++x)
           {
               Instantiate(block, new Vector3(x,y,0), Quaternion.identity);
           }
       }       
   }
}

```

**Result:** The **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) displays the `Block` variable with `None` in the field. A value of `None` means that no Prefab has been assigned to this variable yet. 
![The Block variable, with no Prefab assigned yet](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/InstantiatingWallBlockNotAssigned.png) The **Block** variable, with no Prefab assigned yet
### Assign a prefab to the Block variable
The example script above won’t work until you assign a Prefab to the **Block** variable. To create a simple block Prefab:
  1. Choose **GameObject > 3D Object > Cube.**
  2. Drag the cube from the **Hierarchy** window into the **Assets** folder in the **Project** window. This creates a Prefab Asset.
  3. Rename your Prefab to `Block`.
  4. Now that your `Block` Prefab exists as an Asset, you can safely delete the cube from your Hierarchy. 
  5. Now that you have created a `Block` Prefab, you can assign it to the **Block** variable. Select your original GameObject (the one with the `Wall` script attached to it). Then drag the `Block` Prefab from the ****Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow)** into the **Block** variable slot (where it says `None`).

![The Block variable, with the Block Prefab assigned to it ](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/InstantiatingWallBlockAssigned.png) The **_Block_** variable, with the Block Prefab assigned to it 
When you have finished this set-up, click **Play** and you’ll see that Unity builds the wall using the Prefab:
![A wall built from 4 rows of 10 blocks, as generated by the example above.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/InstantiatingWallComplete.png) A wall built from 4 rows of 10 blocks, as generated by the example above.
This is a flexible workflow pattern that you can use over and over again in Unity. Because you are using a Prefab in this script, you can easily replace or edit the Prefab to modify the properties of the bricks in the wall, without needing to touch the script. You can also use your `Wall` script on other GameObjects in your Scene with different Prefabs assigned to them to have various walls made from different types of Prefab.
You can use code to place a GameObject in a grid, in a circle pattern, randomly scattered, or any other configurations that you can think of to fit whatever game or app you are creating. Here’s another example showing how to place instances in a circular formation:
```
using UnityEngine;
public class CircleFormation : MonoBehaviour
{
   // Instantiates prefabs in a circle formation
   public GameObject prefab;
   public int numberOfObjects = 20;
   public float radius = 5f;
   void Start()
   {
       for (int i = 0; i < numberOfObjects; i++)
       {
           float angle = i * Mathf.PI * 2 / numberOfObjects;
           float x = Mathf.Cos(angle) * radius;
           float z = Mathf.Sin(angle) * radius;
           Vector3 pos = transform.position + new Vector3(x, 0, z);
           float angleDegrees = -angle*Mathf.Rad2Deg;
           Quaternion rot = Quaternion.Euler(0, angleDegrees, 0);
           Instantiate(prefab, pos, rot);
       }
   }
}

```
![A circular arrangement of blocks, as generated by the example above](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/InstantiatingCircle.png) A circular arrangement of blocks, as generated by the example above
## Additonal resources
  * [Instantiate projectiles and explosions](https://docs.unity3d.com/6000.0/Documentation/Manual/instantiating-prefabs-projectiles.html)
  * [Simulate character destruction](https://docs.unity3d.com/6000.0/Documentation/Manual/instantiating-prefabs-wrecks.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/instantiating-prefabs-intro.html)
Introduction to instantiating prefabs
[](https://docs.unity3d.com/6000.0/Documentation/Manual/instantiating-prefabs-projectiles.html)
Instantiate projectiles and explosions
