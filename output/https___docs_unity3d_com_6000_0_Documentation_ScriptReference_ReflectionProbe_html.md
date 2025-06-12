* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe.html

# ReflectionProbe
class in UnityEngine
/
Inherits from:[Behaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Behaviour.html)
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html "Go to ReflectionProbe Component in the Manual")
### Description
The reflection probe is used to capture the surroundings into a texture which is passed to the shaders and used for reflections.
The properties are an exact match for the values shown in the Inspector.  
  
This class is a script interface for a [reflection probe](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html) component.  
  
Reflection probes are usually just created in the Editor, but sometimes you might want to create a reflection probe from a script:
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class ProbeCreator
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("ReflectionProbe[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe.html)/CreateRealtimeProbe")]
    public static void RealtimeProbe()
    {
        // Add a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) with a ReflectionProbe[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe.html) component
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) probeGameObject = new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)("Realtime Reflection Probe");
        ReflectionProbe[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe.html) probeComponent = probeGameObject.AddComponent<ReflectionProbe[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe.html)>();
        
        // The probe will contribute to reflections inside a box of size 10x10x10 centered on the position of the probe
        probeComponent.size = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(10, 10, 10);  
  
        // Set the type to realtime and refresh the probe every frame
        probeComponent.mode = UnityEngine.Rendering.ReflectionProbeMode.Realtime;
        probeComponent.refreshMode = UnityEngine.Rendering.ReflectionProbeRefreshMode.EveryFrame;
    }
}

```

### Static Properties
Property | Description  
---|---  
[defaultTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe-defaultTexture.html) | The surface texture of the default reflection probe that captures the environment contribution. Read only.  
[defaultTextureHDRDecodeValues](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe-defaultTextureHDRDecodeValues.html) | HDR decode values of the default reflection probe texture.  
### Properties
Property | Description  
---|---  
[backgroundColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe-backgroundColor.html) | The color with which the texture of reflection probe will be cleared.  
[bakedTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe-bakedTexture.html) | Reference to the baked texture of the reflection probe's surrounding.  
[blendDistance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe-blendDistance.html) | Distance around probe used for blending (used in deferred probes).  
[bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe-bounds.html) | The probe's world space axis-aligned bounding box in which the probe can contribute to reflections (Read Only).  
[boxProjection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe-boxProjection.html) | Should this reflection probe use box projection?  
[center](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe-center.html) | The center of the probe's bounding box in which the probe can contribute to reflections. The center is relative to the position of the probe.  
[clearFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe-clearFlags.html) | How the reflection probe clears the background.  
[cullingMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe-cullingMask.html) | This is used to render parts of the reflecion probe's surrounding selectively.  
[customBakedTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe-customBakedTexture.html) | Reference to the baked texture of the reflection probe's surrounding. Use this to assign custom reflection texture.  
[farClipPlane](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe-farClipPlane.html) | The far clipping plane distance when rendering the probe.  
[hdr](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe-hdr.html) | Should this reflection probe use HDR rendering?  
[importance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe-importance.html) | Reflection probe importance.  
[intensity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe-intensity.html) | The intensity modifier that is applied to the texture of reflection probe in the shader.  
[mode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe-mode.html) | Should reflection probe texture be generated in the Editor (ReflectionProbeMode.Baked) or should probe use custom specified texure (ReflectionProbeMode.Custom)?  
[nearClipPlane](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe-nearClipPlane.html) | The near clipping plane distance when rendering the probe.  
[realtimeTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe-realtimeTexture.html) | Reference to the real-time texture of the reflection probe's surroundings. Use this to assign a RenderTexture to use for real-time reflection.  
[refreshMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe-refreshMode.html) | Sets the way the probe will refresh.Additional resources: ReflectionProbeRefreshMode.  
[renderDynamicObjects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe-renderDynamicObjects.html) | Specifies whether Unity should render non-static GameObjects into the Reflection Probe. If you set this to true, Unity renders non-static GameObjects into the Reflection Probe. If you set this to false, Unity does not render non-static GameObjects into the Reflection Probe. Unity only takes this property into account if the Reflection Probe's Type is Custom.  
[resolution](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe-resolution.html) | Resolution of the underlying reflection texture in pixels.  
[shadowDistance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe-shadowDistance.html) | Shadow drawing distance when rendering the probe.  
[size](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe-size.html) | The size of the probe's bounding box in which the probe can contribute to reflections. The size is in world space.  
[texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe-texture.html) | Texture which is passed to the shader of the objects in the vicinity of the reflection probe (Read Only).  
[textureHDRDecodeValues](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe-textureHDRDecodeValues.html) | HDR decode values of the reflection probe texture.  
[timeSlicingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe-timeSlicingMode.html) | Sets this probe time-slicing modeAdditional resources: ReflectionProbeTimeSlicingMode.  
### Public Methods
Method | Description  
---|---  
[IsFinishedRendering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe.IsFinishedRendering.html) | Checks if a probe has finished a time-sliced render.  
[RenderProbe](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe.RenderProbe.html) | Refreshes the probe's cubemap.  
[Reset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe.Reset.html) | Revert all ReflectionProbe parameters to default.  
### Static Methods
Method | Description  
---|---  
[BlendCubemap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe.BlendCubemap.html) | Utility method to blend 2 cubemaps into a target render texture.  
[UpdateCachedState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe.UpdateCachedState.html) | Updates the culling system with the ReflectionProbe's current state. This ensures that Unity correctly culls the ReflectionProbe during rendering if you implement your own runtime reflection system.  
### Events
Event | Description  
---|---  
[defaultReflectionSet](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe-defaultReflectionSet.html) | Adds a delegate to get notifications when the default specular Cubemap is changed.  
[defaultReflectionTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe-defaultReflectionTexture.html) | Adds a delegate to get notifications when the default specular Cubemap is changed.  
[reflectionProbeChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe-reflectionProbeChanged.html) | Adds a delegate to get notifications when a Reflection Probe is added to a Scene or removed from a Scene.  
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
