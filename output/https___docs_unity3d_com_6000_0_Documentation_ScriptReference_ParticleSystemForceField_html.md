* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemForceField.html

# ParticleSystemForceField
class in UnityEngine
/
Inherits from:[Behaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Behaviour.html)
/
Implemented in:[UnityEngine.ParticleSystemModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.ParticleSystemModule.html)
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystemForceField.html "Go to ParticleSystemForceField Component in the Manual")
### Description
Script interface for Particle System Force Fields.
Particle System Force Fields can be used to influence groups of particles that enter each field's zone of influence.  
  
The shape of the Force Field can be set to a variety of shapes, and how the particles are affected is controlled by various properties in the Force Field.  
  
As part of choosing the shape, you may define a start and end range. The end range describes the maximum extent of the shape, and the start range can be used to create a hollow shape.  
  
A number of forces can be applied to particles that are within this volume: directional, gravitational, rotational, drag, and a vector field.  
  
The settings for each type of force make use of the [MinMaxCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MinMaxCurve.html) type, which is also used in the Particle System. This type allows you to set simple uniform values, or more complicated values that vary per-particle, and vary over the lifetime of each particle.
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using UnityEngine;  
  
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)))]
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public ParticleSystemForceFieldShape[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemForceFieldShape.html) m_Shape = ParticleSystemForceFieldShape.Sphere[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemForceFieldShape.Sphere.html);
    public float m_StartRange = 0.0f;
    public float m_EndRange = 3.0f;
    public Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) m_Direction = Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html);
    public float m_Gravity = 0.0f;
    public float m_GravityFocus = 0.0f;
    public float m_RotationSpeed = 0.0f;
    public float m_RotationAttraction = 0.0f;
    public Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) m_RotationRandomness = Vector2.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2-zero.html);
    public float m_Drag = 0.0f;
    public bool m_MultiplyDragByParticleSize = false;
    public bool m_MultiplyDragByParticleVelocity = false;  
  
    private ParticleSystemForceField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemForceField.html) m_ForceField;  
  
    void Start()
    {
        // Create a Force Field
        var go = new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)("ForceField", typeof(ParticleSystemForceField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemForceField.html)));
        go.transform.position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0, 2, 0);
        go.transform.rotation = Quaternion.Euler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.Euler.html)(new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(90.0f, 0.0f, 0.0f));  
  
        m_ForceField = go.GetComponent<ParticleSystemForceField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemForceField.html)>();  
  
        // Configure Particle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle.html) System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html)
        transform.position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0, -4, 0);
        transform.rotation = Quaternion.identity[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion-identity.html);
        var ps = GetComponent<ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)>();  
  
        var main = ps.main;
        main.startSize = new ParticleSystem.MinMaxCurve[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MinMaxCurve.html)(0.05f, 0.2f);
        main.startSpeed = new ParticleSystem.MinMaxCurve[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MinMaxCurve.html)(1.5f, 2.5f);
        main.maxParticles = 100000;  
  
        var emission = ps.emission;
        emission.rateOverTime = 0.0f;
        emission.burstCount = 1;
        emission.SetBurst(0, new ParticleSystem.Burst[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Burst.html)(0.0f, 200, 200, -1, 0.1f));  
  
        var shape = ps.shape;
        shape.shapeType = ParticleSystemShapeType.SingleSidedEdge[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemShapeType.SingleSidedEdge.html);
        shape.radius = 5.0f;
        shape.radiusMode = ParticleSystemShapeMultiModeValue.BurstSpread[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemShapeMultiModeValue.BurstSpread.html);
        shape.randomPositionAmount = 0.1f;
        shape.randomDirectionAmount = 0.05f;  
  
        var forces = ps.externalForces;
        forces.enabled = true;
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        m_ForceField.shape = m_Shape;
        m_ForceField.startRange = m_StartRange;
        m_ForceField.endRange = m_EndRange;
        m_ForceField.directionX = m_Direction.x;
        m_ForceField.directionY = m_Direction.y;
        m_ForceField.directionZ = m_Direction.z;
        m_ForceField.gravity = m_Gravity;
        m_ForceField.gravityFocus = m_GravityFocus;
        m_ForceField.rotationSpeed = m_RotationSpeed;
        m_ForceField.rotationAttraction = m_RotationAttraction;
        m_ForceField.rotationRandomness = m_RotationRandomness;
        m_ForceField.drag = m_Drag;
        m_ForceField.multiplyDragByParticleSize = m_MultiplyDragByParticleSize;
        m_ForceField.multiplyDragByParticleVelocity = m_MultiplyDragByParticleVelocity;
    }  
  
    void OnGUI()
    {
        GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)[] shapeLabels = Enum.GetNames(typeof(ParticleSystemForceFieldShape[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemForceFieldShape.html))).Select(n => new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)(n)).ToArray();
        m_Shape = (ParticleSystemForceFieldShape[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemForceFieldShape.html))GUI.SelectionGrid[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.SelectionGrid.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(25, 25, 400, 25), (int)m_Shape, shapeLabels, 4);  
  
        float y = 80.0f;
        float spacing = 40.0f;  
  
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(25, y, 140, 30), "Start Range");
        m_StartRange = GUI.HorizontalSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.HorizontalSlider.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(165, y + 5, 100, 30), m_StartRange, 0.0f, 2.0f);
        y += spacing;  
  
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(25, y, 140, 30), "End Range");
        m_EndRange = GUI.HorizontalSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.HorizontalSlider.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(165, y + 5, 100, 30), m_EndRange, 2.0f, 3.0f);
        y += spacing;  
  
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(25, y, 140, 30), "Direction[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.NavigationMoveEvent.Direction.html)");
        m_Direction.x = GUI.HorizontalSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.HorizontalSlider.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(165, y + 5, 40, 30), m_Direction.x, -1.0f, 1.0f);
        m_Direction.y = GUI.HorizontalSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.HorizontalSlider.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(210, y + 5, 40, 30), m_Direction.y, -1.0f, 1.0f);
        m_Direction.z = GUI.HorizontalSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.HorizontalSlider.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(255, y + 5, 40, 30), m_Direction.z, -1.0f, 1.0f);
        y += spacing;  
  
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(25, y, 140, 30), "Gravity[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Gravity.html)");
        m_Gravity = GUI.HorizontalSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.HorizontalSlider.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(165, y + 5, 100, 30), m_Gravity, -0.05f, 0.05f);
        y += spacing;  
  
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(25, y, 140, 30), "Gravity[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Gravity.html) Focus");
        m_GravityFocus = GUI.HorizontalSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.HorizontalSlider.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(165, y + 5, 100, 30), m_GravityFocus, 0.0f, 1.0f);
        y += spacing;  
  
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(25, y, 140, 30), "Rotation Speed");
        m_RotationSpeed = GUI.HorizontalSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.HorizontalSlider.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(165, y + 5, 100, 30), m_RotationSpeed, -10.0f, 10.0f);
        y += spacing;  
  
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(25, y, 140, 30), "Rotation Attraction");
        m_RotationAttraction = GUI.HorizontalSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.HorizontalSlider.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(165, y + 5, 100, 30), m_RotationAttraction, 0.0f, 0.01f);
        y += spacing;  
  
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(25, y, 140, 30), "Rotation Randomness");
        m_RotationRandomness.x = GUI.HorizontalSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.HorizontalSlider.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(165, y + 5, 60, 30), m_RotationRandomness.x, 0.0f, 1.0f);
        m_RotationRandomness.y = GUI.HorizontalSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.HorizontalSlider.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(230, y + 5, 60, 30), m_RotationRandomness.y, 0.0f, 1.0f);
        y += spacing;  
  
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(25, y, 140, 30), "Drag");
        m_Drag = GUI.HorizontalSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.HorizontalSlider.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(165, y + 5, 100, 30), m_Drag, 0.0f, 20.0f);
        y += spacing;  
  
        m_MultiplyDragByParticleSize = GUI.Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Toggle.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(25, y, 220, 30), m_MultiplyDragByParticleSize, "Multiply Drag by Particle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle.html) Size");
        y += spacing;  
  
        m_MultiplyDragByParticleVelocity = GUI.Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Toggle.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(25, y, 220, 30), m_MultiplyDragByParticleVelocity, "Multiply Drag by Particle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle.html) Velocity");
        y += spacing;
    }
}

