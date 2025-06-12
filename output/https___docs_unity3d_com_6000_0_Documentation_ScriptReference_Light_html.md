* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html

# Light
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Light.html "Go to Light Component in the Manual")
### Description
Script interface for [light components](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Light.html).
Use this to control all aspects of Unity's lights. The properties are an exact match for the values shown in the Inspector.  
  
For more information about shadow maps, refer to [Shadow Mapping](https://docs.unity3d.com/6000.0/Documentation/Manual/shadow-mapping.html).  
  
Usually lights are just created in the editor, but sometimes you want to create a light from a script:
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Make a game object
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) lightGameObject = new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)("The Light[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html)");  
  
        // Add the light component
        Light[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html) lightComp = lightGameObject.AddComponent<Light[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html)>();  
  
        // Set color and position
        lightComp.color = Color.blue[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-blue.html);  
  
        // Set the position (or any transform property)
        lightGameObject.transform.position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0, 5, 0);
    }
}

```

### Properties
Property | Description  
---|---  
[areaSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-areaSize.html) | The size of the area light.  
[bakingOutput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-bakingOutput.html) | This property describes the output of the last Global Illumination bake.  
[bounceIntensity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-bounceIntensity.html) | The multiplier that defines the strength of the bounce lighting.  
[boundingSphereOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-boundingSphereOverride.html) | Bounding sphere used to override the regular light bounding sphere during culling.  
[color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-color.html) | Specifies the color emitted by the light.  
[colorTemperature](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-colorTemperature.html) |  The color temperature of the light. Correlated Color Temperature (abbreviated as CCT) is multiplied with the color filter when calculating the final color of a light source. The color temperature of the electromagnetic radiation emitted from an ideal black body is defined as its surface temperature in Kelvin. White is 6500K according to the D65 standard. A candle light is 1800K and a soft warm light bulb is 2700K. If you want to use colorTemperature, GraphicsSettings.lightsUseLinearIntensity and Light.useColorTemperature has to be enabled. Additional resources: GraphicsSettings.lightsUseLinearIntensity, GraphicsSettings.useColorTemperature.   
[commandBufferCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-commandBufferCount.html) | Number of command buffers set up on this light (Read Only).  
[cookie](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-cookie.html) | The cookie texture projected by the light.  
[cookieSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-cookieSize.html) | The size of a directional light's cookie.  
[cullingMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-cullingMask.html) | This is used to light certain objects in the Scene selectively.  
[dilatedRange](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-dilatedRange.html) |  The Light.range property describes the range of each point on the light. However, area lights consist of several light-emitting points, and so the effective range is a bit larger, and depends on the size of the area light. This property returns this larger range. Use this property to find whether a given world-space point will be lit by the area light. If not an area light, then returns the same value as Light.range.   
[enableSpotReflector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-enableSpotReflector.html) | Wether a Spot Light should simulate having a reflector.  
[flare](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-flare.html) | The flare asset to use for this light.  
[forceVisible](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-forceVisible.html) | Force a light to be visible even if outside the view frustum.  
[innerSpotAngle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-innerSpotAngle.html) | The angle of the spot light's inner cone in degrees.  
[intensity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-intensity.html) | The Intensity of a light is multiplied with the Light color.  
[layerShadowCullDistances](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-layerShadowCullDistances.html) | Per-light, per-layer shadow culling distances. Directional lights only.   
[lightmapBakeType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-lightmapBakeType.html) | This property describes what part of a light's contribution can be baked (Editor only).  
[lightShadowCasterMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-lightShadowCasterMode.html) | Allows you to override the global Shadowmask Mode per light. Only use this with render pipelines that can handle per light Shadowmask modes. Incompatible with the legacy renderers.  
[lightUnit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-lightUnit.html) | The unit Light.intensity should be displayed in.  
[luxAtDistance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-luxAtDistance.html) | How far away to measure LightUnit.Lux from.  
[range](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-range.html) |  The range of each point of the light. Since area lights have a light emitting surface instead of a single point, the cumulative range of the light is larger than this property. This larger range can be read from the Light.dilatedRange property. For non-area lights, Light.range and Light.dilatedRange return the same value.   
[renderingLayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-renderingLayerMask.html) | Determines which rendering LayerMask this Light affects.  
[renderMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-renderMode.html) | Controls how often the light's contribution is calculated during rendering.  
[shadowAngle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-shadowAngle.html) | Controls the amount of artificial softening applied to the edges of shadows cast by directional lights (Editor only).  
[shadowBias](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-shadowBias.html) | Shadow mapping constant bias.  
[shadowCustomResolution](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-shadowCustomResolution.html) | The custom resolution of the shadow map.  
[shadowMatrixOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-shadowMatrixOverride.html) | Matrix that overrides the regular light projection matrix during shadow culling. Unity uses this matrix if you set Light.useShadowMatrixOverride to true.  
[shadowNearPlane](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-shadowNearPlane.html) | Near plane value to use for shadow frustums.  
[shadowNormalBias](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-shadowNormalBias.html) | Shadow mapping normal-based bias.  
[shadowRadius](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-shadowRadius.html) | Controls the amount of artificial softening applied to the edges of shadows cast by the Point or Spot light (Editor only).  
[shadowResolution](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-shadowResolution.html) | The resolution of the shadow map. Change it to balance shadow visual quality and performance.  
[shadows](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-shadows.html) | Determines if this light will cast soft or hard shadows, or not cast shadows at all.  
[shadowStrength](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-shadowStrength.html) | Strength of light's shadows.  
[spotAngle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-spotAngle.html) | The angle of the spot light's cone in degrees.  
[type](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-type.html) | The type of the light.  
[useBoundingSphereOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-useBoundingSphereOverride.html) | Set to true to override light bounding sphere for culling.  
[useColorTemperature](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-useColorTemperature.html) | Set to true to use the color temperature.  
[useShadowMatrixOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-useShadowMatrixOverride.html) | Set to true to enable custom matrix for culling during shadows.  
[useViewFrustumForShadowCasterCull](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-useViewFrustumForShadowCasterCull.html) | Whether to cull shadows for this Light when the Light is outside of the view frustum.  
### Public Methods
Method | Description  
---|---  
[AddCommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.AddCommandBuffer.html) | Add a command buffer to be executed at a specified place.  
[AddCommandBufferAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.AddCommandBufferAsync.html) | Adds a command buffer to the GPU's async compute queues and executes that command buffer when graphics processing reaches a given point.  
[GetCommandBuffers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.GetCommandBuffers.html) | Get command buffers to be executed at a specified place.  
[RemoveAllCommandBuffers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.RemoveAllCommandBuffers.html) | Remove all command buffers set on this light.  
[RemoveCommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.RemoveCommandBuffer.html) | Remove command buffer from execution at a specified place.  
[RemoveCommandBuffers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.RemoveCommandBuffers.html) | Remove command buffers from execution at a specified place.  
[Reset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.Reset.html) | Revert all light parameters to default.  
[SetLightDirty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.SetLightDirty.html) | Sets a light dirty to notify the light baking backends to update their internal light representation (Editor only).  
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
