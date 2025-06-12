* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/naming-scripts.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Get started with scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-get-started.html)
  * Naming scripts


[](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)
Creating scripts
[](https://docs.unity3d.com/6000.0/Documentation/Manual/inspecting-scripts.html)
Inspecting scripts
# Naming scripts
It’s important to choose names for your script files and the classes declared inside them carefully. Using appropriate file names and organizing your classes under namespaces helps ensure the compiler can identify your classes without errors.
## Script file names
The file name you enter on creation of a script will also be used for the name of the class defined inside it. It’s good practice for a script’s file name to match the name of the class defined inside it.
For **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) derived from the built-in Unity types `MonoBehaviour` and `ScriptableObject`, Unity can still resolve a class type defined in your script even if the file name doesn’t match, but there are some limitations:
  * If multiple classes are defined in your script, Unity selects the class with the same name as the file.
  * If you use the C# `partial` keyword to define a single MonoBehaviour-derived class across multiple files, only the file with the same name as the `partial` class can be used as a [Component](https://docs.unity3d.com/6000.0/Documentation/Manual/Components.html)A functional part of a GameObject. A GameObject can contain any number of components. Unity has many built-in components, and you can create your own by writing scripts that inherit from MonoBehaviour. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingComponents.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#component).


**Note** : In all cases where a class name can’t be unambiguously matched to a particular file, Unity displays a warning.
## Class names and namespaces
Naming conflicts arise when multiple classes with the same name are declared in different parts of your project. The likelihood of naming conflicts increases with the scale of a project and the number of contributors. For example, one developer might write code to control the main player character while another writes the equivalent code for the enemy. If both developers choose to call their main class `Controller`, the compiler won’t be able to determine which class usages of `Controller` in the code refer to.
To avoid class name conflicts, it’s good practice in C# programming to organize your classes under namespaces. A namespace is a collection of classes and the namespace prefixed to a class name provides a complete, unambiguous way to refer to the class. Refer to the Microsoft documentation on [namespaces](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/namespaces/) for more information.
In the example below, the classes `Controller1` and `Controller2` are members of a namespace called `Enemy`:
```
namespace Enemy {
    public class Controller1 : MonoBehaviour {
        ...
    }
    
    public class Controller2 : MonoBehaviour {
        ...
    }
}


```

You can reference these classes unambiguously in code by using their complete name. The complete name is the namespace plus the class name, in this case `Enemy.Controller1` and `Enemy.Controller2` respectively. You can add the namespace declaration around existing class declarations so you don’t need to change the names of all the classes individually. You can add namespace declarations around classes wherever they occur, even if those classes are in different source files.
You can avoid having to type the namespace prefix repeatedly by adding a `using` directive at the top of the file.
```
using Enemy;

```

This causes the compiler to resolve references in this file to `Controller1` and `Controller2` as `Enemy.Controller1` and `Enemy.Controller2`, respectively. If the script also needs to refer to classes with the same name from a different namespace (for example, one called `Player`), then you must specify the namespace prefixes. If two namespaces that contain conflicting class names are imported with `using` directives in the same file, the compiler reports an error.
## Limitation for multiple namespaces
Unity has a specific limitation relating to namespaces and MonoBehaviour or ScriptableObject classes. If your file contains a definition for a MonoBehaviour or ScriptableObject class, you can’t use multiple namespaces within that file.
Unity gives the following warning in the console:
```
Class MyClass can not exist in multiple namespaces in the same file, even if one is excluded with preprocessor directives. Please move these to separate files if this is the case.

```

If you have a file which defines a MonoBehaviour in one namespace, and other classes in a different namespace **within the same file** , Unity will not recognize the MonoBehaviour class and you will not be able to use it on **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject). This limitation was introduced in Unity 2020.1 to improve import and compilation speed, and therefore some older **asset store** A growing library of free and commercial assets created by Unity and members of the community. Offers a wide variety of assets, from textures, models and animations to whole project examples, tutorials and Editor extensions. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStore.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AssetStore) packages written before this limitation was introduced may function incorrectly as a result. To fix problems relating to this issue, separate out the code for the classes in each namespace to separate files.
## Additional resources
  * [Create scripts](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)
  * [Assembly definitions](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-files.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)
Creating scripts
[](https://docs.unity3d.com/6000.0/Documentation/Manual/inspecting-scripts.html)
Inspecting scripts
