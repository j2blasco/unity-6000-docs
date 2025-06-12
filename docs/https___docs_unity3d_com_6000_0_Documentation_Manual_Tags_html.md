* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/Tags.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with scenes](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-scenes.html)
  * Tags


[](https://docs.unity3d.com/6000.0/Documentation/Manual/layermask-remove.html)
Remove a layer from a layerMask
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Cameras.html)
Cameras
# Tags
A tag is a reference word which you can assign to one or more **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject). For example, you might define “Player” tags for player-controlled characters and an “Enemy” tag for non-player-controlled characters. You might define items the player can collect in a **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) with a “Collectable” tag. You can use any word you want as a tag. You can even use short phrases, but you might need to widen the Inspector to see the tag’s full name. A GameObject can only have one tag assigned to it.
Tags help you identify GameObjects for scripting purposes. They ensure you don’t need to manually add GameObjects to a script’s exposed properties with drag and drop, so you save time when you use the same script code in multiple GameObjects.
Tags are useful for triggers in [Collider](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collider) control **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) that need to determine if the player interacts with an enemy, a prop, or a collectable, for example.
You can use the [GameObject.FindWithTag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.FindWithTag.html) function to find any GameObject that contains a tag you specify. The following example uses `GameObject.FindWithTag()`. It instantiates `respawnPrefab` at the location of GameObjects with the “Respawn” tag.
```
using UnityEngine;
using System.Collections;

public class Example : MonoBehaviour {
    public GameObject respawnPrefab;
    public GameObject respawn;
    void Start() {
        if (respawn == null)
            respawn = GameObject.FindWithTag("Respawn");

        Instantiate(respawnPrefab, respawn.transform.position, respawn.transform.rotation) as GameObject;
    }
}

```

## Create new Tags
The **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) displays the **Tag** and **Layer** Layers in Unity can be used to selectively opt groups of GameObjects in or out of certain processes or calculations. This includes camera rendering, lighting, physics collisions, or custom calculations in your own code. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Layer) dropdown menus below the name of a GameObject.
To create a new tag, select **Add Tag…**. This opens the [Tag and Layer Manager](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TagManager.html) in the Inspector. Once you name a tag, it can’t be renamed later.
Layers are similar to tags, but are used to define how Unity renders GameObjects in the Scene. Refer to documentation on the [Layers](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html) page for more information.
## Apply a Tag
The **Inspector** shows the **Tag** and **Layer** dropdown menus just below the name of a GameObject. To apply an existing tag to a GameObject, open the **Tags** dropdown and choose the tag you want to apply. The GameObject is now associated with this tag.
## Understand built-in tags
The Editor includes the following built-in tags which don’t appear in the Tag Manager:
  * **Untagged**
  * **Respawn**
  * **Finish**
  * **EditorOnly**
  * **MainCamera**
  * **Player**
  * **GameController**


Some built-in tags like **MainCamera** and **EditorOnly** have unique functions. 
The Editor caches GameObjects tagged with the **MainCamera** tag internally. When you access [Camera.main](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-main.html), the Editor returns the first valid result from its cache. Refer to [Camera.main](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-main.html) to learn more.
A GameObject tagged with **EditorOnly** in a Scene is destroyed when the game builds. Any child GameObjects of a GameObject tagged with **EditorOnly** are also destroyed when the game builds. 
## Additional resources
  * [Camera.main](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-main.html)
  * [Introduction to collision](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)
  * [GameObject.FindWithTag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.FindWithTag.html)
  * [Layers](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/layermask-remove.html)
Remove a layer from a layerMask
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Cameras.html)
Cameras
