* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html

# ScriptableObject
class in UnityEngine
/
Inherits from:[Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html)
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ScriptableObject.html "Go to ScriptableObject Component in the Manual")
### Description
A class you can derive from if you want to create objects that live independently of GameObjects.
Use ScriptableObjects to centralise data in a way that can be conveniently accessed from scenes and assets within a project.  
  
Instantiate ScriptableObject objects with [CreateInstance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html).  
  
You can save ScriptableObjects to asset files either from the Editor UI (see [CreateAssetMenuAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CreateAssetMenuAttribute.html)), or by calling [AssetDatabase.CreateAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CreateAsset.html) from a script. You can also generate ScriptableObjects as an output from a [ScriptedImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.ScriptedImporter.html). See [AssetImportContext.AddObjectToAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext.AddObjectToAsset.html).  
  
If a `ScriptableObject` has not been saved to an asset, and it is referenced from an object in a scene, Unity serializes it directly into the scene file. For ScriptableObjects that have only a single persistent instance within a project, use the [ScriptableSingleton<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableSingleton_1.html) base class.  
  
Access previously saved objects using [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html), for example [AssetDatabase.LoadAssetAtPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAssetAtPath.html). When a ScriptableObject is referenced from a field on a [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html), the ScriptableObject is automatically loaded, so a script can simply use the value of the field to reach it.  
  
The C# fields of a `ScriptableObject` are serialized exactly like fields on a MonoBehaviour, refer to [Script Serialization](https://docs.unity3d.com/6000.0/Documentation/Manual/script-serialization.html) for details. Classes that include big arrays, or other potentially large data, should be declared with the [PreferBinarySerialization](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PreferBinarySerialization.html) attribute, because YAML is not an efficient representation for that sort of data.  
  
Calling `Destroy` on a `ScriptableObject` releases native resources associated with it but the object stays in memory until garbage collected. Objects in this detached state will appear to be null despite not really being so. However, this class doesn't support the [null-conditional operator ](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/language-specification/expressions#null-conditional-operator) (**?.**) and the [null-coalescing operator ](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/language-specification/expressions#the-null-coalescing-operator)(**??**).  
  
The following example demonstrates a typical use of a ScriptableObject: different types of vehicle parameters are represented in the fields of a VehicleTypeInfo class, derived from ScriptableObject. Each type of vehicle would have its own asset file, with the parameter values set appropriately for the type. Each instance of the vehicle in the game would have a reference to the asset corresponding to its type, rather than keeping its own redundant copy of each parameter. This design makes it convenient to tweak vehicle behaviour in a central location. It is also good for performance, especially in cases where the size of the shared data is substantial.  
  
The first script of the example implements a class derived from ScriptableObject. 
```
using UnityEngine;  
  
[CreateAssetMenu]
public class VehicleTypeInfo : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
    // Class that represents a specific type of vehicle
    [Range(0.1f, 100f)]
    public float m_MaxSpeed = 0.1f;  
  
    [Range(0.1f, 10f)]
    public float m_MaxAcceration = 0.1f;  
  
    // This class could have many other vehicle parameters, such as Turning Radius, Range, Damage etc
}

```

The second script implements a MonoBehaviour that uses the ScriptableObject.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class VehicleInstance : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Snippet of a MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html) that would control motion of a specific vehicle.
    // In PlayMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayMode.html) it accelerates up to the maximum speed permitted by its type  
  
    [Range(0f, 200f)]
    public float m_CurrentSpeed;  
  
    [Range(0f, 50f)]
    public float m_Acceleration;  
  
    // Reference to the ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html) asset
    public VehicleTypeInfo m_VehicleType;  
  
    public void Initialize(VehicleTypeInfo vehicleType)
    {
        m_VehicleType = vehicleType;
        m_CurrentSpeed = 0f;
        m_Acceleration = Random.Range[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.Range.html)(0.05f, m_VehicleType.m_MaxAcceration);
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        m_CurrentSpeed += m_Acceleration * Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html);  
  
        // Use parameter from the ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html) to control the behaviour of the Vehicle
        if (m_VehicleType && m_VehicleType.m_MaxSpeed < m_CurrentSpeed)
            m_CurrentSpeed = m_VehicleType.m_MaxSpeed;  
  
        gameObject.transform.position += gameObject.transform.forward * Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html) * m_CurrentSpeed;
    }
}  
  
