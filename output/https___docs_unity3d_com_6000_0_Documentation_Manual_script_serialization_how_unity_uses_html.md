* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/script-serialization-how-unity-uses.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Compilation and code reload ](https://docs.unity3d.com/6000.0/Documentation/Manual/compilation-and-code-reload.html)
  * [Script serialization](https://docs.unity3d.com/6000.0/Documentation/Manual/script-serialization.html)
  * How Unity uses serialization


[](https://docs.unity3d.com/6000.0/Documentation/Manual/script-serialization-custom-serialization.html)
Custom serialization
[](https://docs.unity3d.com/6000.0/Documentation/Manual/json-serialization.html)
JSON Serialization
# How Unity uses serialization
## Saving and loading
Unity uses serialization to load and save [scenes](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene), [Assets](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetWorkflow.html)Any media or data that can be used in your game or project. An asset may come from a file created outside of Unity, such as a 3D Model, an audio file or an image. You can also create some asset types in Unity, such as an Animator Controller, an Audio Mixer or a Render Texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetWorkflow.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Asset), and [AssetBundles](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundlesIntro.html) to and from your device’s memory. This includes data saved in your own scripting API objects such as [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html) components and [ScriptableObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ScriptableObject.html).
Many of the features in the Unity Editor are built on top of the core serialization system. Two things to be particularly aware of with serialization are the [Inspector window](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html), and hot reloading.
### The Inspector window
The **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window shows the value of the serialized fields of the inspected objects. When you change a value in the Inspector, the Inspector updates the serialized data and triggers a deserialization that updates the inspected object.
The same applies for both built-in Unity objects, and scripting objects such as MonoBehaviour-derived classes.
Unity doesn’t call any C# property getters and setters when you view or change values in the Inspector window. Instead, Unity accesses the serialized backing field directly.
### Hot reloading
Hot reloading of script code is performed as part of an asset database refresh. It refers to the process of reloading and applying code changes directly while the Editor is running, without having to restart it. For more information, refer to [Refreshing the Asset Database](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetDatabaseRefreshing.html) and [Hot reloading](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetDatabaseRefreshing.html#hotreloading).
**Note** : Hot reloading is a special serialization case. Unlike in other serialization cases, Unity serializes private fields by default when reloading, even if they don’t have the [SerializeField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Serializefield.html) attribute.
When Unity reloads **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts):
  1. Unity serializes and stores all variables in all loaded scripts.
  2. Unity restores them to their original, pre-serialization values: 
     * Unity restores all variables - **including private variables** - that fulfill the requirements for serialization, even if a variable has no `[SerializeField]` attribute. Sometimes, you need to prevent Unity from restoring private variables, for example, if you want a reference to be null after reloading from scripts. In this case, use the [`[field: NonSerialized]`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/NonSerialized.html) attribute.
     * Unity never restores static variables, so don’t use static variables for states that you need to keep after Unity reloads a script because the reloading process will discard them.


## Prefabs
A [prefab](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Prefab) is the serialized data of one or more [GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/GameObjects.html)The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) or [components](https://docs.unity3d.com/6000.0/Documentation/Manual/Components.html)A functional part of a GameObject. A GameObject can contain any number of components. Unity has many built-in components, and you can create your own by writing scripts that inherit from MonoBehaviour. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingComponents.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#component). A prefab instance contains a reference to both the prefab source and a list of modifications to it. The modifications are what Unity needs to do to the prefab source to create that particular prefab instance.
The prefab instance only exists while you edit your project in the Unity Editor. The Unity Editor instantiates a GameObject from its two sets of serialization data: the prefab source and the prefab instance’s modifications.
## Instantiation
When you call [`Instantiate`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Instantiate.html) on anything that exists in a scene, such as a prefab or a GameObject:
  1. Unity serializes it. This happens both at runtime and in the Editor. Unity can serialize everything that derives from `UnityEngine.Object`.
  2. Unity creates a new GameObject and deserializes the data onto the new GameObject.
  3. Unity runs the same serialization code in a different variant to report which other `UnityEngine.Objects` it references. It checks all referenced `UnityEngine.Objects` to determine if they’re part of the data Unity instantiates. If the reference points to something external, such as a Texture, Unity keeps that reference as it is. If the reference points to something internal, such as a child GameObject, Unity patches the reference to the corresponding copy.


## Unloading unused assets
`EditorUtility.UnloadUnusedAssetsImmediate` is the native Unity garbage collector and has a different purpose to the standard C# garbage collector. It runs after you load a scene and checks for objects (like Textures) that it no longer references and unloads them safely. The native Unity garbage collector runs the serializer in a variation in which objects report all references to external `UnityEngine.Objects`. This is how Textures that one scene uses, the garbage collector unloads in the next.
## Differences between Editor and runtime serialization
Most serialization happens in the Editor, whereas deserialization is the focus at runtime. Unity serializes some features only in the Editor, while it can serialize other features in both the Editor and at runtime:
**Feature** | **Editor** | **Runtime**  
---|---|---  
**Assets in Binary Format** | Read/write supported | Read supported  
**Assets in YAML format** | Read/write supported | Not supported  
**Saving scenes, prefabs and other assets** | Supported, unless in Play mode | Not supported  
**Serialization of individual objects with[JsonUtility](https://docs.unity3d.com/6000.0/Documentation/Manual/json-serialization.html)** | Read/write support with JsonUtility.  
  
Support for additional types of objects with EditorJsonUtility | Read/write support with JsonUtility  
**[SerializeReference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeReference.html)** | Supported | Supported  
**[ISerializationCallbackReceiver](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ISerializationCallbackReceiver.html)** | Supported | Supported  
**[FormerlySerializedAs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Serialization.FormerlySerializedAsAttribute.html)** | Supported | Not supported  
Objects can have additional fields that only the Editor serializes, such as when you declare fields within the UNITY_EDITOR [scripting symbol](https://docs.unity3d.com/6000.0/Documentation/Manual/platform-dependent-compilation.html):
```
public class SerializeRules : MonoBehaviour
{
#if UNITY_EDITOR
public int m_intEditorOnly;
#endif
}

```

In the previous example, the `m_intEditorOnly` field is only serialized in the editor and isn’t included in the build. This allows you to save memory by omitting data that’s only required in the Editor from your build. Any code that uses that field would also need to be conditionally compiled, for example within `#if UNITY_EDITOR` blocks, so that the class can compile at build time.
The Editor doesn’t support objects with fields that Unity only serializes at runtime, (for example, when you declare fields within the UNITY_STANDALONE directive).
## Additional resources
  * [Serialization rules](https://docs.unity3d.com/6000.0/Documentation/Manual/script-serialization-rules.html)
  * [JSONSerialization](https://docs.unity3d.com/6000.0/Documentation/Manual/json-serialization.html)
  * [Serialization best practices](https://docs.unity3d.com/6000.0/Documentation/Manual/script-serialization-best-practices.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/script-serialization-custom-serialization.html)
Custom serialization
[](https://docs.unity3d.com/6000.0/Documentation/Manual/json-serialization.html)
JSON Serialization