```

### Properties
Property | Description  
---|---  
[directionX](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemForceField-directionX.html) | Apply a linear force along the local X axis to particles within the volume of the Force Field.  
[directionY](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemForceField-directionY.html) | Apply a linear force along the local Y axis to particles within the volume of the Force Field.  
[directionZ](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemForceField-directionZ.html) | Apply a linear force along the local Z axis to particles within the volume of the Force Field.  
[drag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemForceField-drag.html) | Apply drag to particles within the volume of the Force Field.  
[endRange](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemForceField-endRange.html) | Determines the size of the shape used for influencing particles.  
[gravity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemForceField-gravity.html) | Apply gravity to particles within the volume of the Force Field.  
[gravityFocus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemForceField-gravityFocus.html) | When using the gravity force, set this value between 0 and 1 to control the focal point of the gravity effect.  
[length](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemForceField-length.html) | Describes the length of the Cylinder when using the Cylinder Force Field shape to influence particles.  
[multiplyDragByParticleSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemForceField-multiplyDragByParticleSize.html) | When using Drag, the drag strength will be multiplied by the size of the particles if this toggle is enabled.  
[multiplyDragByParticleVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemForceField-multiplyDragByParticleVelocity.html) | When using Drag, the drag strength will be multiplied by the speed of the particles if this toggle is enabled.  
[rotationAttraction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemForceField-rotationAttraction.html) | Controls how strongly particles are dragged into the vortex motion.  
[rotationRandomness](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemForceField-rotationRandomness.html) | Apply randomness to the Force Field axis that particles will travel around.  
[rotationSpeed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemForceField-rotationSpeed.html) | The speed at which particles are propelled around a vortex.  
[shape](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemForceField-shape.html) | Selects the type of shape used for influencing particles.  
[startRange](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemForceField-startRange.html) | Setting a value greater than 0 creates a hollow Force Field shape. This will cause particles to not be affected by the Force Field when closer to the center of the volume than the startRange property.  
[vectorField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemForceField-vectorField.html) | Apply forces to particles within the volume of the Force Field, by using a 3D texture containing vector field data.  
[vectorFieldAttraction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemForceField-vectorFieldAttraction.html) | Controls how strongly particles are dragged into the vector field motion.  
[vectorFieldSpeed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemForceField-vectorFieldSpeed.html) | The speed at which particles are propelled through the vector field.  
### Inherited Members
### Properties
Property | Description  
---|---  
[enabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Behaviour-enabled.html) | Enabled Behaviours are Updated, disabled Behaviours are not.  
[isActiveAndEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Behaviour-isActiveAndEnabled.html) | Reports whether a GameObject and its associated Behaviour is active and enabled.  
[gameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-gameObject.html) | The game object this component is attached to. A component is always attached to a game object.  
[tag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-tag.html) | The tag of this game object.  
[transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-transform.html) | The Transform attached to this GameObject.  
[hideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-hideFlags.html) | Should the object be hidden, saved with the Scene or modifiable by the user?  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-name.html) | The name of the object.  
### Public Methods
Method | Description  
---|---  
[BroadcastMessage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.BroadcastMessage.html) | Calls the method named methodName on every MonoBehaviour in this game object or any of its children.  
[CompareTag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.CompareTag.html) | Checks the GameObject's tag against the defined tag.  
[GetComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponent.html) | Gets a reference to a component of type T on the same GameObject as the component specified.  
[GetComponentInChildren](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentInChildren.html) | Gets a reference to a component of type T on the same GameObject as the component specified, or any child of the GameObject.  
[GetComponentIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentIndex.html) | Gets the index of the component on its parent GameObject.  
[GetComponentInParent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentInParent.html) | Gets a reference to a component of type T on the same GameObject as the component specified, or any parent of the GameObject.  
[GetComponents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponents.html) | Gets references to all components of type T on the same GameObject as the component specified.  
[GetComponentsInChildren](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentsInChildren.html) | Gets references to all components of type T on the same GameObject as the component specified, and any child of the GameObject.  
[GetComponentsInParent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentsInParent.html) | Gets references to all components of type T on the same GameObject as the component specified, and any parent of the GameObject.  
[SendMessage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.SendMessage.html) | Calls the method named methodName on every MonoBehaviour in this game object.  
[SendMessageUpwards](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.SendMessageUpwards.html) | Calls the method named methodName on every MonoBehaviour in this game object and on every ancestor of the behaviour.  
[TryGetComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.TryGetComponent.html) | Gets the component of the specified type, if it exists.  
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