public class ScriptableObjectVehicleExample
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/Setup ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html) Vehicle Example")]
    static void MenuCallback()
    {
        // This example programmatically performs steps that would typically be performed from the Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)'s user interface
        // to creates a simple demonstration.  When going into Playmode the three objects will move according to the limits
        // set by their vehicle type.  
  
        // Step 1 - Create or reload the assets that store each VehicleTypeInfo object.
        VehicleTypeInfo wagon = AssetDatabase.LoadAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAssetAtPath.html)<VehicleTypeInfo>("Assets/VehicleTypeWagon.asset");
        if (wagon == null)
        {
            // Create and save ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html) because it doesn't exist yet
            wagon = ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)<VehicleTypeInfo>();
            wagon.m_MaxSpeed = 5f;
            wagon.m_MaxAcceration = 0.5f;
            AssetDatabase.CreateAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CreateAsset.html)(wagon, "Assets/VehicleTypeWagon.asset");
        }  
  
        VehicleTypeInfo cruiser = AssetDatabase.LoadAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAssetAtPath.html)<VehicleTypeInfo>("Assets/VehicleTypeCruiser.asset");
        if (cruiser == null)
        {
            cruiser = ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)<VehicleTypeInfo>();
            cruiser.m_MaxSpeed = 75f;
            cruiser.m_MaxAcceration = 2f;
            AssetDatabase.CreateAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CreateAsset.html)(cruiser, "Assets/VehicleTypeCruiser.asset");
        }  
  
        // Step 2 - Create some example vehicles in the current scene
        {
            var vehicle = GameObject.CreatePrimitive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.CreatePrimitive.html)(PrimitiveType.Sphere[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Sphere.html));
            vehicle.name = "Wagon1";
            var vehicleBehaviour = vehicle.AddComponent<VehicleInstance>();
            vehicleBehaviour.Initialize(wagon);
        }  
  
        {
            var vehicle = GameObject.CreatePrimitive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.CreatePrimitive.html)(PrimitiveType.Sphere[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Sphere.html));
            vehicle.name = "Wagon2";
            var vehicleBehaviour = vehicle.AddComponent<VehicleInstance>();
            vehicleBehaviour.Initialize(wagon);
        }  
  
        {
            var vehicle = GameObject.CreatePrimitive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.CreatePrimitive.html)(PrimitiveType.Cube[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Cube.html));
            vehicle.name = "Cruiser1";
            var vehicleBehaviour = vehicle.AddComponent<VehicleInstance>();
            vehicleBehaviour.Initialize(cruiser);
        }
    }
}

```

### Static Methods
Method | Description  
---|---  
[CreateInstance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html) | Creates an instance of a scriptable object.  
### Messages
Message | Description  
---|---  
[Awake](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.Awake.html) | Called when an instance of ScriptableObject is created.  
[OnDestroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.OnDestroy.html) | This function is called when the scriptable object will be destroyed.  
[OnDisable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.OnDisable.html) | This function is called when the scriptable object goes out of scope.  
[OnEnable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.OnEnable.html) | This function is called when the object is loaded.  
[OnValidate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.OnValidate.html) | Editor-only function that Unity calls when the script is loaded or a value changes in the Inspector.  
[Reset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.Reset.html) | Reset to default values.  
### Inherited Members
### Properties
Property | Description  
---|---  
[hideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-hideFlags.html) | Should the object be hidden, saved with the Scene or modifiable by the user?  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-name.html) | The name of the object.  
### Public Methods
Method | Description  
---|---  
[GetInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.GetInstanceID.html) | Gets the instance ID of the object.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.ToString.html) | Returns the name of the object.  
### Static Methods
Method | Description  
---|---  
[Destroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Destroy.html) | Removes a GameObject, component or asset.  
[DestroyImmediate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DestroyImmediate.html) | Destroys the object obj immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DontDestroyOnLoad.html) | Do not destroy the target Object when loading a new Scene.  
[FindAnyObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindAnyObjectByType.html) | Retrieves any active loaded object of Type type.  
[FindFirstObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindFirstObjectByType.html) | Retrieves the first active loaded object of Type type.  
[FindObjectsByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindObjectsByType.html) | Retrieves a list of all loaded objects of Type type.  
[Instantiate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Instantiate.html) | Clones the object original and returns the clone.  
[InstantiateAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.InstantiateAsync.html) | Captures a snapshot of the original object (that must be related to some GameObject) and returns the AsyncInstantiateOperation.  
### Operators
Operator | Description  
---|---  
[bool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_Object.html) | Does the object exist?  
[operator !=](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_ne.html) | Compares if two objects refer to a different object.  
[operator ==](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_eq.html) | Compares two object references to see if they refer to the same object.  
* * *
